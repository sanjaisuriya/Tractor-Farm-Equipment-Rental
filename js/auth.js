/**
 * Tractor & Farm Equipment Rental - Authentication Manager
 * Farmer Login, Demo Credentials, Registration, Password Visibility, and Session Management
 */

const DEFAULT_DEMO_USER = {
  name: "Guest",
  email: "guest@agrorent.in",
  mobile: "+91 98765 43210",
  village: "Rampur, Ludhiana, Punjab",
  farmSize: "12 Acres",
  primaryCrops: "Wheat, Paddy, Mustard",
  memberSince: "March 2024",
  role: "Verified Progressive Farmer"
};

const Auth = {
  isLoggedIn() {
    return localStorage.getItem('trarent_logged_in') === 'true';
  },

  getUser() {
    const stored = localStorage.getItem('trarent_user');
    if (stored) {
      try {
        return JSON.parse(stored);
      } catch (e) {
        return DEFAULT_DEMO_USER;
      }
    }
    return DEFAULT_DEMO_USER;
  },

  setUser(user) {
    localStorage.setItem('trarent_user', JSON.stringify(user));
  },

  login(email, password) {
    let user = this.getUser();
    if (!email || email.toLowerCase() === DEFAULT_DEMO_USER.email.toLowerCase()) {
      user = { ...DEFAULT_DEMO_USER };
    } else {
      let displayName = email.split('@')[0].replace(/[._]/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
      if (!displayName || displayName.trim() === '') displayName = "Farmer";
      user = {
        ...user,
        email: email,
        name: displayName
      };
    }

    this.setUser(user);
    localStorage.setItem('trarent_auth_origin', 'form');
    localStorage.setItem('trarent_logged_in', 'true');
    return { success: true, message: `Welcome back, ${user.name}! Redirecting to Farmer Dashboard...`, user };
  },

  loginAsGuest() {
    const guestUser = {
      name: "Guest",
      email: "guest@agrorent.in",
      mobile: "+91 98765 43210",
      village: "Coimbatore, Tamil Nadu",
      farmSize: "10 Acres",
      primaryCrops: "Paddy, Coconut, Sugarcane",
      memberSince: "November 2026",
      role: "Guest Farmer"
    };
    this.setUser(guestUser);
    localStorage.setItem('trarent_auth_origin', 'form');
    localStorage.setItem('trarent_logged_in', 'true');
    showAuthToast("Welcome, Guest! Opening Farmer Dashboard...", "success");
    setTimeout(() => {
      window.location.href = 'farmer-dashboard.html';
    }, 500);
  },

  register(userData) {
    if (!userData.name || !userData.mobile || !userData.email || !userData.password) {
      return { success: false, message: "Please fill in all required fields." };
    }
    if (userData.password !== userData.confirmPassword) {
      return { success: false, message: "Passwords do not match. Please re-enter." };
    }

    const newUser = {
      name: userData.name,
      email: userData.email,
      mobile: userData.mobile,
      village: userData.village || "Rampur, Punjab",
      farmSize: userData.farmSize || "10 Acres",
      primaryCrops: "Wheat, Paddy",
      memberSince: "November 2026",
      role: "Registered Farmer"
    };

    this.setUser(newUser);
    localStorage.setItem('trarent_auth_origin', 'form');
    localStorage.setItem('trarent_logged_in', 'true');
    return { success: true, message: `Account created successfully! Welcome, ${newUser.name}. Redirecting...`, user: newUser };
  },

  logout() {
    localStorage.removeItem('trarent_logged_in');
    localStorage.removeItem('trarent_auth_origin');
    localStorage.removeItem('trarent_user');
    showAuthToast("You have been safely logged out.", "success");
    setTimeout(() => {
      window.location.href = 'index.html';
    }, 500);
  },

  loginAsSocial(provider) {
    const user = {
      name: "Guest",
      email: `guest.${provider.toLowerCase().replace(/\s+/g, '')}@agrorent.in`,
      mobile: "+91 98765 43210",
      village: "Rampur, Punjab",
      farmSize: "12 Acres",
      primaryCrops: "Wheat, Paddy, Mustard",
      memberSince: "November 2026",
      role: `${provider} Connected Farmer`
    };
    this.setUser(user);
    localStorage.setItem('trarent_auth_origin', 'guest');
    localStorage.removeItem('trarent_logged_in');
    showAuthToast(`Authenticated via ${provider}! Redirecting to Dashboard...`, "success");
    setTimeout(() => {
      window.location.href = 'farmer-dashboard.html';
    }, 600);
  },

  protectDashboard() {
    // Farmer Dashboard runs as a live showcase preview.
    // It should NEVER force login, redirect to login, or automatically mark the user as logged in.
    if (localStorage.getItem('trarent_auth_origin') !== 'form') {
      localStorage.removeItem('trarent_logged_in');
    }
    return true;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  // 1. Password Visibility Toggle (Show / Hide)
  document.querySelectorAll('.password-toggle-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const container = btn.closest('.relative') || btn.parentElement;
      const input = container ? container.querySelector('input') : btn.previousElementSibling;
      if (input && (input.type === 'password' || input.type === 'text')) {
        const isPassword = input.type === 'password';
        input.type = isPassword ? 'text' : 'password';
        const icon = btn.querySelector('i');
        if (icon) {
          icon.className = isPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye';
        }
        if (btn.id === 'passwordShowToggleBtn') {
          btn.textContent = isPassword ? 'Hide' : 'Show';
        }
        btn.setAttribute('title', isPassword ? 'Hide password' : 'Show password');
        btn.setAttribute('aria-label', isPassword ? 'Hide password' : 'Show password');
      }
    });
  });

  // Continue as Guest Button (1-Click Instant Guest Access)
  const guestBtn = document.getElementById('continueAsGuestBtn');
  if (guestBtn) {
    guestBtn.addEventListener('click', (e) => {
      e.preventDefault();
      Auth.loginAsGuest();
    });
  }

  // 2. Tab Switches and Registration Links
  const tabLogin = document.getElementById('tabLogin');
  const tabRegister = document.getElementById('tabRegister');
  const loginSec = document.getElementById('loginSection');
  const registerSec = document.getElementById('registerSection');
  const linkToRegister = document.getElementById('linkToRegister');
  const linkToLogin = document.getElementById('linkToLogin');

  function switchToLogin() {
    if (tabLogin) tabLogin.classList.add('active');
    if (tabRegister) tabRegister.classList.remove('active');
    if (loginSec) loginSec.classList.remove('hidden');
    if (registerSec) registerSec.classList.add('hidden');
  }

  function switchToRegister() {
    if (tabRegister) tabRegister.classList.add('active');
    if (tabLogin) tabLogin.classList.remove('active');
    if (registerSec) registerSec.classList.remove('hidden');
    if (loginSec) loginSec.classList.add('hidden');
  }

  if (tabLogin && tabRegister) {
    tabLogin.addEventListener('click', switchToLogin);
    tabRegister.addEventListener('click', switchToRegister);
  }
  if (linkToRegister) linkToRegister.addEventListener('click', (e) => { e.preventDefault(); switchToRegister(); });
  if (linkToLogin) linkToLogin.addEventListener('click', (e) => { e.preventDefault(); switchToLogin(); });

  // 3. Quick 1-Click Demo Login Button
  const demoLoginBtn = document.getElementById('quickDemoLoginBtn');
  if (demoLoginBtn) {
    demoLoginBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('loginEmail');
      const passInput = document.getElementById('loginPassword');
      if (emailInput) emailInput.value = DEFAULT_DEMO_USER.email;
      if (passInput) passInput.value = "farmer123";

      Auth.setUser(DEFAULT_DEMO_USER);
      localStorage.setItem('trarent_auth_origin', 'form');
      localStorage.setItem('trarent_logged_in', 'true');
      showAuthToast("Signed in as Rajesh Kumar (Demo Farmer)! Opening Dashboard...", "success");
      setTimeout(() => {
        window.location.href = 'farmer-dashboard.html';
      }, 700);
    });
  }

  // 4. Fill Demo Credentials Helper Button
  const fillDemoCredsBtn = document.getElementById('fillDemoCredsBtn');
  if (fillDemoCredsBtn) {
    fillDemoCredsBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('loginEmail');
      const passInput = document.getElementById('loginPassword');
      if (emailInput) emailInput.value = DEFAULT_DEMO_USER.email;
      if (passInput) passInput.value = "farmer123";
      showAuthToast("Demo credentials loaded into form!", "success");
    });
  }

  // 5. Forgot Password Dialog Trigger
  const forgotPasswordLink = document.getElementById('forgotPasswordLink');
  if (forgotPasswordLink) {
    forgotPasswordLink.addEventListener('click', (e) => {
      e.preventDefault();
      const modal = document.getElementById('forgotPasswordModal');
      if (modal) {
        modal.classList.add('active');
      } else {
        alert("Demo Recovery:\n\nEmail: farmer@agrorent.in\nPassword: farmer123\n\nUse these credentials or click 'Instant 1-Click Demo Login'.");
      }
    });
  }

  const closeForgotModal = document.getElementById('closeForgotModal');
  if (closeForgotModal) {
    closeForgotModal.addEventListener('click', () => {
      document.getElementById('forgotPasswordModal')?.classList.remove('active');
    });
  }

  // Social Login: Google and Apple Buttons
  const googleBtn = document.getElementById('googleSignInBtn');
  if (googleBtn) {
    googleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      Auth.loginAsSocial('Google');
    });
  }

  const appleBtn = document.getElementById('appleSignInBtn');
  if (appleBtn) {
    appleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      Auth.loginAsSocial('Apple ID');
    });
  }

  // Create Farmer Account Modal Triggers
  const createAccBtn = document.getElementById('createAccountBtn');
  const regModal = document.getElementById('registerModal');
  const closeRegModal = document.getElementById('closeRegisterModal');

  if (createAccBtn && regModal) {
    createAccBtn.addEventListener('click', (e) => {
      e.preventDefault();
      regModal.classList.add('active');
    });
  }

  if (closeRegModal && regModal) {
    closeRegModal.addEventListener('click', () => {
      regModal.classList.remove('active');
    });
  }

  const createAccForm = document.getElementById('createAccountForm');
  if (createAccForm) {
    createAccForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regFarmerName')?.value.trim() || 'Guest';
      const contact = document.getElementById('regFarmerContact')?.value.trim() || '';
      const user = {
        name: name,
        email: contact.includes('@') ? contact : `${contact}@farmer.agrorent.in`,
        mobile: contact.includes('@') ? '+91 98765 43210' : contact,
        village: 'Rampur, Punjab',
        farmSize: '12 Acres',
        primaryCrops: 'Wheat, Paddy',
        memberSince: 'November 2026',
        role: 'Registered Farmer'
      };
      Auth.setUser(user);
      localStorage.setItem('trarent_auth_origin', 'form');
      localStorage.setItem('trarent_logged_in', 'true');
      showAuthToast(`Account created! Welcome, ${name}. Loading Dashboard...`, 'success');
      regModal?.classList.remove('active');
      setTimeout(() => {
        window.location.href = 'farmer-dashboard.html';
      }, 700);
    });
  }

  // 6. Login Form Submission
  const loginForm = document.getElementById('farmerLoginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail')?.value.trim();
      const password = document.getElementById('loginPassword')?.value;

      const submitBtn = loginForm.querySelector('button[type="submit"]');
      const originalHtml = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin mr-2"></i> Verifying...';
      }

      setTimeout(() => {
        const res = Auth.login(email, password);
        if (res.success) {
          showAuthToast(res.message, "success");
          setTimeout(() => {
            window.location.href = 'farmer-dashboard.html';
          }, 600);
        } else {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalHtml;
          }
          showAuthToast(res.message, "error");
        }
      }, 400);
    });
  }

  // Real-time input validation for Name (letters only) & Mobile (digits only, max 10)
  const regNameEl = document.getElementById('regName');
  const regMobileEl = document.getElementById('regMobile');

  if (regNameEl) {
    regNameEl.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/[^a-zA-Z\s]/g, '');
    });
    regNameEl.addEventListener('keydown', (e) => {
      if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      if (e.ctrlKey || e.metaKey) return;
      if (e.key === ' ') return;
      if (!/^[a-zA-Z]$/.test(e.key)) {
        e.preventDefault();
      }
    });
  }

  if (regMobileEl) {
    regMobileEl.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/\D/g, '').slice(0, 10);
    });
    regMobileEl.addEventListener('keydown', (e) => {
      if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      if (e.ctrlKey || e.metaKey) return;
      if (!/^[0-9]$/.test(e.key)) {
        e.preventDefault();
      }
      if (regMobileEl.value.length >= 10 && regMobileEl.selectionStart === regMobileEl.selectionEnd) {
        e.preventDefault();
      }
    });
  }

  // 7. Register Form Submission
  const registerForm = document.getElementById('farmerRegisterForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regName')?.value.trim();
      const mobile = document.getElementById('regMobile')?.value.trim();
      const email = document.getElementById('regEmail')?.value.trim();
      const village = document.getElementById('regVillage')?.value.trim();
      const farmSize = document.getElementById('regFarmSize')?.value.trim();
      const password = document.getElementById('regPassword')?.value;
      const confirmPassword = document.getElementById('regConfirmPassword')?.value;

      const res = Auth.register({ name, mobile, email, village, farmSize, password, confirmPassword });
      if (res.success) {
        showAuthToast(res.message, "success");
        setTimeout(() => {
          window.location.href = 'farmer-dashboard.html';
        }, 700);
      } else {
        showAuthToast(res.message, "error");
      }
    });
  }
});

function showAuthToast(msg, type = "success") {
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

window.Auth = Auth;
window.showAuthToast = showAuthToast;
