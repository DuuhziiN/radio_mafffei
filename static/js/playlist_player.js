// ARQUIVO: radiomaffei/static/js/playlist_player.js

document.addEventListener('DOMContentLoaded', () => {

    // Seleciona todos os containers de player customizado na página
    const playerContainers = document.querySelectorAll('.custom-player');

    playerContainers.forEach(container => {
        const audio = container.querySelector('.audio-source');
        const playPauseBtn = container.querySelector('.btn-play-pause-playlist');
        const seekbar = container.querySelector('.player-seekbar');
        const timeCurrent = container.querySelector('.player-time-current');
        const timeDuration = container.querySelector('.player-time-duration');
        const icon = playPauseBtn.querySelector('i');

        // Função utilitária para formatar o tempo (segundos para MM:SS)
        const formatTime = (time) => {
            const minutes = Math.floor(time / 60);
            const seconds = Math.floor(time % 60).toString().padStart(2, '0');
            return `${minutes}:${seconds}`;
        };

        // Atualiza a duração quando o áudio é carregado
        audio.addEventListener('loadedmetadata', () => {
            timeDuration.textContent = formatTime(audio.duration);
            seekbar.max = audio.duration;
        });

        // Toca/Pausa e altera o ícone
        playPauseBtn.addEventListener('click', () => {
            // Se o player global de streaming estiver ativo, pause-o
            const livePlayer = document.getElementById('audio-player');
            if (livePlayer && !livePlayer.paused) {
                livePlayer.pause();
                // O radio.js deve atualizar o ícone do play/pause principal.
            }

            if (audio.paused) {
                audio.play().catch(e => {
                    // Trata o erro de autoplay
                    console.error("Autoplay falhou na playlist:", e);
                });
                icon.classList.remove('fa-play');
                icon.classList.add('fa-pause');
            } else {
                audio.pause();
                icon.classList.remove('fa-pause');
                icon.classList.add('fa-play');
            }
        });

        // Atualiza o tempo e a seekbar enquanto o áudio toca
        audio.addEventListener('timeupdate', () => {
            timeCurrent.textContent = formatTime(audio.currentTime);
            seekbar.value = audio.currentTime;
        });

        // Permite que o usuário arraste a seekbar
        seekbar.addEventListener('input', () => {
            audio.currentTime = seekbar.value;
        });

        // Quando a música termina
        audio.addEventListener('ended', () => {
            icon.classList.remove('fa-pause');
            icon.classList.add('fa-play');
            audio.currentTime = 0; // Volta ao início
        });
    });
});