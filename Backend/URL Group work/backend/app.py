from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

from models import db, URL
from services import generate_short_code

from dsa import (
    cache_url,
    get_cached_url,
    push_deleted,
    pop_restore,
    add_request,
    process_request,
    sort_urls_by_clicks,
    binary_search,
    add_click,
    get_top_clicked
)

app = Flask(__name__)
CORS(app)

# =========================
# DATABASE (XAMPP MYSQL)
# =========================
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:@localhost/url_shortener'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# =========================
# SHORTEN URL
# =========================
@app.route('/shorten', methods=['POST'])
def shorten():
    try:
        data = request.json
        long_url = data.get("url")

        if not long_url:
            return jsonify({"error": "URL is required"}), 400

        add_request(long_url)
        process_request()

        code = generate_short_code()

        short_link = f"http://localhost:5000/{code}"

        cache_url(code, long_url)

        new_url = URL(
            original_url=long_url,
            short_code=code
        )

        db.session.add(new_url)
        db.session.commit()

        return jsonify({
            "message": "Success",
            "short_url": short_link,
            "code": code
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# REDIRECT
# =========================
@app.route("/<short_code>")
def redirect_url(short_code):
    try:

        cached = get_cached_url(short_code)
        if cached:
            add_click(short_code, 1)
            return redirect(cached)

        url = URL.query.filter_by(short_code=short_code).first()

        if url:
            url.click_count += 1
            db.session.commit()

            cache_url(short_code, url.original_url)
            add_click(short_code, url.click_count)

            return redirect(url.original_url)

        return jsonify({"error": "URL not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# GET ALL URLS
# =========================
@app.route("/urls", methods=["GET"])
def get_urls():
    try:
        urls = URL.query.all()

        return jsonify([
            {
                "id": u.id,
                "original_url": u.original_url,
                "short_code": u.short_code,
                "click_count": u.click_count
            }
            for u in urls
        ])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# DELETE (STACK)
# =========================
@app.route("/url/<int:id>", methods=["DELETE"])
def delete_url(id):
    try:
        url = URL.query.get(id)

        if not url:
            return jsonify({"error": "URL not found"}), 404

        push_deleted({
            "id": url.id,
            "original_url": url.original_url,
            "short_code": url.short_code,
            "click_count": url.click_count
        })

        db.session.delete(url)
        db.session.commit()

        return jsonify({"message": "Deleted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# UNDO (STACK)
# =========================
@app.route("/undo", methods=["POST"])
def undo_delete():
    try:
        restored = pop_restore()

        if not restored:
            return jsonify({"message": "Nothing to restore"}), 400

        url = URL(
            id=restored["id"],
            original_url=restored["original_url"],
            short_code=restored["short_code"],
            click_count=restored["click_count"]
        )

        db.session.add(url)
        db.session.commit()

        return jsonify({"message": "Restored successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# TOP URLs (SORTING)
# =========================
@app.route("/top-urls", methods=["GET"])
def top_urls():
    try:
        urls = URL.query.all()
        sorted_urls = sort_urls_by_clicks(urls)

        return jsonify([
            {
                "short_code": u.short_code,
                "click_count": u.click_count
            }
            for u in sorted_urls[:5]
        ])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# SEARCH (BINARY SEARCH)
# =========================
@app.route("/search/<short_code>", methods=["GET"])
def search_url(short_code):
    try:
        urls = URL.query.all()
        urls_sorted = sorted(urls, key=lambda x: x.short_code)

        codes = [u.short_code for u in urls_sorted]

        index = binary_search(codes, short_code)

        if index == -1:
            return jsonify({"message": "Not found"}), 404

        url = urls_sorted[index]

        return jsonify({
            "short_code": url.short_code,
            "original_url": url.original_url,
            "click_count": url.click_count
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# TOP CLICKED (HEAP)
# =========================
@app.route("/top-clicked", methods=["GET"])
def top_clicked():
    try:
        return jsonify(get_top_clicked())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Bitly-lite Backend Running (FULL DSA SYSTEM)"


if __name__ == "__main__":
    app.run(debug=True)