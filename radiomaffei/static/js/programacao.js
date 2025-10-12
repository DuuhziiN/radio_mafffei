document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const conteudoDias = document.querySelectorAll('.conteudo-dia');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const diaSelecionado = button.getAttribute('data-dia');

            tabButtons.forEach(btn => btn.classList.remove('active'));

            button.classList.add('active');

            conteudoDias.forEach(conteudo => {
                conteudo.classList.remove('active');
            });

            const conteudoAtivo = document.getElementById(diaSelecionado);
            if (conteudoAtivo) {
                conteudoAtivo.classList.add('active');
            }
        });
    });
});