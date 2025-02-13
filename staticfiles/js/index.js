let currentIndex = 0;
const slides = document.querySelectorAll(".slide-img");
const dots = document.querySelectorAll(".ellipse-dot");

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove("active");
    dots[i].classList.remove("active");
  });

  slides[index].classList.add("active");
  dots[index].classList.add("active");
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % slides.length;
  showSlide(currentIndex);
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  showSlide(currentIndex);
}

function setSlide(index) {
  currentIndex = index;
  showSlide(currentIndex);
}


document.getElementById("scroll").addEventListener("click", function (e) {
  e.preventDefault();
  document.getElementById("target").scrollIntoView({ behavior: "smooth" });
});
