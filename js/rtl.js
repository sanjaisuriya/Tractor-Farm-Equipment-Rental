/**
 * Tractor & Farm Equipment Rental - RTL / LTR Manager
 * Direction toggle with LocalStorage persistence and directional arrow icons
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
    const isRtl = dir === 'rtl';
    const btns = document.querySelectorAll('.rtl-toggle-btn');
    btns.forEach(btn => {
      const icon = btn.querySelector('i');
      if (icon) {
        icon.className = 'fa-solid fa-right-left text-sm';
      }

      // Ensure no text remains inside button
      const label = btn.querySelector('.dir-label');
      if (label) {
        label.remove();
      }

      btn.setAttribute('title', isRtl ? 'Active Direction: RTL (Click for LTR)' : 'Active Direction: LTR (Click for RTL)');
      btn.setAttribute('aria-label', isRtl ? 'Switch to Left-to-Right layout' : 'Switch to Right-to-Left layout');

      if (isRtl) {
        btn.classList.add('rtl-active');
      } else {
        btn.classList.remove('rtl-active');
      }
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
