document.getElementById("consultation-form").addEventListener("submit", function(event) {
    event.preventDefault();

    fetch("/request_consultation", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            mobile: document.getElementById("mobile").value,
            disease: document.getElementById("disease").value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response-message").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
});
