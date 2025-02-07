$("#loginForm").on("submit", function(event) {
    event.preventDefault();

    const username = $("#username").val();
    const password = $("#password").val();

    // Send data to the Flask backend
    $.post("/login", { username: username, password: password }, function(response) {
        if (response.status === "success") {
            $("#error-message").text("").removeClass("error");
            alert(response.message);
            // Redirect or perform other actions here
        } else {
            $("#error-message").text(response.message).addClass("error");
        }
    });
});
