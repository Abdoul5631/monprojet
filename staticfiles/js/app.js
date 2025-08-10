// Affiche un message de bienvenue dans la console
console.log("Bienvenue sur la liste des CVs !");

// Exemple de manipulation DOM : Ajoute un style à un élément avec l'id "title"
document.addEventListener("DOMContentLoaded", function () {
    const titleElement = document.getElementById("title");
    if (titleElement) {
        titleElement.style.color = "blue";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    // Exemple : Confirmation avant suppression
    const deleteButtons = document.querySelectorAll(".btn-delete");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmation = confirm("Êtes-vous sûr de vouloir supprimer ce CV ?");
            if (!confirmation) {
                event.preventDefault(); // Empêche l'action si non confirmé
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Exemple : Confirmation avant suppression
    const deleteButtons = document.querySelectorAll(".btn-delete");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmation = confirm("Êtes-vous sûr de vouloir supprimer ce CV ?");
            if (!confirmation) {
                event.preventDefault(); // Empêche l'action si non confirmé
            }
        });
    });
});
