/* ARQUIVO: radiomaffei/static/js/menu.js (CÓDIGO FINAL DE FUNCIONALIDADE MOBILE) */

class MobileNavbar {
    constructor(mobileMenu, navList, navLinks) {
        // Seleciona os elementos essenciais
        this.mobileMenu = document.querySelector(mobileMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active"; // Classe CSS que ativa/desativa

        // Liga o método handleClick ao objeto correto
        this.handleClick = this.handleClick.bind(this);
    }

    // Função que aplica o efeito de fade-in/fade-out
    animateLinks() {
        this.navLinks.forEach((link) => {
            // Este código é baseado no CSS de animação que você forneceu
            link.style.animation
                ? (link.style.animation = "")
                : (link.style.animation = `navLinkFade 0.5s ease forwards 0.3s`);
        });
    }

    handleClick() {
        // 1. Alterna a classe 'active' para MOSTRAR/ESCONDER o menu
        this.navList.classList.toggle(this.activeClass);
        // 2. Alterna a classe 'active' no ícone (para transformá-lo em 'X')
        this.mobileMenu.classList.toggle(this.activeClass);
        // 3. Aplica a animação
        this.animateLinks();
    }

    addClickEvent() {
        // Liga a função ao clique
        if (this.mobileMenu) {
            this.mobileMenu.addEventListener("click", this.handleClick);
        }
    }

    init() {
        if (this.mobileMenu) {
            this.addClickEvent();
        }
        return this;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Inicializa a navegação mobile
    const mobileNavbar = new MobileNavbar(
        ".mobile-menu", // Seletor para o ícone de hambúrguer
        ".nav-list",    // Seletor para a lista de links
        ".nav-list li", // Seletor para cada link (para animação)
    );
    mobileNavbar.init();
});