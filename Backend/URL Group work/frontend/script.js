
const shortenBtn = document.getElementById("shortenBtn");
const urlInput = document.getElementById("urlInput");
const shortUrl = document.getElementById("shortUrl");
const copyBtn = document.getElementById("copyBtn");
const errorMessage = document.getElementById("errorMessage");


shortenBtn.addEventListener("click", async () => {

    const userUrl = urlInput.value.trim();

    errorMessage.textContent = "";
    shortUrl.value = "";

    if (userUrl === "") {
        errorMessage.textContent = "Please enter a URL.";
        return;
    }

    if (!userUrl.startsWith("http://") && !userUrl.startsWith("https://")) {
        errorMessage.textContent = "Enter valid URL.";
        return;
    }

    try {

        const response = await fetch("http://localhost:5000/shorten", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: userUrl })
        });

        const data = await response.json();

        if (!response.ok) {
            errorMessage.textContent = data.error || "Server error";
            return;
        }

        if (data.short_url) {
            shortUrl.value = data.short_url;
        } else {
            errorMessage.textContent = "Short URL not generated";
        }

    } catch (err) {
        errorMessage.textContent = "Server not responding";
    }
});


copyBtn.addEventListener("click", () => {

    if (shortUrl.value === "") {
        errorMessage.textContent = "Nothing to copy.";
        return;
    }

    navigator.clipboard.writeText(shortUrl.value);

    copyBtn.innerText = "Copied!";

    setTimeout(() => {
        copyBtn.innerText = "Copy";
    }, 1000);
});