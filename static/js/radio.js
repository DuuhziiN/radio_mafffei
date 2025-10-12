// ARQUIVO: radiomaffei/static/js/radio.js

document.addEventListener('DOMContentLoaded', () => {
    // === LÓGICA DE CONEXÃO DO PLAYER (HOME PAGE) ===

    const playPauseBtn = document.getElementById('play-pause-btn');
    const audioPlayer = document.getElementById('audio-player');

    // Este código só deve rodar se o botão estilizado e o player de streaming existirem
    if (playPauseBtn && audioPlayer) {
        playPauseBtn.addEventListener('click', (event) => {
            event.preventDefault(); // Impede o link de navegar (para o 'a href="#"')

            const icon = playPauseBtn.querySelector('i');

            if (audioPlayer.paused) {
                // Tenta dar Play no player do Channels
                audioPlayer.play().catch(error => {
                    console.error("Erro ao tentar dar Play:", error);
                    alert("A reprodução foi bloqueada pelo navegador. Tente novamente clicando no botão.");
                });
                icon.classList.remove('fa-play');
                icon.classList.add('fa-pause');
            } else {
                // Dá Pause
                audioPlayer.pause();
                icon.classList.remove('fa-pause');
                icon.classList.add('fa-play');
            }
        });

        // Mantém o ícone sincronizado com o estado do áudio
        audioPlayer.addEventListener('play', () => {
            const icon = playPauseBtn.querySelector('i');
            icon.classList.remove('fa-play');
            icon.classList.add('fa-pause');
        });

        audioPlayer.addEventListener('pause', () => {
            const icon = playPauseBtn.querySelector('i');
            icon.classList.remove('fa-pause');
            icon.classList.add('fa-play');
        });
    }
});