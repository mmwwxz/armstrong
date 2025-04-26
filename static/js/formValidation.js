document.addEventListener("DOMContentLoaded", function () {
  // Form Validation
  const nameInput = document.querySelector(".frame-input");
  const phoneInput = document.querySelector(".frame-input-10");
  const commentInput = document.querySelector(".frame-input-12");
  const submitBtn = document.querySelector(".frame-13");

  if (submitBtn) {
    submitBtn.addEventListener("click", function (event) {
      event.preventDefault();

      let isValid = true;
      let errorMessage = "";

      const formData = {
        name: nameInput.value.trim(),
        phone: phoneInput.value.trim(),
        comment: commentInput.value.trim() || "Комментария нет",
      };

      // Name validation - only letters allowed
      if (!/^[a-zA-Zа-яА-ЯёЁ\s]+$/.test(formData.name)) {
        isValid = false;
        errorMessage += "Имя должно содержать буквы\n";
        nameInput.style.border = "2px solid red";
      } else {
        nameInput.style.border = "none";
      }

      // Phone validation - 8-15 digits
      if (!/^\d{8,15}$/.test(formData.phone)) {
        isValid = false;
        errorMessage += "Введите корректный номер телефона (8-15 цифр).\n";
        phoneInput.style.border = "2px solid red";
      } else {
        phoneInput.style.border = "none";
      }

      if (!isValid) {
        alert(errorMessage);
      } else {
        console.log(formData);
        alert("Заявка отправлена");

        // Reset form
        if (nameInput) nameInput.value = "";
        if (phoneInput) phoneInput.value = "";
        if (commentInput) commentInput.value = "";
      }
    });
  }
});
