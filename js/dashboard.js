/**
 * Tractor & Farm Equipment Rental - Farmer Dashboard Engine
 * Handles sidebar tabs, metrics, live booking cards, active rentals, bills, invoices
 */

const SEED_BOOKINGS = [
  {
    id: "TR-849201",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "tr-575",
    equipmentName: "Mahindra 575 DI High-Power Tractor",
    equipmentCategory: "Tractors",
    equipmentImage: "assets/images/equipment/tractor.jpg",
    startDate: "2026-11-05",
    endDate: "2026-11-09",
    durationDays: 4,
    location: "Rampur Farm Sector 4, Ludhiana",
    hasOperator: true,
    hasDelivery: true,
    notes: "Deep field ploughing and bed preparation",
    baseCost: 14000,
    operatorCost: 2800,
    deliveryCost: 450,
    deposit: 1400,
    totalAmount: 18650,
    status: "Active",
    bookingDate: "2026-11-04",
    invoiceDate: "04 Nov 2026"
  },
  {
    id: "TR-721495",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "rot-48",
    equipmentName: "Shaktiman Semi-Champion 6 Feet Rotavator",
    equipmentCategory: "Rotavators",
    equipmentImage: "assets/images/equipment/rotavator.jpg",
    startDate: "2026-11-12",
    endDate: "2026-11-14",
    durationDays: 2,
    location: "Rampur Farm Sector 4, Ludhiana",
    hasOperator: false,
    hasDelivery: true,
    notes: "Fine seedbed preparation for wheat sowing",
    baseCost: 3200,
    operatorCost: 0,
    deliveryCost: 300,
    deposit: 640,
    totalAmount: 4140,
    status: "Upcoming",
    bookingDate: "2026-11-02",
    invoiceDate: "02 Nov 2026"
  },
  {
    id: "TR-603184",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "harv-9000",
    equipmentName: "Preet 987 Self-Propelled Combine Harvester",
    equipmentCategory: "Combine Harvesters",
    equipmentImage: "assets/images/equipment/harvester.jpg",
    startDate: "2026-10-18",
    endDate: "2026-10-21",
    durationDays: 3,
    location: "Rampur Farm Sector 2, Ludhiana",
    hasOperator: true,
    hasDelivery: true,
    notes: "Paddy crop harvesting",
    baseCost: 43500,
    operatorCost: 3600,
    deliveryCost: 900,
    deposit: 5000,
    totalAmount: 53000,
    status: "Completed",
    bookingDate: "2026-10-15",
    invoiceDate: "15 Oct 2026"
  }
];

document.addEventListener('DOMContentLoaded', () => {
  // Ensure seed data exists
  if (!localStorage.getItem('trarent_bookings')) {
    localStorage.setItem('trarent_bookings', JSON.stringify(SEED_BOOKINGS));
  }

  // Load User Profile Data
  loadUserProfile();

  // Tab Switching
  setupDashboardTabs();

  // Load Metrics & Tables
  renderDashboardData();

  // Mobile Sidebar Toggle
  const sidebarToggle = document.getElementById('dashboardSidebarToggle');
  const sidebar = document.getElementById('dashboardSidebar');
  const sidebarClose = document.getElementById('dashboardSidebarClose');

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('active');
    });
  }
  if (sidebarClose && sidebar) {
    sidebarClose.addEventListener('click', () => {
      sidebar.classList.remove('active');
    });
  }

  // Profile Form Save
  const profileForm = document.getElementById('farmerProfileForm');
  if (profileForm) {
    profileForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const updatedUser = {
        name: document.getElementById('profName').value.trim(),
        email: document.getElementById('profEmail').value.trim(),
        mobile: document.getElementById('profMobile').value.trim(),
        village: document.getElementById('profVillage').value.trim(),
        farmSize: document.getElementById('profFarmSize').value.trim(),
        memberSince: "March 2024",
        role: "Verified Progressive Farmer"
      };
      Auth.setUser(updatedUser);
      loadUserProfile();
      showDashboardToast("Profile updated successfully!", "success");
    });
  }
});

