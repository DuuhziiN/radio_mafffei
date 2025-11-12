// ARQUIVO: radiomaffei/static/js/radio.js

document.addEventListener('DOMContentLoaded', () => {

    // --- Variáveis de Controle ---
    const playPauseBtn = document.getElementById('play-pause-btn');
    const audioPlayer = document.getElementById('audio-player');

    // Este código só deve rodar se o botão estilizado e o player de streaming existirem
    if (playPauseBtn && audioPlayer) {

        // Função para manter o ícone sincronizado com o estado do áudio
        const updateIcon = (is_playing) => {
            const icon = playPauseBtn.querySelector('i');
            if (is_playing) {
                icon.classList.remove('fa-play');
                icon.classList.add('fa-pause');
            } else {
                icon.classList.remove('fa-pause');
                icon.classList.add('fa-play');
            }
        };

        playPauseBtn.addEventListener('click', (event) => {
            event.preventDefault();

            if (audioPlayer.paused) {
                // Tenta dar Play no player do Channels (o stream)
                audioPlayer.play().then(() => {
                    updateIcon(true);
                }).catch(error => {
                    console.error("Erro ao iniciar playback (autoplay bloqueado):", error);
                    alert("A reprodução de áudio foi bloqueada. Tente dar Play novamente.");
                    updateIcon(false);
                });
            } else {
                // Dá Pause
                audioPlayer.pause();
                updateIcon(false);
            }
        });

        // Mantém o ícone sincronizado se o áudio for iniciado/parado por outro lugar
        audioPlayer.addEventListener('play', () => updateIcon(true));
        audioPlayer.addEventListener('pause', () => updateIcon(false));
    }

    // --- Nota: A lógica de Slideshow e Menu está em seus respectivos arquivos ---

});