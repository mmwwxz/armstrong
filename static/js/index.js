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


document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector(".header");
  const navToggle = document.createElement("div");
  navToggle.className = "nav-toggle";
  navToggle.innerHTML = `
    <span style="display:block; width:30px; height:3px; background:#fff; margin-bottom:5px;"></span>
    <span style="display:block; width:30px; height:3px; background:#fff; margin-bottom:5px;"></span>
    <span style="display:block; width:30px; height:3px; background:#fff;"></span>
  `;
  header.appendChild(navToggle);

  const nav = document.querySelector(".nav");

  if (window.innerWidth <= 768) {
    nav.style.display = "none";
  }

  navToggle.addEventListener("click", function () {
    if (nav.style.display === "none" || nav.style.display === "") {
      nav.style.display = "flex";
      document.body.classList.add("mobile-menu-active");
    } else {
      nav.style.display = "none";
      document.body.classList.remove("mobile-menu-active");
    }
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 768) {
      nav.style.display = "flex";
    } else {
      if (!document.body.classList.contains("mobile-menu-active")) {
        nav.style.display = "none";
      }
    }
  });
});

function adjustSliderForMobile() {
  const box = document.querySelector(".box");
  if (window.innerWidth <= 768) {
    box.style.height = "220px";
  } else if (window.innerWidth <= 480) {
    box.style.height = "180px";
  } else {
    box.style.height = "360px";
  }
}

window.addEventListener("load", adjustSliderForMobile);
window.addEventListener("resize", adjustSliderForMobile);

document.addEventListener("DOMContentLoaded", function () {
  // Создаем кнопку для мобильного меню
  const header = document.querySelector(".header");

  if (!document.querySelector(".nav-toggle")) {
    const navToggle = document.createElement("div");
    navToggle.className = "nav-toggle";
    navToggle.innerHTML = `
      <span style="display:block; width:30px; height:3px; background:#fff; margin-bottom:5px;"></span>
      <span style="display:block; width:30px; height:3px; background:#fff; margin-bottom:5px;"></span>
      <span style="display:block; width:30px; height:3px; background:#fff;"></span>
    `;
    header.appendChild(navToggle);

    // Получаем навигацию
    const nav = document.querySelector(".nav");

    // Изначально скрываем меню на мобильных устройствах
    if (window.innerWidth <= 768) {
      nav.style.display = "none";
    }

    // Добавляем переключение по клику
    navToggle.addEventListener("click", function () {
      if (nav.style.display === "none" || nav.style.display === "") {
        nav.style.display = "flex";
        nav.style.flexDirection = "column";
        document.body.classList.add("mobile-menu-active");
      } else {
        nav.style.display = "none";
        document.body.classList.remove("mobile-menu-active");
      }
    });

    // Обработчик изменения размера окна
    window.addEventListener("resize", function () {
      if (window.innerWidth > 768) {
        nav.style.display = "flex";
        nav.style.flexDirection = "row";
      } else {
        if (!document.body.classList.contains("mobile-menu-active")) {
          nav.style.display = "none";
        } else {
          nav.style.flexDirection = "column";
        }
      }
    });
  }

  // Добавляем стили ховера через JavaScript для мобильных устройств
  const cards = document.querySelectorAll(".card, .card-7, .card-9, .card-b");

  cards.forEach((card) => {
    card.addEventListener("touchstart", function () {
      this.classList.add("touch-active");
    });

    card.addEventListener("touchend", function () {
      setTimeout(() => {
        this.classList.remove("touch-active");
      }, 300);
    });
  });
});

// Исправляем отображение продуктов на мобильном
function fixMobileProductsLayout() {
  if (window.innerWidth <= 768) {
    const frame16 = document.querySelector(".frame-16");
    if (frame16) {
      // Убедимся, что продукты отображаются в столбик
      frame16.style.flexDirection = "column";
      frame16.style.alignItems = "center";

      // Корректируем стили для карточек продуктов
      const productCards = document.querySelectorAll(
        ".component-17, .component-19, .component-1b"
      );
      productCards.forEach((card) => {
        card.style.width = "100%";
        card.style.marginBottom = "20px";
      });
    }
  }
}

// Запускаем функцию при загрузке и изменении размера окна
window.addEventListener("DOMContentLoaded", fixMobileProductsLayout);
window.addEventListener("resize", fixMobileProductsLayout);