function loadUserProfile() {
  const user = Auth.getUser();
  const nameEls = document.querySelectorAll('.user-name-display');
  const emailEls = document.querySelectorAll('.user-email-display');
  const villageEls = document.querySelectorAll('.user-village-display');

  nameEls.forEach(el => el.textContent = user.name || "Rajesh Kumar");
  emailEls.forEach(el => el.textContent = user.email || "farmer@agrorent.in");
  villageEls.forEach(el => el.textContent = user.village || "Rampur, Punjab");

  const profName = document.getElementById('profName');
  const profEmail = document.getElementById('profEmail');
  const profMobile = document.getElementById('profMobile');
  const profVillage = document.getElementById('profVillage');
  const profFarmSize = document.getElementById('profFarmSize');

  if (profName) profName.value = user.name || "Rajesh Kumar";
  if (profEmail) profEmail.value = user.email || "farmer@agrorent.in";
  if (profMobile) profMobile.value = user.mobile || "+91 98765 43210";
  if (profVillage) profVillage.value = user.village || "Rampur, Ludhiana, Punjab";
  if (profFarmSize) profFarmSize.value = user.farmSize || "12 Acres";
}

function setupDashboardTabs() {
  const tabLinks = document.querySelectorAll('.sidebar-link[data-tab]');
  const tabPanels = document.querySelectorAll('.tab-content-panel');

  tabLinks.forEach(link => {
    link.addEventListener('click', () => {
      const tabId = link.getAttribute('data-tab');

      if (tabId === 'logout') {
        Auth.logout();
        return;
      }

      tabLinks.forEach(l => l.classList.remove('active'));
      link.classList.add('active');

      tabPanels.forEach(panel => {
        panel.classList.remove('active');
        if (panel.id === `tab-${tabId}`) {
          panel.classList.add('active');
        }
      });

      // Close mobile sidebar if open
      const sidebar = document.getElementById('dashboardSidebar');
      if (sidebar && window.innerWidth < 1024) {
        sidebar.classList.remove('active');
      }
    });
  });
}

