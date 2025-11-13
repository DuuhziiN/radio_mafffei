/* ARQUIVO: radiomaffei/static/js/menu.js (CÓDIGO FINAL DE FUNCIONALIDADE MOBILE) */

class MobileNavbar {
    constructor(mobileMenu, navList, navLinks) {
        this.mobileMenu = document.querySelector(mobileMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active";

        this.handleClick = this.handleClick.bind(this);
    }

    animateLinks() {
        this.navLinks.forEach((link) => {
            link.style.animation
                ? (link.style.animation = "")
                : (link.style.animation = `navLinkFade 0.5s ease forwards 0.3s`);
        });
    }

    handleClick() {
        // 1. Alterna a classe 'active' no nav-list (para aparecer/sumir)
        this.navList.classList.toggle(this.activeClass);
        // 2. Alterna a classe 'active' no mobile-menu (para virar o 'X')
        this.mobileMenu.classList.toggle(this.activeClass);
        this.animateLinks();
    }

    addClickEvent() {
        // Adiciona o evento de clique
        if (this.mobileMenu) {
            this.mobileMenu.addEventListener("click", this.handleClick);
        }
    }

    init() {
        // O init será chamado SOMENTE após o DOM carregar
        if (this.mobileMenu) {
            this.addClickEvent();
            // Garante que a nav-list esteja invisível ao iniciar em mobile
            // Embora o CSS faça isso, é uma garantia extra
            this.navList.classList.remove(this.activeClass);
        }
        return this;
    }
}

// CRÍTICO: Inicializa a classe após o DOM carregar
document.addEventListener('DOMContentLoaded', () => {
    const mobileNavbar = new MobileNavbar(
        ".mobile-menu",
        ".nav-list",
        ".nav-list li",
    );
    mobileNavbar.init();
});