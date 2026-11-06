/**
 * Tractor & Farm Equipment Rental - Theme Manager
 * Dark / Light Mode with LocalStorage persistence
 */

(function () {
  const THEME_KEY = 'trarent_theme';

  function applyTheme(theme) {
    const html = document.documentElement;
    html.classList.add('theme-transition');

    if (theme === 'dark') {
      html.classList.add('dark');
    } else {
      html.classList.remove('dark');
    }

    localStorage.setItem(THEME_KEY, theme);
    updateThemeToggleIcons(theme);

    setTimeout(() => {
      html.classList.remove('theme-transition');
    }, 300);
  }

  function updateThemeToggleIcons(theme) {
    const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
    toggleBtns.forEach(btn => {
      const icon = btn.querySelector('i');
      if (icon) {
        if (theme === 'dark') {
          icon.className = 'fa-solid fa-sun text-yellow-400';
          btn.setAttribute('aria-label', 'Switch to light mode');
          btn.setAttribute('title', 'Switch to light mode');
        } else {
          icon.className = 'fa-solid fa-moon text-slate-700 dark:text-slate-200';
          btn.setAttribute('aria-label', 'Switch to dark mode');
          btn.setAttribute('title', 'Switch to dark mode');
        }
      }
    });
  }

  function initTheme() {
    const savedTheme = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

    applyTheme(initialTheme);

    document.addEventListener('DOMContentLoaded', () => {
      updateThemeToggleIcons(initialTheme);

      document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          const isDark = document.documentElement.classList.contains('dark');
          applyTheme(isDark ? 'light' : 'dark');
        });
      });
    });
  }

  initTheme();
  window.trarentTheme = { applyTheme };
})();