function renderDashboardData() {
  const bookings = JSON.parse(localStorage.getItem('trarent_bookings') || '[]');

  // Metrics
  const totalCount = bookings.length;
  const activeCount = bookings.filter(b => b.status === 'Active').length;
  const upcomingCount = bookings.filter(b => b.status === 'Upcoming').length;
  const completedCount = bookings.filter(b => b.status === 'Completed').length;
  const totalExpenses = bookings.reduce((sum, b) => sum + (b.totalAmount || 0), 0);

  const totalEl = document.getElementById('metricTotalBookings');
  const activeEl = document.getElementById('metricActiveRentals');
  const upcomingEl = document.getElementById('metricUpcomingBookings');
  const completedEl = document.getElementById('metricCompletedRentals');
  const expensesEl = document.getElementById('metricTotalExpenses');

  if (totalEl) totalEl.textContent = totalCount;
  if (activeEl) activeEl.textContent = activeCount;
  if (upcomingEl) upcomingEl.textContent = upcomingCount;
  if (completedEl) completedEl.textContent = completedCount;
  if (expensesEl) expensesEl.textContent = `₹${totalExpenses.toLocaleString('en-IN')}`;

  // Overview Recent Bookings
  const overviewList = document.getElementById('overviewBookingsList');
  if (overviewList) {
    if (bookings.length === 0) {
      overviewList.innerHTML = `<p class="text-sm text-muted p-4">No bookings found. <a href="booking.html" class="text-agri font-bold underline">Book equipment now</a>.</p>`;
    } else {
      overviewList.innerHTML = bookings.slice(0, 3).map(b => `
        <div class="flex items-center justify-between p-4 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-agri transition">
          <div class="flex items-center gap-4">
            <img src="${b.equipmentImage}" alt="${b.equipmentName}" class="w-14 h-14 rounded-lg object-cover" />
            <div>
              <div class="flex items-center gap-2">
                <span class="text-xs font-bold text-slate-500">${b.id}</span>
                <span class="px-2 py-0.5 text-xs font-semibold rounded-full ${getStatusBadgeClass(b.status)}">${b.status}</span>
              </div>
              <h4 class="font-bold text-slate-800 dark:text-white">${b.equipmentName}</h4>
              <p class="text-xs text-muted"><i class="fa-solid fa-calendar mr-1"></i>${b.startDate} to ${b.endDate} (${b.durationDays} Days)</p>
            </div>
          </div>
          <div class="text-right">
            <span class="font-black text-agri dark:text-fresh text-lg">₹${b.totalAmount.toLocaleString('en-IN')}</span>
            <div class="mt-1">
              <button onclick="InvoiceManager.renderModal('${b.id}')" class="text-xs text-slate-600 dark:text-slate-300 hover:text-agri font-semibold flex items-center gap-1 justify-end">
                <i class="fa-solid fa-receipt"></i> Invoice
              </button>
            </div>
          </div>
        </div>
      `).join('');
    }
  }

  // Full "My Bookings" Table
  const bookingsTableBody = document.getElementById('myBookingsTableBody');
  if (bookingsTableBody) {
    bookingsTableBody.innerHTML = bookings.map(b => `
      <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
        <td class="p-4 font-bold text-xs text-slate-600 dark:text-slate-300">${b.id}</td>
        <td class="p-4">
          <div class="flex items-center gap-3">
            <img src="${b.equipmentImage}" alt="${b.equipmentName}" class="w-12 h-12 rounded-lg object-cover flex-shrink-0" />
            <div>
              <p class="font-bold text-sm text-slate-900 dark:text-white">${b.equipmentName}</p>
              <span class="text-xs text-slate-500">${b.equipmentCategory}</span>
            </div>
          </div>
        </td>
        <td class="p-4 text-xs text-slate-600 dark:text-slate-300">${b.bookingDate}</td>
        <td class="p-4 text-xs font-medium text-slate-800 dark:text-slate-200">${b.startDate}</td>
        <td class="p-4 text-xs font-medium text-slate-800 dark:text-slate-200">${b.endDate}</td>
        <td class="p-4">
          <span class="px-2.5 py-1 text-xs font-semibold rounded-full ${getStatusBadgeClass(b.status)}">
            ${b.status}
          </span>
        </td>
        <td class="p-4 text-right">
          <button onclick="InvoiceManager.renderModal('${b.id}')" class="btn-secondary text-xs py-1.5 px-3">
            <i class="fa-solid fa-file-invoice"></i> Bill
          </button>
        </td>
      </tr>
    `).join('');
  }

  // Active Rentals Section
  const activeRentalsContainer = document.getElementById('activeRentalsContainer');
  if (activeRentalsContainer) {
    const activeItems = bookings.filter(b => b.status === 'Active');
    if (activeItems.length === 0) {
      activeRentalsContainer.innerHTML = `
        <div class="p-8 text-center bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
          <i class="fa-solid fa-tractor text-4xl text-slate-400 mb-3"></i>
          <h4 class="font-bold text-slate-700 dark:text-slate-200">No active equipment rentals right now</h4>
          <p class="text-xs text-muted mb-4">Book farm machinery for your current field needs.</p>
          <a href="equipment.html" class="btn-primary text-xs py-2 px-4">Browse Machinery</a>
        </div>
      `;
    } else {
      activeRentalsContainer.innerHTML = activeItems.map(item => `
        <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-6 flex flex-col md:flex-row gap-6 items-center">
          <img src="${item.equipmentImage}" alt="${item.equipmentName}" class="w-full md:w-56 h-40 rounded-lg object-cover flex-shrink-0" />
          <div class="flex-1">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge-agri badge-available"><i class="fa-solid fa-check"></i> Field Active</span>
              <span class="text-xs text-muted">ID: ${item.id}</span>
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">${item.equipmentName}</h3>
            <p class="text-xs text-slate-600 dark:text-slate-300 mb-4">Location: <strong>${item.location}</strong></p>

            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-xs mb-4">
              <div>
                <span class="text-muted block">Rental Duration</span>
                <strong class="text-slate-800 dark:text-slate-200">${item.durationDays} Days</strong>
              </div>
              <div>
                <span class="text-muted block">Expected Return</span>
                <strong class="text-forest font-bold">${item.endDate}</strong>
              </div>
              <div>
                <span class="text-muted block">Operator Included?</span>
                <strong class="text-slate-800 dark:text-slate-200">${item.hasOperator ? 'Yes (Certified)' : 'Self-Operated'}</strong>
              </div>
            </div>

            <div class="flex flex-wrap gap-2">
              <button onclick="extendRental('${item.id}')" class="btn-secondary text-xs py-2 px-3">
                <i class="fa-solid fa-clock-rotate-left mr-1"></i> Extend Rental
              </button>
              <button onclick="requestAssistance('${item.id}')" class="btn-secondary text-xs py-2 px-3 border-amber-300 text-amber-700 dark:text-amber-400">
                <i class="fa-solid fa-wrench mr-1"></i> Field Assistance
              </button>
              <button onclick="InvoiceManager.renderModal('${item.id}')" class="btn-primary text-xs py-2 px-3">
                <i class="fa-solid fa-receipt mr-1"></i> View Receipt
              </button>
            </div>
          </div>
        </div>
      `).join('');
    }
  }

  // Booking History Tab
  const historyContainer = document.getElementById('bookingHistoryContainer');
  if (historyContainer) {
    const pastItems = bookings.filter(b => b.status === 'Completed');
    if (pastItems.length === 0) {
      historyContainer.innerHTML = `<p class="p-6 text-muted text-sm">No completed rental history yet.</p>`;
    } else {
      historyContainer.innerHTML = pastItems.map(item => `
        <div class="p-5 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <div class="flex items-center gap-4">
            <img src="${item.equipmentImage}" alt="${item.equipmentName}" class="w-16 h-16 rounded-lg object-cover" />
            <div>
              <span class="text-xs font-bold text-slate-400">${item.id}</span>
              <h4 class="font-bold text-slate-800 dark:text-white">${item.equipmentName}</h4>
              <p class="text-xs text-muted">Used: ${item.startDate} to ${item.endDate} (${item.durationDays} Days)</p>
            </div>
          </div>
          <div class="text-right">
            <span class="font-black text-slate-700 dark:text-slate-300 block mb-2">₹${item.totalAmount.toLocaleString('en-IN')}</span>
            <button onclick="InvoiceManager.renderModal('${item.id}')" class="btn-secondary text-xs py-1 px-3">Invoice</button>
          </div>
        </div>
      `).join('');
    }
  }

  // Bills & Payments Tab
  const billsContainer = document.getElementById('billsContainer');
  if (billsContainer) {
    billsContainer.innerHTML = bookings.map(b => `
      <div class="p-6 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="font-bold text-sm text-forest">Invoice #INV-${b.id}</span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-full bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-300">PAID</span>
          </div>
          <h4 class="font-bold text-base text-slate-800 dark:text-white mb-1">${b.equipmentName}</h4>
          <p class="text-xs text-muted">Rental charges: ₹${b.baseCost.toLocaleString('en-IN')} | Operator: ₹${b.operatorCost.toLocaleString('en-IN')} | Delivery: ₹${b.deliveryCost.toLocaleString('en-IN')}</p>
        </div>
        <div class="text-right flex items-center gap-4">
          <div>
            <span class="text-xs text-muted block">Total Paid</span>
            <strong class="text-xl font-black text-agri dark:text-fresh">₹${b.totalAmount.toLocaleString('en-IN')}</strong>
          </div>
          <button onclick="InvoiceManager.renderModal('${b.id}')" class="btn-primary text-xs py-2 px-3">
            <i class="fa-solid fa-print mr-1"></i> Print / Download
          </button>
        </div>
      </div>
    `).join('');
  }
}

