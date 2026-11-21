(() => {
  const control = document.querySelector('.theme-control');
  if (!control) return;
  const select = control.querySelector('select');
  const root = document.documentElement;
  select.value = root.dataset.theme || 'auto';
  control.hidden = false;
  select.addEventListener('change', () => {
    if (select.value === 'auto') delete root.dataset.theme;
    else root.dataset.theme = select.value;
    try {
      if (select.value === 'auto') localStorage.removeItem('gospel-theme');
      else localStorage.setItem('gospel-theme', select.value);
    } catch {}
  });
})();
