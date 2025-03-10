
// text function 
const texts = ['Project Manager',' ', ' ', '<Backend Developer/>'];
let index = 0;
let charIndex = 0;
let currentText = '';
let isDeleting = false;
let cycleCount = 0;
const maxCycles = 10;
const typingSpeed = 200;
const eraseSpeed = 100;
const delayBetweenText = 10000;

function type() {
    const target = document.getElementById('typing-text');
    if (cycleCount >= maxCycles){
        target.textContent =texts[texts.length - 1];
        return;
    }
    
    currentText = texts[index];
    // Typing the text 
    if (!isDeleting && charIndex <= currentText.length) {
            target.textContent = currentText.slice(0, charIndex++) + "|";
            setTimeout(type, typingSpeed);
    } 
    // Erasing the text 
    else if (isDeleting && charIndex >= 0){
        target.textContent = currentText.slice(0, charIndex--) + "|";
        setTimeout(type, eraseSpeed);
    }

    // Once the word is fully typed 
    if (charIndex === currentText.length){
        isDeleting = true;
        setTimeout(type, delayBetweenText);
    }

    if (charIndex === -1){
        isDeleting = false;
        index = (index + 1) % texts.length;
        cycleCount ++;
        setTimeout(type, typingSpeed)
    }
}

window.onload = type;

// project function 
const projectNumber = 162;
const projectDuration = 1000;
const duration = 10000;

function project(target, projectDuration) {
    const start = 0; // starting number
    const increment = target / (projectDuration/50); // the increment value
    let currentNumber = start;

    const interval = setInterval (() => {
        currentNumber += increment // increase the current number

        if (currentNumber >= target){
            clearInterval(interval);
            currentNumber = target; 
        }    

        document.getElementById('projectNumber').innerText = Math.floor(currentNumber) + "+";
    }, 50);
}

project(projectNumber, duration)

// Links 
const links = document.querySelectorAll('.scroll-link')

// Event listener to all links 
links.forEach(link =>{
    link.addEventListener('click', function(event){
        event.preventDefault(); //prevent default behaviour
        const targetID = this.getAttribute('data-target'); //target ID section
        const targetSection = document.getElementById(targetID);

        window.scrollTo({
            top: targetSection.offsetTop,
            behavior: 'smooth'  
        })
    })
})

//CV download
document.getElementById('download-btn').addEventListener('click', function(){
    const downloadLink = document.createElement('a');
    downloadLink.href = '/AMARACHUKWU AGUOLU DIVINE CV.pdf';
    downloadLink.download = 'AMARACHUKWU AGUOLU DIVINE CV.pdf';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
})

//ScroLl to the top
let myButton = document.getElementById("scrollToTopBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150){
        myButton.style.display = "block";
    }
    else{
        myButton.style.display = "none"
    }
}

function topFunction() {
    document.body.scrollTop = 10;
    document.documentElement.scrollTop = 10;
}

myButton.addEventListener("click", topFunction)

// Display Message



//current year
const currentYear = new Date().getFullYear();
document.getElementById('current-year').textContent = currentYear;