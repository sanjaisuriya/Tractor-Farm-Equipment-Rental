/**
 * Tractor & Farm Equipment Rental - Booking Engine
 * Live cost calculation, LocalStorage sync, and confirmation modal
 */

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('equipmentBookingForm');
  const equipSelect = document.getElementById('bookingEquipment');
  const categoryInput = document.getElementById('bookingCategory');
  const startDateInput = document.getElementById('bookingStartDate');
  const endDateInput = document.getElementById('bookingEndDate');
  const operatorCheckbox = document.getElementById('bookingOperator');
  const deliveryCheckbox = document.getElementById('bookingDelivery');
  const farmerNameInput = document.getElementById('bookingFarmerName');
  const mobileInput = document.getElementById('bookingMobile');
  const emailInput = document.getElementById('bookingEmail');
  const locationInput = document.getElementById('bookingLocation');
  const notesInput = document.getElementById('bookingNotes');

  // Summary elements
  const sumEquipName = document.getElementById('sumEquipName');
  const sumRatePerDay = document.getElementById('sumRatePerDay');
  const sumDuration = document.getElementById('sumDuration');
  const sumEquipCost = document.getElementById('sumEquipCost');
  const sumOperatorCost = document.getElementById('sumOperatorCost');
  const sumDeliveryCost = document.getElementById('sumDeliveryCost');
  const sumDeposit = document.getElementById('sumDeposit');
  const sumTotalAmount = document.getElementById('sumTotalAmount');

  // Pre-fill user details if logged in
  if (window.Auth && Auth.isLoggedIn()) {
    const user = Auth.getUser();
    if (farmerNameInput && !farmerNameInput.value) farmerNameInput.value = user.name || '';
    if (mobileInput && !mobileInput.value) mobileInput.value = user.mobile || '';
    if (emailInput && !emailInput.value) emailInput.value = user.email || '';
    if (locationInput && !locationInput.value) locationInput.value = user.village || '';
  }

  // Populate equipment dropdown
  if (equipSelect && window.EQUIPMENT_DATA) {
    equipSelect.innerHTML = `<option value="">-- Choose Farm Machinery --</option>` +
      EQUIPMENT_DATA.map(item => `
        <option value="${item.id}" data-category="${item.category}" data-rate="${item.dailyRate}" data-operator="${item.operatorRate}">
          ${item.name} (${item.hp}) - ₹${item.dailyRate}/day
        </option>
      `).join('');

    // Preselect from URL query params
    const params = new URLSearchParams(window.location.search);
    const equipParam = params.get('id');
    if (equipParam) {
      equipSelect.value = equipParam;
    } else {
      equipSelect.selectedIndex = 1; // Default to first equipment
    }
  }

  // Set default dates: Start today, End tomorrow
  const today = new Date();
  const tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 2); // 2 days default

  const formatDate = (d) => d.toISOString().split('T')[0];

  if (startDateInput && !startDateInput.value) {
    startDateInput.min = formatDate(today);
    startDateInput.value = formatDate(today);
  }
  if (endDateInput && !endDateInput.value) {
    endDateInput.min = formatDate(today);
    endDateInput.value = formatDate(tomorrow);
  }

  // Calculation function
  function calculateTotal() {
    const selectedOption = equipSelect.options[equipSelect.selectedIndex];
    if (!selectedOption || !selectedOption.value) return;

    const equip = EquipmentService.getById(selectedOption.value);
    if (categoryInput) categoryInput.value = equip.category;

    // Dates & Duration
    const sDate = new Date(startDateInput.value);
    const eDate = new Date(endDateInput.value);

    let days = 1;
    if (eDate >= sDate) {
      const diffTime = Math.abs(eDate - sDate);
      days = Math.max(1, Math.ceil(diffTime / (1000 * 60 * 60 * 24)));
    } else {
      endDateInput.value = startDateInput.value;
      days = 1;
    }

    const dailyRate = equip.dailyRate;
    const baseEquipCost = dailyRate * days;

    const hasOperator = operatorCheckbox ? operatorCheckbox.checked : false;
    const operatorDaily = equip.operatorRate || 700;
    const operatorCost = hasOperator ? operatorDaily * days : 0;

    const hasDelivery = deliveryCheckbox ? deliveryCheckbox.checked : false;
    const deliveryCost = hasDelivery ? (equip.transportRate * 15) : 0; // standard 15km delivery flat rate

    const refundableDeposit = Math.round(dailyRate * 0.4);
    const total = baseEquipCost + operatorCost + deliveryCost + refundableDeposit;

    // Update Summary UI
    if (sumEquipName) sumEquipName.textContent = equip.name;
    if (sumRatePerDay) sumRatePerDay.textContent = `₹${dailyRate.toLocaleString('en-IN')}`;
    if (sumDuration) sumDuration.textContent = `${days} Day${days > 1 ? 's' : ''}`;
    if (sumEquipCost) sumEquipCost.textContent = `₹${baseEquipCost.toLocaleString('en-IN')}`;
    if (sumOperatorCost) sumOperatorCost.textContent = `₹${operatorCost.toLocaleString('en-IN')}`;
    if (sumDeliveryCost) sumDeliveryCost.textContent = `₹${deliveryCost.toLocaleString('en-IN')}`;
    if (sumDeposit) sumDeposit.textContent = `₹${refundableDeposit.toLocaleString('en-IN')}`;
    if (sumTotalAmount) sumTotalAmount.textContent = `₹${total.toLocaleString('en-IN')}`;

    return {
      equip,
      days,
      baseEquipCost,
      operatorCost,
      deliveryCost,
      refundableDeposit,
      total
    };
  }

  // Event Listeners for live recalculation
  if (equipSelect) equipSelect.addEventListener('change', calculateTotal);
  if (startDateInput) startDateInput.addEventListener('change', calculateTotal);
  if (endDateInput) endDateInput.addEventListener('change', calculateTotal);
  if (operatorCheckbox) operatorCheckbox.addEventListener('change', calculateTotal);
  if (deliveryCheckbox) deliveryCheckbox.addEventListener('change', calculateTotal);

  // Initial Calculation
  calculateTotal();

  // Booking Form Submission
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const farmerName = farmerNameInput.value.trim();
      const mobile = mobileInput.value.trim();
      const email = emailInput.value.trim();
      const location = locationInput.value.trim();
      const notes = notesInput ? notesInput.value.trim() : '';

      if (!farmerName || !mobile || !location) {
        showBookingToast("Please fill in your Name, Mobile Number, and Farm Location.", "error");
        return;
      }

      const calc = calculateTotal();
      if (!calc) return;

      const bookingId = "TR-" + Math.floor(100000 + Math.random() * 900000);
      const newBooking = {
        id: bookingId,
        farmerName,
        mobile,
        email: email || "farmer@agrorent.in",
        equipmentId: calc.equip.id,
        equipmentName: calc.equip.name,
        equipmentCategory: calc.equip.category,
        equipmentImage: calc.equip.image,
        startDate: startDateInput.value,
        endDate: endDateInput.value,
        durationDays: calc.days,
        location,
        hasOperator: operatorCheckbox ? operatorCheckbox.checked : false,
        hasDelivery: deliveryCheckbox ? deliveryCheckbox.checked : false,
        notes,
        baseCost: calc.baseEquipCost,
        operatorCost: calc.operatorCost,
        deliveryCost: calc.deliveryCost,
        deposit: calc.refundableDeposit,
        totalAmount: calc.total,
        status: "Active", // "Active" so it immediately shows up in Active Rentals & My Bookings
        bookingDate: new Date().toISOString().split('T')[0],
        invoiceDate: new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
      };

      // Save into LocalStorage
      const existingBookings = JSON.parse(localStorage.getItem('trarent_bookings') || '[]');
      existingBookings.unshift(newBooking);
      localStorage.setItem('trarent_bookings', JSON.stringify(existingBookings));

      // Also mark logged in if not yet
      if (!localStorage.getItem('trarent_logged_in')) {
        localStorage.setItem('trarent_logged_in', 'true');
        localStorage.setItem('trarent_user', JSON.stringify({
          name: farmerName,
          email: email || "farmer@agrorent.in",
          mobile: mobile,
          village: location,
          farmSize: "10 Acres",
          memberSince: "November 2026",
          role: "Verified Farmer"
        }));
      }

      // Show Confirmation Modal
      showBookingSuccessModal(newBooking);
    });
  }
});

function showBookingSuccessModal(booking) {
  const modal = document.getElementById('bookingConfirmModal');
  if (!modal) return;

  const modalIdEl = document.getElementById('confirmBookingId');
  const modalEquipEl = document.getElementById('confirmEquipName');
  const modalDatesEl = document.getElementById('confirmDates');
  const modalTotalEl = document.getElementById('confirmTotal');
  const modalFarmerEl = document.getElementById('confirmFarmer');

  if (modalIdEl) modalIdEl.textContent = booking.id;
  if (modalEquipEl) modalEquipEl.textContent = booking.equipmentName;
  if (modalDatesEl) modalDatesEl.textContent = `${booking.startDate} to ${booking.endDate} (${booking.durationDays} Days)`;
  if (modalTotalEl) modalTotalEl.textContent = `₹${booking.totalAmount.toLocaleString('en-IN')}`;
  if (modalFarmerEl) modalFarmerEl.textContent = `${booking.farmerName} (${booking.location})`;

  // Save current booking id for invoice printing
  localStorage.setItem('trarent_last_booking_id', booking.id);

  modal.classList.add('active');
}

function showBookingToast(msg, type = "success") {
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
