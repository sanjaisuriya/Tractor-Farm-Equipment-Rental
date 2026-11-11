/**
 * Tractor & Farm Equipment Rental - Navigation Handler
 * Responsive menu, sticky navbar, active link detection, auth status badge
 */

document.addEventListener('DOMContentLoaded', () => {
  // Sticky Navbar blur and shadow on scroll
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 30) {
        header.classList.add('shadow-md', 'bg-white/95', 'dark:bg-[#121813]/95', 'backdrop-blur-md');
      } else {
        header.classList.remove('shadow-md', 'bg-white/95', 'dark:bg-[#121813]/95', 'backdrop-blur-md');
      }
    });
  }

  // Mobile Menu Drawer Toggling
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const mobileNavBackdrop = document.getElementById('mobileNavBackdrop');
  const closeMobileMenu = document.getElementById('closeMobileMenu');

  function openDrawer() {
    if (mobileNavDrawer && mobileNavBackdrop) {
      mobileNavDrawer.classList.add('open');
      mobileNavBackdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeDrawer() {
    if (mobileNavDrawer && mobileNavBackdrop) {
      mobileNavDrawer.classList.remove('open');
      mobileNavBackdrop.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', openDrawer);
  }

  if (closeMobileMenu) {
    closeMobileMenu.addEventListener('click', closeDrawer);
  }

  if (mobileNavBackdrop) {
    mobileNavBackdrop.addEventListener('click', closeDrawer);
  }

  // Active Link Detection & Underline Highlight
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.site-header nav .nav-link, .mobile-nav-drawer nav a');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    let isMatch = false;

    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      isMatch = true;
    } else if ((currentPath === 'index.html' || currentPath === 'home-2.html' || currentPath === '') && link.closest('.dropdown-container')) {
      isMatch = true;
    } else if ((currentPath === 'equipment-details.html') && href === 'equipment.html') {
      isMatch = true;
    }

    if (isMatch) {
      link.classList.add('active', 'active-page', 'text-agri', 'font-bold');
      link.setAttribute('aria-current', 'page');
    }
  });

  // Mobile Home Submenu Toggle
  const mobileHomeToggle = document.getElementById('mobileHomeToggle');
  const mobileHomeSubmenu = document.getElementById('mobileHomeSubmenu');
  if (mobileHomeToggle && mobileHomeSubmenu) {
    mobileHomeToggle.addEventListener('click', (e) => {
      e.preventDefault();
      mobileHomeSubmenu.classList.toggle('hidden');
      const arrow = mobileHomeToggle.querySelector('.arrow-icon');
      if (arrow) arrow.classList.toggle('rotate-180');
    });
  }

  // Update Auth Link in Header
  updateNavAuthStatus();
});

function updateNavAuthStatus() {
  let loggedIn = false;
  let user = {};
  try {
    loggedIn = localStorage.getItem('trarent_logged_in') === 'true';
    user = JSON.parse(localStorage.getItem('trarent_user') || '{}');
  } catch (e) {
    // Graceful fallback
  }

  const authNavContainers = document.querySelectorAll('.nav-auth-item');
  authNavContainers.forEach(container => {
    if (loggedIn && user && user.name) {
      container.innerHTML = `
        <a href="farmer-dashboard.html" class="btn-secondary text-xs xl:text-sm py-2 px-3 xl:px-4 whitespace-nowrap flex items-center gap-1.5 font-semibold" title="Logged in as ${user.name}">
          <i class="fa-solid fa-circle-user text-xs text-agri"></i>
          <span>${user.name.split(' ')[0]}</span>
        </a>
      `;
    } else {
      container.innerHTML = `
        <a href="login-register.html" class="btn-secondary text-xs xl:text-sm py-2 px-3 xl:px-4 whitespace-nowrap flex items-center gap-1.5 font-semibold" title="Login / Register">
          <i class="fa-solid fa-arrow-right-to-bracket text-xs text-agri"></i>
          <span>Login</span>
        </a>
      `;
    }
  });

  const mobileAuthContainers = document.querySelectorAll('.mobile-nav-auth-item');
  mobileAuthContainers.forEach(container => {
    if (loggedIn && user && user.name) {
      container.innerHTML = `
        <a href="farmer-dashboard.html" class="btn-secondary w-full py-2.5 justify-center text-sm font-semibold flex items-center gap-2">
          <i class="fa-solid fa-circle-user text-agri"></i>
          <span>${user.name.split(' ')[0]} (Dashboard)</span>
        </a>
      `;
    } else {
      container.innerHTML = `
        <a href="login-register.html" class="btn-secondary w-full py-2.5 justify-center text-sm font-semibold flex items-center gap-2">
          <i class="fa-solid fa-arrow-right-to-bracket text-agri"></i>
          <span>Login</span>
        </a>
      `;
    }
  });
}
