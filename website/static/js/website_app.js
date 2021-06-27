// Toggle sidebar
const hamburger = document.querySelector("#hamburger");
const sidebar = document.querySelector("#sidebar");
hamburger.addEventListener("click", (event) => {
  hamburger.classList.toggle("active");
  sidebar.classList.toggle("active");

  if (window.scrollY > 100) {
    window.scrollTo(0, 40);
  }
});

document.addEventListener("click", (event) => {
  if (!sidebar.contains(event.target) && !hamburger.contains(event.target)) {
    sidebar.classList.remove("active");
    hamburger.classList.remove("active");
  }
});
