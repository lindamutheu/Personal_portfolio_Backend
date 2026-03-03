let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll("header nav a");

window.addEventListener("scroll", () => {
    let top = window.scrollY;

    sections.forEach(sec => {
        let offset = sec.offsetTop - 100;
        let height = sec.offsetHeight;
        let id = sec.getAttribute("id");

        if (top >= offset && top < offset + height) {
            navLinks.forEach(link => link.classList.remove("active"));
            document.querySelector(`header nav a[href="#${id}"]`)?.classList.add("active");
        }
    });
});

function fireConfetti() {
    if (typeof confetti !== "undefined") {
        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    }
}

let script = document.createElement("script");
script.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js";
document.body.appendChild(script);
