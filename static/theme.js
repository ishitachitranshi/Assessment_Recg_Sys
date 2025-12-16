const toggle = document.getElementById('toggle');

toggle.onclick = () => {
  document.body.classList.toggle('dark');
  toggle.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
};