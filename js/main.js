/**
 * Tractor & Farm Equipment Rental - Main Core Scripts
 * Global utilities, contact form validation, back-to-top, demo data seeding
 */

document.addEventListener('DOMContentLoaded', () => {
  // Back to Top Button
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.remove('opacity-0', 'invisible', 'translate-y-4');
        backToTopBtn.classList.add('opacity-100', 'visible', 'translate-y-0');
      } else {
        backToTopBtn.classList.add('opacity-0', 'invisible', 'translate-y-4');
        backToTopBtn.classList.remove('opacity-100', 'visible', 'translate-y-0');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Contact Form Handling (Page 10)
  const contactForm = document.getElementById('tractorContactForm');
  if (contactForm) {
    const contactNameInput = document.getElementById('contactName');
    const contactPhoneInput = document.getElementById('contactPhone');

    if (contactNameInput) {
      contactNameInput.addEventListener('input', (e) => {
        e.target.value = e.target.value.replace(/[^a-zA-Z\s]/g, '');
      });
      contactNameInput.addEventListener('keydown', (e) => {
        if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
        if (e.ctrlKey || e.metaKey) return;
        if (e.key === ' ') return;
        if (!/^[a-zA-Z]$/.test(e.key)) e.preventDefault();
      });
    }

    if (contactPhoneInput) {
      contactPhoneInput.addEventListener('input', (e) => {
        e.target.value = e.target.value.replace(/\D/g, '').slice(0, 10);
      });
      contactPhoneInput.addEventListener('keydown', (e) => {
        if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
        if (e.ctrlKey || e.metaKey) return;
        if (!/^[0-9]$/.test(e.key)) e.preventDefault();
        if (contactPhoneInput.value.length >= 10 && contactPhoneInput.selectionStart === contactPhoneInput.selectionEnd) {
          e.preventDefault();
        }
      });
    }

    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = contactNameInput?.value.trim();
      const phone = contactPhoneInput?.value.trim();
      const message = document.getElementById('contactMessage')?.value.trim();

      if (!name || !phone || !message) {
        showGlobalToast("Please provide your name, phone number, and rental query.", "error");
        return;
      }

      if (!/^[a-zA-Z\s]+$/.test(name)) {
        showGlobalToast("Name must contain letters and spaces only.", "error");
        contactNameInput?.focus();
        return;
      }

      if (!/^[0-9]{10}$/.test(phone)) {
        showGlobalToast("Please enter a valid 10-digit phone number.", "error");
        contactPhoneInput?.focus();
        return;
      }

      const successNotice = document.getElementById('contactSuccessNotice');
      if (successNotice) {
        successNotice.classList.remove('hidden');
        contactForm.reset();
        successNotice.scrollIntoView({ behavior: 'smooth' });
      } else {
        showGlobalToast("Thank you! Your tractor rental inquiry has been submitted. Our team will contact you shortly.", "success");
        contactForm.reset();
      }
    });
  }

  // Footer Newsletter Form
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      if (input && input.value.trim()) {
        showGlobalToast("Subscribed! You will receive agricultural machinery rental seasonal alerts.", "success");
        input.value = '';
      }
    });
  });
});

function showGlobalToast(msg, type = "success") {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <i class="fa-solid ${type === 'success' ? 'fa-circle-check text-green-400' : 'fa-triangle-exclamation text-red-400'}"></i>
    <span>${msg}</span>
  `;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}

window.showGlobalToast = showGlobalToast;
