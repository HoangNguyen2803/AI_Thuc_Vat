// Tooltip hiển thị sinh động
const tooltip = document.getElementById('tooltip');

document.querySelectorAll('.sector').forEach(el => {
  el.addEventListener('mouseenter', (e) => {
    tooltip.textContent = el.title;
    tooltip.style.left = e.pageX + 'px';
    tooltip.style.top  = e.pageY + 'px';
    tooltip.classList.remove('hidden');
  });
  el.addEventListener('mouseleave', () => {
    tooltip.classList.add('hidden');
  });
});
