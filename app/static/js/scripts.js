document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (e) {
        const urlField = document.querySelector("#url");
        const htmlField = document.querySelector("#html");

        if (!urlField.value && !htmlField.value) {
            e.preventDefault();
            alert("Por favor, ingresa una URL o código HTML para validar.");
        }
    });
});
