// Get HTML elements
const shortenBtn = document.getElementById("shortenBtn");
const urlInput = document.getElementById("urlInput");
const shortUrl = document.getElementById("shortUrl");
const copyBtn = document.getElementById("copyBtn");
const errorMessage = document.getElementById("errorMessage");


// button is clicked
shortenBtn.addEventListener("click", () => {

    // Get input value
    const userUrl = urlInput.value.trim();

    // Clear previous error
    errorMessage.textContent = "";

    // Check if input is empty
    if(userUrl === ""){
        errorMessage.textContent = "Please enter a URL.";
        return;
    }

    // Simple URL validation
    if(
        !userUrl.startsWith("http://") &&
        !userUrl.startsWith("https://")
    ){
        errorMessage.textContent = "Please enter a valid URL.";
        return;
    }

    // Fake shortened URL
    const randomCode = Math.random()
        .toString(36)
        .substring(2, 8);

    const generatedShortUrl = `short.ly/${randomCode}`;

    // Display shortened URL
    shortUrl.value = generatedShortUrl;

});


// Copy button functionality
copyBtn.addEventListener("click", () => {

    // Check if there is a short URL
    if(shortUrl.value === ""){
        errorMessage.textContent = "Nothing to copy.";
        return;
    }

    // Copy text
    navigator.clipboard.writeText(shortUrl.value);

    // Success message
    alert("Short URL copied!");

});