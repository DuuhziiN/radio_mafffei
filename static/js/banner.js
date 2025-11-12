// ARQUIVO: radiomaffei/static/js/banner.js

let slideIndex = 0;

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");

    // Se não houver slides, pare a função
    if (slides.length === 0) return;

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }

    // Exibe o slide atual
    slides[slideIndex - 1].style.display = "block";

    // Chama a função novamente após 4 segundos
    setTimeout(showSlides, 4000);
}

document.addEventListener('DOMContentLoaded', () => {
    // Inicia o slideshow
    showSlides();
});