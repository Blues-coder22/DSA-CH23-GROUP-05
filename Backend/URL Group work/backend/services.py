import random
import string
from models import URL


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    # Keep generating until we find a unique code. With a large
    # character space this will succeed quickly; avoid an arbitrary
    # max attempts that could return an error to the user.
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        if not URL.query.filter_by(short_code=code).first():
            return code