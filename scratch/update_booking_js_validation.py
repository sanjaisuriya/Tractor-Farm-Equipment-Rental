with open('js/booking.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Insert input event listeners after line 37 (Auth prefill)
target1 = """  if (window.Auth && Auth.isLoggedIn()) {
    const user = Auth.getUser();
    if (farmerNameInput && !farmerNameInput.value) farmerNameInput.value = user.name || '';
    if (mobileInput && !mobileInput.value) mobileInput.value = user.mobile || '';
    if (emailInput && !emailInput.value) emailInput.value = user.email || '';
    if (locationInput && !locationInput.value) locationInput.value = user.village || '';
  }"""

replacement1 = """  if (window.Auth && Auth.isLoggedIn()) {
    const user = Auth.getUser();
    if (farmerNameInput && !farmerNameInput.value) farmerNameInput.value = user.name || '';
    if (mobileInput && !mobileInput.value) mobileInput.value = user.mobile || '';
    if (emailInput && !emailInput.value) emailInput.value = user.email || '';
    if (locationInput && !locationInput.value) locationInput.value = user.village || '';
  }

  // Strict Validation: Name (Letters only) & Mobile (Numbers only, 10 digits)
  if (farmerNameInput) {
    farmerNameInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/[^a-zA-Z\s]/g, '');
    });
    farmerNameInput.addEventListener('keydown', (e) => {
      if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      if (e.ctrlKey || e.metaKey) return;
      if (e.key === ' ') return;
      if (!/^[a-zA-Z]$/.test(e.key)) {
        e.preventDefault();
      }
    });
  }

  if (mobileInput) {
    mobileInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/\D/g, '').slice(0, 10);
    });
    mobileInput.addEventListener('keydown', (e) => {
      if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      if (e.ctrlKey || e.metaKey) return;
      if (!/^[0-9]$/.test(e.key)) {
        e.preventDefault();
      }
      if (mobileInput.value.length >= 10 && mobileInput.selectionStart === mobileInput.selectionEnd) {
        e.preventDefault();
      }
    });
  }"""

if target1 in js:
    js = js.replace(target1, replacement1, 1)
    print("Added input event listeners to js/booking.js successfully!")
else:
    print("Could not find target1 in js/booking.js!")

# 2. Add regex validation to form submit handler in js/booking.js
target2 = """      if (!farmerName || !mobile || !location) {
        showBookingToast("Please fill in your Name, Mobile Number, and Farm Location.", "error");
        return;
      }"""

replacement2 = """      if (!farmerName || !mobile || !location) {
        showBookingToast("Please fill in your Name, Mobile Number, and Farm Location.", "error");
        return;
      }

      if (!/^[a-zA-Z\s]+$/.test(farmerName)) {
        showBookingToast("Farmer Full Name must contain letters and spaces only.", "error");
        farmerNameInput.focus();
        return;
      }

      if (!/^[0-9]{10}$/.test(mobile)) {
        showBookingToast("Please enter a valid 10-digit mobile number.", "error");
        mobileInput.focus();
        return;
      }"""

if target2 in js:
    js = js.replace(target2, replacement2, 1)
    print("Added submit validation checks to js/booking.js successfully!")
else:
    print("Could not find target2 in js/booking.js!")

with open('js/booking.js', 'w', encoding='utf-8') as f:
    f.write(js)
