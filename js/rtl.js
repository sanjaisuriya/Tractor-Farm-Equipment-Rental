/**
 * Tractor & Farm Equipment Rental - RTL / LTR Manager
 * Direction toggle with LocalStorage persistence
 */

(function () {
  const DIR_KEY = 'trarent_direction';

  function applyDirection(dir) {
    const html = document.documentElement;
    html.setAttribute('dir', dir);
    localStorage.setItem(DIR_KEY, dir);

    updateRtlToggleButtons(dir);
  }

  function updateRtlToggleButtons(dir) {
    const btns = document.querySelectorAll('.rtl-toggle-btn');
    btns.forEach(btn => {
      const textSpan = btn.querySelector('.dir-label');
      if (textSpan) {
        textSpan.textContent = dir === 'rtl' ? 'LTR' : 'RTL';
      }
      btn.setAttribute('title', dir === 'rtl' ? 'Switch to Left-to-Right' : 'Switch to Right-to-Left');
    });
  }

  function initDirection() {
    const savedDir = localStorage.getItem(DIR_KEY) || 'ltr';
    applyDirection(savedDir);

    document.addEventListener('DOMContentLoaded', () => {
      updateRtlToggleButtons(savedDir);

      document.querySelectorAll('.rtl-toggle-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          const currentDir = document.documentElement.getAttribute('dir') || 'ltr';
          applyDirection(currentDir === 'rtl' ? 'ltr' : 'rtl');
        });
      });
    });
  }

  initDirection();
  window.trarentRtl = { applyDirection };
})();