function getStatusBadgeClass(status) {
  if (status === 'Active') return 'bg-emerald-100 text-emerald-800 border border-emerald-300 dark:bg-emerald-900/40 dark:text-emerald-300';
  if (status === 'Upcoming') return 'bg-blue-100 text-blue-800 border border-blue-300 dark:bg-blue-900/40 dark:text-blue-300';
  if (status === 'Completed') return 'bg-slate-100 text-slate-800 border border-slate-300 dark:bg-slate-800 dark:text-slate-300';
  return 'bg-amber-100 text-amber-800';
}

function extendRental(id) {
  const addDays = prompt("How many additional days would you like to extend this machinery rental?", "2");
  if (addDays && parseInt(addDays) > 0) {
    const days = parseInt(addDays);
    const bookings = JSON.parse(localStorage.getItem('trarent_bookings') || '[]');
    const booking = bookings.find(b => b.id === id);
    if (booking) {
      booking.durationDays += days;
      const oldEnd = new Date(booking.endDate);
      oldEnd.setDate(oldEnd.getDate() + days);
      booking.endDate = oldEnd.toISOString().split('T')[0];
      const daily = Math.round(booking.baseCost / (booking.durationDays - days));
      booking.baseCost += daily * days;
      booking.totalAmount += daily * days;

      localStorage.setItem('trarent_bookings', JSON.stringify(bookings));
      renderDashboardData();
      showDashboardToast(`Rental extended by ${days} days until ${booking.endDate}!`, "success");
    }
  }
}

function requestAssistance(id) {
  showDashboardToast(`Field engineer dispatched for booking ${id}. Contact: +91 94123 00000`, "success");
}

function showDashboardToast(msg, type = "success") {
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

window.renderDashboardData = renderDashboardData;
window.extendRental = extendRental;
window.requestAssistance = requestAssistance;
