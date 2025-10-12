document.addEventListener('DOMContentLoaded', () => {
    const audio = document.getElementById('radio-stream');
    const playPauseBtn = document.getElementById('play-pause-btn');
    const icon = playPauseBtn.querySelector('i');
    let isPlaying = false;

    function playRadio() {
        audio.play().then(() => {
            isPlaying = true;
            icon.classList.remove('fa-play');
            icon.classList.add('fa-pause');
        }).catch(error => {
            // Trata erro de autoplay bloqueado (comum em navegadores móveis)
            alert('O navegador bloqueou o início automático do áudio. Tente novamente clicando no botão.');
            console.error("Erro ao tentar tocar o áudio:", error);
        });
    }


    function pauseRadio() {
        audio.pause();
        isPlaying = false;
        icon.classList.remove('fa-pause');
        icon.classList.add('fa-play');
    }


    playPauseBtn.addEventListener('click', () => {
        if (isPlaying) {
            pauseRadio();
        } else {
            playRadio();
        }
    });


    icon.classList.add('fa-play');
});