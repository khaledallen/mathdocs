const stepContainer = document.querySelector(".proof");
let rawSteps = stepContainer.innerHTML;
stepContainer.innerHTML = stepBuilder(rawSteps.split('[STEP]'));

let steps = document.querySelectorAll(".step")
toggleSteps(steps);

function stepBuilder(stepsArr) {
    let formattedSteps = [];
    stepsArr.forEach( (val, idx) => {
        let html = `<div class="step"><a href="#"><h4>Step ${idx+1}</h4></a><p class="step-body hide">${val}</p></div>`
        formattedSteps.push(html);
    });
    return formattedSteps.join('');
}

function toggleSteps(stepsElements) {
    stepsElements.forEach( step => {
        const title = step.querySelector('h4');
        const body = step.querySelector('p');
        title.addEventListener('click', evt => {
            body.classList.toggle('hide');
        });
    });
}