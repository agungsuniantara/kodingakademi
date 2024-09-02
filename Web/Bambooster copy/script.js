let currentOpen = null;

function toggleAnswer(button) {
    let answerElement = document.getElementById(button.id.replace('button', 'answer'));

    if (currentOpen === answerElement) {
        answerElement.classList.add('hidden');
        currentOpen = null;
    } else {
        if (currentOpen !== null) {
            currentOpen.classList.add('hidden');
        }
        answerElement.classList.remove('hidden');
        currentOpen = answerElement;
    }
}



