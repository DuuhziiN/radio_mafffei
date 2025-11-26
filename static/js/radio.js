// ARQUIVO: radio.js (CÓDIGO COMPLETO REVISADO)

document.addEventListener('DOMContentLoaded', () => {

    const playPauseBtn = document.getElementById('play-pause-btn');
    const audioPlayer = document.getElementById('audio-player');

    // VARIÁVEL CRÍTICA: Controla se o MediaSource está pronto para aceitar o play.
    let isMediaReady = false;

    // Ouve o evento disparado pelo audio_script.html
    document.addEventListener('mediaSourceReady', () => {
        isMediaReady = true;
        console.log("Status: MediaSource está pronto para reprodução.");
        // Opcional: Você pode tentar habilitar o botão aqui, se estiver desabilitado no HTML
    });

    // Função para manter o ícone sincronizado com o estado do áudio
    const updateIcon = (is_playing) => {
        // ... (código existente para trocar fa-play e fa-pause) ...
        const icon = playPauseBtn.querySelector('i');
        if (is_playing) {
            icon.classList.remove('fa-play');
            icon.classList.add('fa-pause');
        } else {
            icon.classList.remove('fa-pause');
            icon.classList.add('fa-play');
        }
    };

    if (playPauseBtn && audioPlayer) {

        playPauseBtn.addEventListener('click', (event) => {
            event.preventDefault();

            // VERIFICAÇÃO CRÍTICA: Não tente dar play se o MediaSource não estiver pronto
            if (!isMediaReady) {
                console.warn("Player indisponível: Aguardando MediaSource.");
                // Você pode dar um alerta amigável ao usuário aqui:
                // alert("Aguarde. O stream está inicializando. Tente em instantes."); 
                return;
            }

            if (audioPlayer.paused) {
                // Tenta dar Play somente se o MediaSource estiver pronto
                audioPlayer.play().then(() => {
                    updateIcon(true);
                }).catch(error => {
                    // Este é o erro de bloqueio de autoplay que esperamos
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
});