const loginNavItem = document.querySelector('.nav-item:nth-child(2)');

loginNavItem.addEventListener('mouseenter', () => {
  loginNavItem.style.transform = 'translateX(-20%)';
});

loginNavItem.addEventListener('mouseleave', () => {
  loginNavItem.style.transform = 'translateX(0%)';
});