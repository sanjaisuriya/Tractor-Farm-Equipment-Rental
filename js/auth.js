/**
 * Tractor & Farm Equipment Rental - Authentication Manager
 * Demo Login, Registration, Password Toggle & Dashboard Protection
 */

const DEFAULT_DEMO_USER = {
  name: "Rajesh Kumar",
  email: "farmer@agrorent.in",
  mobile: "+91 98765 43210",
  village: "Rampur, Ludhiana, Punjab",
  farmSize: "12 Acres",
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

  login(identifier, password) {
    if (!identifier || !password) {
      return { success: false, message: "Please fill in all required fields." };
    }

    let user = this.getUser();
    localStorage.setItem('trarent_logged_in', 'true');
    return { success: true, message: "Login successful! Redirecting to Dashboard...", user };
  },

  register(userData) {
    if (!userData.name || !userData.mobile || !userData.password) {
      return { success: false, message: "Please fill in all required fields." };
    }
    if (userData.password !== userData.confirmPassword) {
      return { success: false, message: "Passwords do not match." };
    }

    const newUser = {
      name: userData.name,
      email: userData.email || "farmer@agrorent.in",
      mobile: userData.mobile,
      village: userData.village || "Kisan Nagar",
      farmSize: "8 Acres",
      memberSince: "November 2026",
      role: "Registered Farmer"
    };

    this.setUser(newUser);
    localStorage.setItem('trarent_logged_in', 'true');
    return { success: true, message: "Account created successfully! Redirecting to Dashboard...", user: newUser };
  },

  logout() {
    localStorage.removeItem('trarent_logged_in');
    window.location.href = 'login-register.html';
  },

  protectDashboard() {
    if (!this.isLoggedIn()) {
      // In demo mode, if unauthenticated, show a quick prompt or banner
      const notice = document.getElementById('authNoticeModal');
      if (notice) {
        notice.classList.add('active');
      } else {
        window.location.href = 'login-register.html?redirect=farmer-dashboard.html';
      }
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  // Password Visibility Toggle
  document.querySelectorAll('.password-toggle-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const input = btn.previousElementSibling;
      if (input && (input.type === 'password' || input.type === 'text')) {
        const isPassword = input.type === 'password';
        input.type = isPassword ? 'text' : 'password';
        const icon = btn.querySelector('i');
        if (icon) {
          icon.className = isPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye';
        }
      }
    });
  });

  // Handle Login & Register page tab switches and submissions if present
  const loginForm = document.getElementById('farmerLoginForm');
  const registerForm = document.getElementById('farmerRegisterForm');
  const tabLogin = document.getElementById('tabLogin');
  const tabRegister = document.getElementById('tabRegister');
  const loginSec = document.getElementById('loginSection');
  const registerSec = document.getElementById('registerSection');

  if (tabLogin && tabRegister) {
    tabLogin.addEventListener('click', () => {
      tabLogin.classList.add('active');
      tabRegister.classList.remove('active');
      loginSec.classList.remove('hidden');
      registerSec.classList.add('hidden');
    });

    tabRegister.addEventListener('click', () => {
      tabRegister.classList.add('active');
      tabLogin.classList.remove('active');
      registerSec.classList.remove('hidden');
      loginSec.classList.add('hidden');
    });
  }

  // Quick Demo Login Button
  const demoLoginBtn = document.getElementById('quickDemoLoginBtn');
  if (demoLoginBtn) {
    demoLoginBtn.addEventListener('click', (e) => {
      e.preventDefault();
      Auth.setUser(DEFAULT_DEMO_USER);
      localStorage.setItem('trarent_logged_in', 'true');
      showAuthToast("Welcome, Rajesh Kumar! Logged in as Demo Farmer.", "success");
      setTimeout(() => {
        window.location.href = 'farmer-dashboard.html';
      }, 700);
    });
  }

  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const identifier = document.getElementById('loginIdentifier')?.value.trim();
      const password = document.getElementById('loginPassword')?.value;

      const res = Auth.login(identifier, password);
      if (res.success) {
        showAuthToast(res.message, "success");
        setTimeout(() => {
          const params = new URLSearchParams(window.location.search);
          const redirect = params.get('redirect') || 'farmer-dashboard.html';
          window.location.href = redirect;
        }, 800);
      } else {
        showAuthToast(res.message, "error");
      }
    });
  }

  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regName')?.value.trim();
      const mobile = document.getElementById('regMobile')?.value.trim();
      const email = document.getElementById('regEmail')?.value.trim();
      const village = document.getElementById('regVillage')?.value.trim();
      const password = document.getElementById('regPassword')?.value;
      const confirmPassword = document.getElementById('regConfirmPassword')?.value;

      const res = Auth.register({ name, mobile, email, village, password, confirmPassword });
      if (res.success) {
        showAuthToast(res.message, "success");
        setTimeout(() => {
          window.location.href = 'farmer-dashboard.html';
        }, 800);
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
