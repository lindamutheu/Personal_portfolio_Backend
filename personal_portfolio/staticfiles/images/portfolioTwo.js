let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll("header nav a");

window.onscroll = () => {
    sections.forEach(sec => {
         let top = window.scrollY;
         let offset = sec.offsetTop;
         let height = sec.offsetHeight;
         let id = sec.getAttribute("id");


         if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector("header nav a[href# =' + id + ']").classList.add('active');

            });
         };
    });
    const text = document.getElementById("box");
    const btn = document.getElementById("btn anim");
    
    btn.addEventListener("click", () => {
        text.classList.toggle("expanded");
    
        if (text.classList.contains("expanded")) {
            btn.textContent = "Read Less";
        } else {
            btn.textContent = "Read More";
        }
    });


};

function fireConfetti() {
    const confettiSettings = { particleCount: 100, spread: 70, origin: { y: 0.7 } };
    confetti(confettiSettings);
}

// Load Confetti Library
const script = document.createElement("script");
script.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.3.2/dist/confetti.browser.min.js";
script.onload = () => console.log("Confetti loaded");
document.body.appendChild(script);





