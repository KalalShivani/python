const form = document.getElementById("userForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone");
const passwordInput = document.getElementById("password");
const successMsg = document.getElementById("success");

function showError(input, message) {
  const error = input.nextElementSibling;
  error.textContent = message;
  input.style.borderColor = "red";
}

function clearError(input) {
  const error = input.nextElementSibling;
  error.textContent = "";
  input.style.borderColor = "#ccc";
}

function validateName() {
  const value = nameInput.value.trim();
  if (value === "") {
    showError(nameInput, "Name is required");
    return false;
  }
  clearError(nameInput);
  return true;
}

function validateEmail() {
  const value = emailInput.value.trim();
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(value)) {
    showError(emailInput, "Enter a valid email");
    return false;
  }
  clearError(emailInput);
  return true;
}

function validatePhone() {
  const value = phoneInput.value.trim();
  const regex = /^\d{10}$/;
  if (!regex.test(value)) {
    showError(phoneInput, "Enter 10-digit phone number");
    return false;
  }
  clearError(phoneInput);
  return true;
}

function validatePassword() {
  const value = passwordInput.value;
  if (value.length < 6) {
    showError(passwordInput, "Password must be at least 6 characters");
    return false;
  }
  clearError(passwordInput);
  return true;
}

form.addEventListener("input", () => {
  successMsg.textContent = "";
});

nameInput.addEventListener("blur", validateName);
emailInput.addEventListener("blur", validateEmail);
phoneInput.addEventListener("blur", validatePhone);
passwordInput.addEventListener("blur", validatePassword);

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const isValid =
    validateName() &&
    validateEmail() &&
    validatePhone() &&
    validatePassword();

  if (isValid) {
    successMsg.textContent = "Form submitted successfully!";
    form.reset();
  }
});

