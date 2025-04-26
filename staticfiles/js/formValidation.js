document.addEventListener("DOMContentLoaded", function () {
  const nameInput = document.querySelector(".frame-input");
  const phoneInput = document.querySelector(".frame-input-10");
  const commentInput = document.querySelector(".frame-input-12");
  const submitBtn = document.querySelector(".frame-13");

  submitBtn.addEventListener("click", function (event) {
    event.preventDefault();

    let isValid = true;
    let errorMessage = "";

    const formData = {
      name: nameInput.value.trim(),
      phone: phoneInput.value.trim(),
      comment: commentInput.value.trim() || "Комментария нет",
    };

    if (!/^[a-zA-Zа-яА-ЯёЁ\s]+$/.test(formData.name)) {
      isValid = false;
      errorMessage += "Имя должно содержать буквы \n";
      nameInput.style.border = "2px solid red";
    } else {
      nameInput.style.border = "1px solid #ccc";
    }

    if (!/^\d{8,15}$/.test(formData.phone)) {
      isValid = false;
      errorMessage += "Введите корректный номер телефона (8-15 цифр).\n";
      phoneInput.style.border = "2px solid red";
    } else {
      phoneInput.style.border = "1px solid #ccc";
    }

    if (!isValid) {
      alert(errorMessage);
    } else {
      console.log(formData);
      alert("Заявка отправлена");
    }
  });
});
