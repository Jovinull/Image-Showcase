document.addEventListener('DOMContentLoaded', function () {
    const carouselElement = document.querySelector('#carouselExampleIndicators');
    const carousel = new bootstrap.Carousel(carouselElement, {
        interval: 1000,  // Altere conforme necessário
        ride: 'carousel'
    });

    // Adiciona listeners para eventos de visibilidade da página
    document.addEventListener('visibilitychange', function () {
        if (document.visibilityState === 'visible') {
            carousel.cycle();
        } else {
            carousel.pause();
        }
    });

    // Adiciona listeners para eventos de tela cheia
    document.addEventListener('fullscreenchange', function () {
        if (document.fullscreenElement) {
            carousel.cycle();
        } else {
            carousel.pause();
        }
    });
});
