document.getElementById('scroll-left').addEventListener('click', function() {
    document.querySelector('.container').scrollLeft -= 1360;
});

document.getElementById('scroll-right').addEventListener('click', function() {
    document.querySelector('.container').scrollLeft += 1360;
});

let scrollInterval;

function startAutoScroll() {
    scrollInterval = setInterval(function() {
        document.querySelector('.container').scrollLeft += 1360;
    }, 8000);
}

startAutoScroll();



// let container = document.querySelector('.container');
// let startTime;
// let currentX = 0;
// let targetX = 1360;
// let duration = 3000;

// function animate(time) {
//     if (startTime === undefined) {
//         startTime = time;
//     }

//     const elapsed = time - startTime;
//     const progress = Math.min(elapsed / duration, 1);

//     currentX = targetX * progress;

//     container.scrollLeft = currentX;

//     if (progress < 1) {
//         requestAnimationFrame(animate);
//     }
// }

// function startAutoScroll() {
//     requestAnimationFrame(animate);
// }

// startAutoScroll();