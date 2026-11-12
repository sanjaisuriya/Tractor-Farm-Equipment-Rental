/**
 * Tractor & Farm Equipment Rental - Farmer Dashboard Engine
 * Implements 12 Seed Bookings, KPI Cards, Rental Tracking, Invoices, Status Stepper & Profile Editor
 */

const SEED_DATA_VERSION = 'agrorent_v3_12bookings';

const SEED_BOOKINGS = [
  {
    id: "TR-849201",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "harv-987",
    equipmentName: "Preet 987 Self-Propelled Combine Harvester",
    equipmentCategory: "Combine Harvesters",
    equipmentImage: "assets/images/equipment/preet-987-harvester.jpg",
    bookingDate: "04 Nov 2026",
    startDate: "2026-11-05",
    endDate: "2026-11-09",
    durationDays: 4,
    location: "Rampur Farm Sector 4, Ludhiana, Punjab",
    hasOperator: true,
    operatorName: "Gurpreet Singh (Certified)",
    operatorPhone: "+91 98140 12345",
    hasDelivery: true,
    notes: "Paddy crop harvesting on 22 acres",
    baseCost: 44000,
    operatorCost: 5000,
    deliveryCost: 1500,
    deposit: 2500,
    totalAmount: 53000,
    paidAmount: 50000,
    pendingAmount: 3000,
    paymentStatus: "Pending ₹3,000",
    status: "Active",
    engineHours: "34 hrs logged",
    gpsStatus: "Live at Sector 4 (30.9010° N, 75.8573° E)",
    currentStage: 3
  },
  {
    id: "TR-849202",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "seed-912",
    equipmentName: "Dasmesh 912 Happy Seeder",
    equipmentCategory: "Seed Drills & Planters",
    equipmentImage: "assets/images/equipment/dasmesh-happy-seeder.jpg",
    bookingDate: "06 Nov 2026",
    startDate: "2026-11-07",
    endDate: "2026-11-10",
    durationDays: 3,
    location: "Rampur Farm Sector 3, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated (Farmer)",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Direct wheat sowing into standing rice stubble",
    baseCost: 10500,
    operatorCost: 0,
    deliveryCost: 800,
    deposit: 1200,
    totalAmount: 12500,
    paidAmount: 10000,
    pendingAmount: 2500,
    paymentStatus: "Pending ₹2,500",
    status: "Active",
    engineHours: "18 hrs logged",
    gpsStatus: "Live at Sector 3 (30.8980° N, 75.8520° E)",
    currentStage: 3
  },
  {
    id: "TR-849203",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "tr-jd5310",
    equipmentName: "John Deere 5310 4WD Heavy Tractor",
    equipmentCategory: "Tractors",
    equipmentImage: "assets/images/equipment/john-deere-5310.jpg",
    bookingDate: "08 Nov 2026",
    startDate: "2026-11-09",
    endDate: "2026-11-14",
    durationDays: 5,
    location: "Rampur Farm Sector 5, Ludhiana, Punjab",
    hasOperator: true,
    operatorName: "Balwinder Singh (Gold Certified)",
    operatorPhone: "+91 98141 67890",
    hasDelivery: true,
    notes: "Laser land leveling and primary subsoiling",
    baseCost: 17500,
    operatorCost: 2500,
    deliveryCost: 500,
    deposit: 1500,
    totalAmount: 22000,
    paidAmount: 19000,
    pendingAmount: 3000,
    paymentStatus: "Pending ₹3,000",
    status: "Active",
    engineHours: "12 hrs logged",
    gpsStatus: "Live at Sector 5 (30.9050° N, 75.8610° E)",
    currentStage: 3
  },
  {
    id: "TR-721495",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "rot-shaktiman",
    equipmentName: "Shaktiman Semi-Champion 6 Feet Rotavator",
    equipmentCategory: "Rotavators",
    equipmentImage: "assets/images/equipment/rotavator-tilling.jpg",
    bookingDate: "09 Nov 2026",
    startDate: "2026-11-13",
    endDate: "2026-11-15",
    durationDays: 2,
    location: "Rampur Farm Sector 4, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated (Farmer)",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Fine tilth preparation for vegetable sowing",
    baseCost: 3200,
    operatorCost: 0,
    deliveryCost: 400,
    deposit: 600,
    totalAmount: 4200,
    paidAmount: 4200,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Upcoming",
    engineHours: "Scheduled (Dispatch 13 Nov)",
    gpsStatus: "At Ludhiana Agro Hub Depot",
    currentStage: 1
  },
  {
    id: "TR-603180",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "tr-mah575",
    equipmentName: "Mahindra 575 DI PowerPlus Tractor",
    equipmentCategory: "Tractors",
    equipmentImage: "assets/images/equipment/mahindra-575-di.jpg",
    bookingDate: "24 Oct 2026",
    startDate: "2026-10-25",
    endDate: "2026-10-28",
    durationDays: 3,
    location: "Rampur Farm Sector 2, Ludhiana, Punjab",
    hasOperator: true,
    operatorName: "Sukhdev Singh",
    operatorPhone: "+91 98722 33445",
    hasDelivery: true,
    notes: "Post-monsoon land clearing and tilling",
    baseCost: 10500,
    operatorCost: 1800,
    deliveryCost: 400,
    deposit: 800,
    totalAmount: 13500,
    paidAmount: 13500,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "26 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603181",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "tr-sonalika22",
    equipmentName: "Sonalika GT 22 Orchard Mini Tractor",
    equipmentCategory: "Mini Tractors",
    equipmentImage: "assets/images/equipment/sonalika-gt22-mini.jpg",
    bookingDate: "19 Oct 2026",
    startDate: "2026-10-20",
    endDate: "2026-10-22",
    durationDays: 2,
    location: "Rampur Guava Orchard Plot, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Inter-row weeding in fruit orchard",
    baseCost: 4600,
    operatorCost: 0,
    deliveryCost: 400,
    deposit: 800,
    totalAmount: 5800,
    paidAmount: 5800,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "16 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603182",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "plough-lemken",
    equipmentName: "Lemken 3-MB Reversible Hydraulic Plough",
    equipmentCategory: "Ploughs",
    equipmentImage: "assets/images/equipment/plough.jpg",
    bookingDate: "14 Oct 2026",
    startDate: "2026-10-15",
    endDate: "2026-10-17",
    durationDays: 2,
    location: "Rampur Farm Sector 1, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Deep soil inversion and weed eradication",
    baseCost: 2800,
    operatorCost: 0,
    deliveryCost: 300,
    deposit: 500,
    totalAmount: 3600,
    paidAmount: 3600,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "14 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603183",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "harrow-fieldking",
    equipmentName: "Fieldking Heavy-Duty Trailed Disc Harrow",
    equipmentCategory: "Harrows",
    equipmentImage: "assets/images/equipment/disc-harrow.jpg",
    bookingDate: "09 Oct 2026",
    startDate: "2026-10-10",
    endDate: "2026-10-13",
    durationDays: 3,
    location: "Rampur Farm Sector 2, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Breaking heavy clay clods after primary ploughing",
    baseCost: 3600,
    operatorCost: 0,
    deliveryCost: 400,
    deposit: 500,
    totalAmount: 4500,
    paidAmount: 4500,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "20 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603184",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "sprayer-kisankraft",
    equipmentName: "KisanKraft 500L Tractor Boom Sprayer",
    equipmentCategory: "Sprayers",
    equipmentImage: "assets/images/equipment/sprayer.jpg",
    bookingDate: "01 Oct 2026",
    startDate: "2026-10-02",
    endDate: "2026-10-03",
    durationDays: 1,
    location: "Rampur Farm Sector 4, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Organic fungicide application on cotton crop",
    baseCost: 1800,
    operatorCost: 0,
    deliveryCost: 300,
    deposit: 300,
    totalAmount: 2400,
    paidAmount: 2400,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "8 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603185",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "harv-987-sep",
    equipmentName: "Preet 987 Combine Harvester",
    equipmentCategory: "Combine Harvesters",
    equipmentImage: "assets/images/equipment/preet-987-harvester.jpg",
    bookingDate: "20 Sep 2026",
    startDate: "2026-09-22",
    endDate: "2026-09-26",
    durationDays: 4,
    location: "Rampur South Boundary, Ludhiana, Punjab",
    hasOperator: true,
    operatorName: "Gurpreet Singh (Certified)",
    operatorPhone: "+91 98140 12345",
    hasDelivery: true,
    notes: "Early Basmati paddy harvesting and threshing",
    baseCost: 43500,
    operatorCost: 5000,
    deliveryCost: 1500,
    deposit: 2000,
    totalAmount: 52000,
    paidAmount: 52000,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "38 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603186",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "rot-shaktiman-sep",
    equipmentName: "Shaktiman Semi-Champion Rotavator",
    equipmentCategory: "Rotavators",
    equipmentImage: "assets/images/equipment/rotavator-tilling.jpg",
    bookingDate: "12 Sep 2026",
    startDate: "2026-09-14",
    endDate: "2026-09-17",
    durationDays: 3,
    location: "Rampur Farm Sector 1, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Post-harvest stubble incorporation and aeration",
    baseCost: 4500,
    operatorCost: 0,
    deliveryCost: 400,
    deposit: 500,
    totalAmount: 5400,
    paidAmount: 5400,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "24 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  },
  {
    id: "TR-603187",
    farmerName: "Rajesh Kumar",
    mobile: "+91 98765 43210",
    email: "farmer@agrorent.in",
    equipmentId: "trailer-5t",
    equipmentName: "Heavy Duty Hydraulic Tipping Trolley",
    equipmentCategory: "Trailers & Trolleys",
    equipmentImage: "assets/images/equipment/trailer.jpg",
    bookingDate: "03 Sep 2026",
    startDate: "2026-09-05",
    endDate: "2026-09-07",
    durationDays: 2,
    location: "Rampur Farm to Mandi, Ludhiana, Punjab",
    hasOperator: false,
    operatorName: "Self-Operated",
    operatorPhone: "+91 98765 43210",
    hasDelivery: true,
    notes: "Grain transport to Khanna Grain Market",
    baseCost: 2200,
    operatorCost: 0,
    deliveryCost: 300,
    deposit: 500,
    totalAmount: 3000,
    paidAmount: 3000,
    pendingAmount: 0,
    paymentStatus: "Paid in Full",
    status: "Completed",
    engineHours: "16 hrs (Completed)",
    gpsStatus: "Returned to Depot",
    currentStage: 5
  }
];

document.addEventListener('DOMContentLoaded', () => {
  // 1. Authenticate & Protect Dashboard
  if (window.Auth && typeof Auth.protectDashboard === 'function') {
    Auth.protectDashboard();
  }

  // 2. Ensure the 12 bookings are seeded
  initBookingsData();

  // 3. Load Profile Data
  loadUserProfile();

  // 4. Setup Tabs
  setupDashboardTabs();

  // 5. Render All Panels & Metrics
  renderDashboardData();

  // 6. Mobile Sidebar Toggle & Backdrop
  setupMobileSidebar();

  // 7. Profile Form Save
  setupProfileForm();

  // 8. Search & Filter for My Bookings
  setupBookingsFilters();
});

function initBookingsData() {
  const version = localStorage.getItem('trarent_version');
  const stored = localStorage.getItem('trarent_bookings');
  if (!stored || version !== SEED_DATA_VERSION) {
    localStorage.setItem('trarent_bookings', JSON.stringify(SEED_BOOKINGS));
    localStorage.setItem('trarent_version', SEED_DATA_VERSION);
  }
}

function getStoredBookings() {
  return JSON.parse(localStorage.getItem('trarent_bookings') || '[]');
}

function saveBookings(bookings) {
  localStorage.setItem('trarent_bookings', JSON.stringify(bookings));
}

function loadUserProfile() {
  const user = window.Auth ? Auth.getUser() : {
    name: "Rajesh Kumar",
    email: "farmer@agrorent.in",
    mobile: "+91 98765 43210",
    village: "Rampur, Ludhiana, Punjab",
    farmSize: "12 Acres",
    primaryCrops: "Wheat, Paddy, Mustard"
  };

  document.querySelectorAll('.user-name-display').forEach(el => el.textContent = user.name || "Rajesh Kumar");
  document.querySelectorAll('.user-email-display').forEach(el => el.textContent = user.email || "farmer@agrorent.in");
  document.querySelectorAll('.user-village-display').forEach(el => el.textContent = user.village || "Rampur, Punjab");
  document.querySelectorAll('.user-farmsize-display').forEach(el => el.textContent = user.farmSize || "12 Acres");

  const profName = document.getElementById('profName');
  const profEmail = document.getElementById('profEmail');
  const profMobile = document.getElementById('profMobile');
  const profVillage = document.getElementById('profVillage');
  const profFarmSize = document.getElementById('profFarmSize');
  const profCrops = document.getElementById('profCrops');

  if (profName) profName.value = user.name || "Rajesh Kumar";
  if (profEmail) profEmail.value = user.email || "farmer@agrorent.in";
  if (profMobile) profMobile.value = user.mobile || "+91 98765 43210";
  if (profVillage) profVillage.value = user.village || "Rampur, Ludhiana, Punjab";
  if (profFarmSize) profFarmSize.value = user.farmSize || "12 Acres";
  if (profCrops) profCrops.value = user.primaryCrops || "Wheat, Paddy, Mustard";
}

function setupProfileForm() {
  const profileForm = document.getElementById('farmerProfileForm');
  const profNameInput = document.getElementById('profName');
  const profMobileInput = document.getElementById('profMobile');

  if (profNameInput) {
    profNameInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/[^a-zA-Z\s]/g, '');
    });
    profNameInput.addEventListener('keydown', (e) => {
      if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      if (e.ctrlKey || e.metaKey) return;
      if (e.key === ' ') return;
      if (!/^[a-zA-Z]$/.test(e.key)) {
        e.preventDefault();
      }
    });
  }

  if (profMobileInput) {
    profMobileInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/\D/g, '').slice(0, 10);
    });
    profMobileInput.addEventListener('keydown', (e) => {
      if (['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      if (e.ctrlKey || e.metaKey) return;
      if (!/^[0-9]$/.test(e.key)) {
        e.preventDefault();
      }
      if (profMobileInput.value.length >= 10 && profMobileInput.selectionStart === profMobileInput.selectionEnd) {
        e.preventDefault();
      }
    });
  }

  if (profileForm) {
    profileForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const updatedUser = {
        name: document.getElementById('profName').value.trim() || "Rajesh Kumar",
        email: document.getElementById('profEmail').value.trim() || "farmer@agrorent.in",
        mobile: document.getElementById('profMobile').value.trim() || "+91 98765 43210",
        village: document.getElementById('profVillage').value.trim() || "Rampur, Ludhiana, Punjab",
        farmSize: document.getElementById('profFarmSize').value.trim() || "12 Acres",
        primaryCrops: document.getElementById('profCrops')?.value.trim() || "Wheat, Paddy, Mustard",
        memberSince: "March 2024",
        role: "Verified Progressive Farmer"
      };

      if (window.Auth) {
        Auth.setUser(updatedUser);
      }
      loadUserProfile();
      showDashboardToast("Farmer profile saved successfully! Updated across your portal.", "success");
    });
  }
}

function setupDashboardTabs() {
  const tabLinks = document.querySelectorAll('.sidebar-link[data-tab]');
  const tabPanels = document.querySelectorAll('.tab-content-panel');

  tabLinks.forEach(link => {
    link.addEventListener('click', () => {
      const tabId = link.getAttribute('data-tab');

      if (tabId === 'logout') {
        if (window.Auth) Auth.logout();
        else window.location.href = 'index.html';
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

      // Close mobile sidebar
      const sidebar = document.getElementById('dashboardSidebar');
      const backdrop = document.getElementById('dashboardBackdrop');
      if (sidebar && window.innerWidth < 1024) {
        sidebar.classList.remove('active');
        if (backdrop) backdrop.classList.remove('active');
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });
}

function setupMobileSidebar() {
  const sidebarToggle = document.getElementById('dashboardSidebarToggle');
  const sidebar = document.getElementById('dashboardSidebar');
  const sidebarClose = document.getElementById('dashboardSidebarClose');
  const backdrop = document.getElementById('dashboardBackdrop');

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.add('active');
      if (backdrop) backdrop.classList.add('active');
    });
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('active');
    if (backdrop) backdrop.classList.remove('active');
  }

  if (sidebarClose) sidebarClose.addEventListener('click', closeSidebar);
  if (backdrop) backdrop.addEventListener('click', closeSidebar);
}

function renderDashboardData() {
  const bookings = getStoredBookings();

  // Metrics calculation
  const totalCount = bookings.length;
  const activeCount = bookings.filter(b => b.status === 'Active').length;
  const completedCount = bookings.filter(b => b.status === 'Completed').length;
  const upcomingCount = bookings.filter(b => b.status === 'Upcoming').length;
  const pendingAmount = bookings.reduce((sum, b) => sum + (b.pendingAmount || 0), 0);
  const totalCost = bookings.reduce((sum, b) => sum + (b.totalAmount || 0), 0);
  const paidAmount = bookings.reduce((sum, b) => sum + (b.paidAmount || 0), 0);

  // 1. KPI Cards (Explicit prompt requirements: Total: 12, Active: 3, Completed: 8, Pending: ₹8,500)
  const totalEl = document.getElementById('kpiTotalBookings');
  const activeEl = document.getElementById('kpiActiveRentals');
  const completedEl = document.getElementById('kpiCompletedRentals');
  const pendingEl = document.getElementById('kpiPendingPayments');

  if (totalEl) totalEl.textContent = totalCount;
  if (activeEl) activeEl.textContent = activeCount;
  if (completedEl) completedEl.textContent = completedCount;
  if (pendingEl) pendingEl.textContent = `₹${pendingAmount.toLocaleString('en-IN')}`;

  // 2. Financial Summary in Payments Tab
  const finTotalEl = document.getElementById('finTotalCost');
  const finPaidEl = document.getElementById('finPaidAmount');
  const finPendingEl = document.getElementById('finPendingAmount');
  const finStatusEl = document.getElementById('finPaymentStatus');

  if (finTotalEl) finTotalEl.textContent = `₹${totalCost.toLocaleString('en-IN')}`;
  if (finPaidEl) finPaidEl.textContent = `₹${paidAmount.toLocaleString('en-IN')}`;
  if (finPendingEl) finPendingEl.textContent = `₹${pendingAmount.toLocaleString('en-IN')}`;
  if (finStatusEl) {
    if (pendingAmount > 0) {
      finStatusEl.className = "inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-800 dark:bg-amber-900/40 dark:text-amber-300 border border-amber-300";
      finStatusEl.innerHTML = `<i class="fa-solid fa-clock"></i> Pending Settlement: ₹${pendingAmount.toLocaleString('en-IN')}`;
    } else {
      finStatusEl.className = "inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-300 border border-green-300";
      finStatusEl.innerHTML = `<i class="fa-solid fa-circle-check"></i> All Payments Settled`;
    }
  }

  // 3. Overview: Recent Bookings Preview (Features Preet 987, Dasmesh Happy Seeder, Shaktiman Rotavator, John Deere)
  renderRecentBookingsPreview(bookings);

  // 4. "My Bookings" Table (All 12 Bookings)
  renderMyBookingsTable(bookings);

  // 5. "Rental Tracking" Hub (Upcoming, Currently Rented, Completed)
  renderRentalTracking(bookings);

  // 6. "Payment Details" Invoices Table
  renderPaymentInvoicesTable(bookings);
}

// Render Recent Bookings in Overview (top 4 items: Preet Harvester, Dasmesh Seeder, John Deere Tractor, Shaktiman Rotavator)
function renderRecentBookingsPreview(bookings) {
  const container = document.getElementById('recentBookingsList');
  if (!container) return;

  const previewItems = bookings.slice(0, 4);
  container.innerHTML = previewItems.map(b => `
    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between p-4 rounded-xl bg-slate-50 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-700/80 hover:border-agri transition gap-4">
      <div class="flex items-center gap-3 sm:gap-4 min-w-0">
        <img src="${b.equipmentImage}" alt="${b.equipmentName}" class="w-14 h-14 sm:w-16 sm:h-16 rounded-xl object-cover border border-slate-200 dark:border-slate-700 flex-shrink-0" />
        <div class="min-w-0">
          <div class="flex flex-wrap items-center gap-2 mb-1">
            <span class="text-xs font-mono font-bold text-slate-500">${b.id}</span>
            <span class="px-2 py-0.5 text-[11px] font-bold rounded-full ${getStatusBadgeClass(b.status)}">${b.status}</span>
            <span class="text-[10px] text-muted hidden sm:inline"><i class="fa-solid fa-calendar mr-1"></i>${b.bookingDate}</span>
          </div>
          <h4 class="font-bold text-sm sm:text-base text-slate-900 dark:text-white truncate">${b.equipmentName}</h4>
          <p class="text-xs text-slate-600 dark:text-slate-300">
            <i class="fa-solid fa-clock text-agri mr-1"></i>${b.durationDays} Days (${b.startDate} to ${b.endDate})
          </p>
        </div>
      </div>
      <div class="flex sm:flex-col items-center sm:items-end justify-between w-full sm:w-auto gap-2 border-t sm:border-t-0 pt-2 sm:pt-0 border-slate-200 dark:border-slate-700">
        <div class="text-left sm:text-right">
          <span class="text-xs text-muted block">Total Rental</span>
          <span class="font-black text-agri dark:text-fresh text-base sm:text-lg">₹${b.totalAmount.toLocaleString('en-IN')}</span>
        </div>
        <div class="flex items-center gap-1.5">
          <button onclick="viewBookingDetails('${b.id}')" class="btn-secondary text-[11px] py-1.5 px-2.5" title="View Specifications">
            <i class="fa-solid fa-circle-info mr-1"></i> Details
          </button>
          <button onclick="trackBookingStatus('${b.id}')" class="btn-primary text-[11px] py-1.5 px-2.5" title="Track Live Status">
            <i class="fa-solid fa-location-dot mr-1"></i> Track
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

// Render Full "My Equipment Bookings" Table
function renderMyBookingsTable(bookings, filter = 'all', searchQuery = '') {
  const tbody = document.getElementById('myBookingsTableBody');
  const countEl = document.getElementById('myBookingsCount');
  if (!tbody) return;

  let filtered = [...bookings];
  if (filter !== 'all') {
    filtered = filtered.filter(b => b.status.toLowerCase() === filter.toLowerCase());
  }
  if (searchQuery) {
    const q = searchQuery.toLowerCase();
    filtered = filtered.filter(b =>
      b.id.toLowerCase().includes(q) ||
      b.equipmentName.toLowerCase().includes(q) ||
      b.equipmentCategory.toLowerCase().includes(q)
    );
  }

  if (countEl) countEl.textContent = `Showing ${filtered.length} of ${bookings.length} Bookings`;

  if (filtered.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="7" class="p-8 text-center text-slate-500 dark:text-slate-400">
          <i class="fa-solid fa-magnifying-glass text-2xl mb-2 block"></i>
          No equipment bookings found matching the current filter.
        </td>
      </tr>
    `;
    return;
  }

  tbody.innerHTML = filtered.map(b => `
    <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition">
      <!-- Equipment Name -->
      <td class="p-4">
        <div class="flex items-center gap-3">
          <img src="${b.equipmentImage}" alt="${b.equipmentName}" class="w-12 h-12 rounded-xl object-cover border border-slate-200 dark:border-slate-700 flex-shrink-0" />
          <div class="min-w-0">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white truncate max-w-xs">${b.equipmentName}</h4>
            <span class="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-1.5">
              <i class="fa-solid fa-tag text-[10px] text-agri"></i> ${b.equipmentCategory}
            </span>
          </div>
        </div>
      </td>

      <!-- Booking ID -->
      <td class="p-4 font-mono font-bold text-xs text-slate-700 dark:text-slate-300 whitespace-nowrap">
        ${b.id}
      </td>

      <!-- Booking Date -->
      <td class="p-4 text-xs text-slate-600 dark:text-slate-300 whitespace-nowrap">
        <i class="fa-regular fa-calendar-check mr-1 text-slate-400"></i>${b.bookingDate}
      </td>

      <!-- Rental Duration -->
      <td class="p-4 text-xs text-slate-800 dark:text-slate-200 whitespace-nowrap">
        <span class="font-bold text-forest dark:text-fresh">${b.durationDays} Days</span>
        <span class="block text-[11px] text-muted">${b.startDate} to ${b.endDate}</span>
      </td>

      <!-- Total Amount -->
      <td class="p-4 whitespace-nowrap">
        <span class="font-black text-sm text-slate-900 dark:text-white block">₹${b.totalAmount.toLocaleString('en-IN')}</span>
        <span class="text-[10px] ${b.pendingAmount > 0 ? 'text-amber-600 dark:text-amber-400 font-semibold' : 'text-green-600 dark:text-green-400'}">
          ${b.pendingAmount > 0 ? `Pending: ₹${b.pendingAmount.toLocaleString('en-IN')}` : 'Paid in Full'}
        </span>
      </td>

      <!-- Booking Status -->
      <td class="p-4 whitespace-nowrap">
        <span class="px-2.5 py-1 text-xs font-bold rounded-full ${getStatusBadgeClass(b.status)}">
          ${b.status}
        </span>
      </td>

      <!-- Actions -->
      <td class="p-4 text-right whitespace-nowrap">
        <div class="flex items-center justify-end gap-1.5">
          <button onclick="viewBookingDetails('${b.id}')" class="btn-secondary text-xs py-1.5 px-2.5" title="View Details">
            <i class="fa-solid fa-eye"></i>
          </button>
          <button onclick="trackBookingStatus('${b.id}')" class="btn-secondary text-xs py-1.5 px-2.5 text-agri border-agri/30" title="Track Live Rental Status">
            <i class="fa-solid fa-location-dot"></i>
          </button>
          <button onclick="viewInvoiceModal('${b.id}')" class="btn-primary text-xs py-1.5 px-2.5" title="View Invoice">
            <i class="fa-solid fa-file-invoice"></i>
          </button>
          ${b.status === 'Upcoming' ? `
            <button onclick="openCancelModal('${b.id}')" class="btn-secondary text-xs py-1.5 px-2.5 text-red-600 dark:text-red-400 border-red-300 dark:border-red-800 hover:bg-red-50 dark:hover:bg-red-950/40" title="Cancel Booking">
              <i class="fa-solid fa-ban"></i>
            </button>
          ` : ''}
        </div>
      </td>
    </tr>
  `).join('');
}

function setupBookingsFilters() {
  const filterBtns = document.querySelectorAll('.booking-filter-btn');
  const searchInput = document.getElementById('bookingSearchInput');

  let currentFilter = 'all';
  let currentSearch = '';

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('bg-agri', 'text-white');
        b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
      });
      btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
      btn.classList.add('bg-agri', 'text-white');

      currentFilter = btn.getAttribute('data-filter') || 'all';
      renderMyBookingsTable(getStoredBookings(), currentFilter, currentSearch);
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value.trim();
      renderMyBookingsTable(getStoredBookings(), currentFilter, currentSearch);
    });
  }
}

// Render "Rental Tracking" Hub with 3 sub-sections: Upcoming Rentals, Currently Rented Equipment, Completed Rentals
function renderRentalTracking(bookings) {
  // 1. Currently Rented Equipment (Active)
  const activeContainer = document.getElementById('activeRentalsTrackingContainer');
  if (activeContainer) {
    const activeItems = bookings.filter(b => b.status === 'Active');
    if (activeItems.length === 0) {
      activeContainer.innerHTML = `
        <div class="p-6 text-center bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700">
          <i class="fa-solid fa-tractor text-3xl text-slate-300 mb-2"></i>
          <p class="text-sm font-semibold text-slate-600 dark:text-slate-300">No equipment currently active in fields.</p>
        </div>
      `;
    } else {
      activeContainer.innerHTML = activeItems.map(item => `
        <div class="p-6 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col lg:flex-row gap-6 items-start lg:items-center">
          <img src="${item.equipmentImage}" alt="${item.equipmentName}" class="w-full lg:w-56 h-44 rounded-xl object-cover border border-slate-200 dark:border-slate-700 flex-shrink-0" />
          <div class="flex-1 w-full">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
              <div class="flex items-center gap-2">
                <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-green-100 text-green-800 dark:bg-green-900/50 dark:text-green-300 border border-green-300 animate-pulse">
                  <span class="w-2 h-2 rounded-full bg-green-600"></span> Live Field Deployed
                </span>
                <span class="font-mono text-xs font-bold text-slate-500">${item.id}</span>
              </div>
              <span class="text-xs text-muted font-medium"><i class="fa-solid fa-clock text-agri mr-1"></i>Return: <strong class="text-slate-900 dark:text-white">${item.endDate}</strong></span>
            </div>

            <h3 class="text-lg sm:text-xl font-black text-slate-900 dark:text-white mb-1.5">${item.equipmentName}</h3>
            <p class="text-xs text-slate-600 dark:text-slate-300 mb-3 flex items-center gap-1.5">
              <i class="fa-solid fa-location-dot text-red-500"></i> ${item.location}
            </p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 p-3 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-700/60 text-xs mb-4">
              <div>
                <span class="text-muted block text-[11px]">Rental Duration</span>
                <strong class="text-slate-900 dark:text-white font-bold">${item.durationDays} Days</strong>
              </div>
              <div>
                <span class="text-muted block text-[11px]">Assigned Operator</span>
                <strong class="text-slate-900 dark:text-white font-bold truncate block">${item.operatorName}</strong>
              </div>
              <div>
                <span class="text-muted block text-[11px]">Telemetry Log</span>
                <strong class="text-forest dark:text-fresh font-bold">${item.engineHours}</strong>
              </div>
              <div>
                <span class="text-muted block text-[11px]">GPS Status</span>
                <strong class="text-slate-900 dark:text-white font-bold truncate block">${item.gpsStatus}</strong>
              </div>
            </div>

            <div class="flex flex-wrap items-center gap-2">
              <button onclick="extendRentalPrompt('${item.id}')" class="btn-secondary text-xs py-2 px-3 font-semibold">
                <i class="fa-solid fa-clock-rotate-left mr-1.5 text-agri"></i> Extend Rental
              </button>
              <button onclick="requestFieldAssistance('${item.id}')" class="btn-secondary text-xs py-2 px-3 font-semibold text-amber-700 dark:text-amber-400 border-amber-300 dark:border-amber-800">
                <i class="fa-solid fa-wrench mr-1.5"></i> Request Field Support
              </button>
              <button onclick="trackBookingStatus('${item.id}')" class="btn-primary text-xs py-2 px-3 font-bold">
                <i class="fa-solid fa-route mr-1.5"></i> Track Machine Workflow
              </button>
            </div>
          </div>
        </div>
      `).join('');
    }
  }

  // 2. Upcoming Rentals
  const upcomingContainer = document.getElementById('upcomingRentalsTrackingContainer');
  if (upcomingContainer) {
    const upcomingItems = bookings.filter(b => b.status === 'Upcoming');
    if (upcomingItems.length === 0) {
      upcomingContainer.innerHTML = `
        <div class="p-6 text-center bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700">
          <i class="fa-solid fa-calendar-check text-3xl text-slate-300 mb-2"></i>
          <p class="text-sm font-semibold text-slate-600 dark:text-slate-300">No upcoming machinery bookings scheduled.</p>
          <a href="booking.html" class="btn-primary text-xs py-2 px-4 mt-3 inline-block">Book Farm Equipment</a>
        </div>
      `;
    } else {
      upcomingContainer.innerHTML = upcomingItems.map(item => `
        <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <img src="${item.equipmentImage}" alt="${item.equipmentName}" class="w-16 h-16 rounded-xl object-cover border border-slate-200 dark:border-slate-700 flex-shrink-0" />
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="px-2 py-0.5 text-xs font-bold rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 border border-blue-300">Scheduled Dispatch</span>
                <span class="font-mono text-xs font-bold text-slate-500">${item.id}</span>
              </div>
              <h4 class="font-bold text-base text-slate-900 dark:text-white">${item.equipmentName}</h4>
              <p class="text-xs text-slate-600 dark:text-slate-300">
                <i class="fa-solid fa-calendar-days text-blue-500 mr-1"></i> Start Date: <strong>${item.startDate}</strong> | Duration: <strong>${item.durationDays} Days</strong>
              </p>
            </div>
          </div>
          <div class="flex items-center gap-2 w-full sm:w-auto justify-end">
            <button onclick="trackBookingStatus('${item.id}')" class="btn-secondary text-xs py-2 px-3">
              <i class="fa-solid fa-location-dot mr-1"></i> Track Dispatch
            </button>
            <button onclick="openCancelModal('${item.id}')" class="btn-secondary text-xs py-2 px-3 text-red-600 dark:text-red-400 border-red-300 dark:border-red-800 hover:bg-red-50">
              <i class="fa-solid fa-ban mr-1"></i> Cancel Booking
            </button>
          </div>
        </div>
      `).join('');
    }
  }

  // 3. Completed Rentals (8 items)
  const completedContainer = document.getElementById('completedRentalsTrackingContainer');
  if (completedContainer) {
    const completedItems = bookings.filter(b => b.status === 'Completed');
    completedContainer.innerHTML = completedItems.map(item => `
      <div class="p-4 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <img src="${item.equipmentImage}" alt="${item.equipmentName}" class="w-12 h-12 rounded-lg object-cover flex-shrink-0" />
          <div>
            <div class="flex items-center gap-2">
              <span class="font-bold text-xs text-slate-500 font-mono">${item.id}</span>
              <span class="px-2 py-0.5 text-[10px] font-bold rounded-full bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-300">Returned & Verified</span>
            </div>
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">${item.equipmentName}</h4>
            <p class="text-xs text-muted">Deployed: ${item.startDate} to ${item.endDate} (${item.durationDays} Days)</p>
          </div>
        </div>
        <div class="flex items-center gap-3 w-full sm:w-auto justify-between sm:justify-end">
          <span class="font-black text-slate-800 dark:text-white text-sm">₹${item.totalAmount.toLocaleString('en-IN')}</span>
          <button onclick="viewInvoiceModal('${item.id}')" class="btn-secondary text-xs py-1.5 px-3">
            <i class="fa-solid fa-file-invoice mr-1 text-agri"></i> Invoice
          </button>
        </div>
      </div>
    `).join('');
  }
}

// Render Invoices Table in Payments Tab
function renderPaymentInvoicesTable(bookings) {
  const container = document.getElementById('paymentInvoicesTableBody');
  if (!container) return;

  container.innerHTML = bookings.map(b => `
    <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition">
      <td class="p-4 font-mono font-bold text-xs text-forest dark:text-fresh">
        INV-${b.id}
      </td>
      <td class="p-4 text-xs text-slate-600 dark:text-slate-300 whitespace-nowrap">
        ${b.bookingDate}
      </td>
      <td class="p-4">
        <p class="font-bold text-sm text-slate-900 dark:text-white">${b.equipmentName}</p>
        <span class="text-xs text-muted">Base: ₹${b.baseCost.toLocaleString('en-IN')} | Oper: ₹${b.operatorCost.toLocaleString('en-IN')} | Deliv: ₹${b.deliveryCost.toLocaleString('en-IN')}</span>
      </td>
      <td class="p-4 font-black text-sm text-slate-900 dark:text-white whitespace-nowrap">
        ₹${b.totalAmount.toLocaleString('en-IN')}
      </td>
      <td class="p-4 text-xs text-green-600 dark:text-green-400 font-bold whitespace-nowrap">
        ₹${b.paidAmount.toLocaleString('en-IN')}
      </td>
      <td class="p-4 whitespace-nowrap">
        ${b.pendingAmount > 0 ? `
          <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-amber-100 text-amber-800 dark:bg-amber-900/40 dark:text-amber-300 border border-amber-300">
            Pending: ₹${b.pendingAmount.toLocaleString('en-IN')}
          </span>
        ` : `
          <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-300 border border-green-300">
            Paid in Full
          </span>
        `}
      </td>
      <td class="p-4 text-right whitespace-nowrap">
        <button onclick="viewInvoiceModal('${b.id}')" class="btn-primary text-xs py-1.5 px-3">
          <i class="fa-solid fa-print mr-1"></i> View Tax Invoice
        </button>
      </td>
    </tr>
  `).join('');
}

function getStatusBadgeClass(status) {
  if (status === 'Active') return 'bg-emerald-100 text-emerald-800 border border-emerald-300 dark:bg-emerald-900/50 dark:text-emerald-300';
  if (status === 'Upcoming') return 'bg-blue-100 text-blue-800 border border-blue-300 dark:bg-blue-900/50 dark:text-blue-300';
  if (status === 'Completed') return 'bg-slate-100 text-slate-800 border border-slate-300 dark:bg-slate-800 dark:text-slate-300';
  if (status === 'Cancelled') return 'bg-red-100 text-red-800 border border-red-300 dark:bg-red-900/50 dark:text-red-300';
  return 'bg-amber-100 text-amber-800';
}

// -------------------------------------------------------------
// MODALS & ACTIONS
// -------------------------------------------------------------

// 1. View Booking Details Modal
function viewBookingDetails(id) {
  const bookings = getStoredBookings();
  const b = bookings.find(item => item.id === id);
  if (!b) return;

  const modal = document.getElementById('bookingDetailsModal');
  const content = document.getElementById('bookingDetailsModalContent');
  if (!modal || !content) return;

  content.innerHTML = `
    <div class="flex items-start justify-between pb-4 border-b border-slate-200 dark:border-slate-700">
      <div>
        <span class="text-xs font-mono font-bold text-slate-500 block mb-1">BOOKING DETAILS & SPECIFICATIONS</span>
        <h3 class="text-xl font-black text-slate-900 dark:text-white font-heading">${b.equipmentName}</h3>
      </div>
      <button onclick="closeBookingDetailsModal()" class="text-slate-400 hover:text-slate-700 dark:hover:text-white p-1">
        <i class="fa-solid fa-xmark text-xl"></i>
      </button>
    </div>

    <div class="py-5 space-y-5">
      <div class="flex flex-col sm:flex-row gap-4 items-center p-4 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-700">
        <img src="${b.equipmentImage}" alt="${b.equipmentName}" class="w-full sm:w-36 h-28 rounded-xl object-cover border border-slate-300 dark:border-slate-700" />
        <div class="flex-1 space-y-1 text-xs">
          <div class="flex items-center gap-2">
            <span class="font-bold text-slate-900 dark:text-white text-sm">Booking ID: ${b.id}</span>
            <span class="px-2 py-0.5 font-bold rounded-full ${getStatusBadgeClass(b.status)}">${b.status}</span>
          </div>
          <p class="text-slate-600 dark:text-slate-300"><strong class="text-slate-500">Category:</strong> ${b.equipmentCategory}</p>
          <p class="text-slate-600 dark:text-slate-300"><strong class="text-slate-500">Booked On:</strong> ${b.bookingDate}</p>
          <p class="text-slate-600 dark:text-slate-300"><strong class="text-slate-500">Rental Period:</strong> ${b.startDate} to ${b.endDate} (${b.durationDays} Days)</p>
          <p class="text-slate-600 dark:text-slate-300"><strong class="text-slate-500">Delivery Location:</strong> ${b.location}</p>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
        <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-2">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm flex items-center gap-2">
            <i class="fa-solid fa-user-shield text-agri"></i> Operator & Delivery
          </h4>
          <p class="text-slate-600 dark:text-slate-300"><strong>Operator:</strong> ${b.hasOperator ? b.operatorName : 'Self-Operated by Farmer'}</p>
          ${b.hasOperator ? `<p class="text-slate-600 dark:text-slate-300"><strong>Operator Contact:</strong> ${b.operatorPhone}</p>` : ''}
          <p class="text-slate-600 dark:text-slate-300"><strong>Transport:</strong> Flatbed delivery included</p>
          <p class="text-slate-600 dark:text-slate-300"><strong>Field Notes:</strong> ${b.notes}</p>
        </div>

        <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-2">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm flex items-center gap-2">
            <i class="fa-solid fa-receipt text-agri"></i> Price Breakdown
          </h4>
          <div class="flex justify-between text-slate-600 dark:text-slate-300">
            <span>Base Rental Cost:</span>
            <strong>₹${b.baseCost.toLocaleString('en-IN')}</strong>
          </div>
          <div class="flex justify-between text-slate-600 dark:text-slate-300">
            <span>Operator Charges:</span>
            <strong>₹${b.operatorCost.toLocaleString('en-IN')}</strong>
          </div>
          <div class="flex justify-between text-slate-600 dark:text-slate-300">
            <span>Delivery & Fuel Surcharge:</span>
            <strong>₹${b.deliveryCost.toLocaleString('en-IN')}</strong>
          </div>
          <div class="flex justify-between text-slate-600 dark:text-slate-300">
            <span>Refundable Deposit:</span>
            <strong>₹${b.deposit.toLocaleString('en-IN')}</strong>
          </div>
          <div class="flex justify-between border-t border-slate-200 dark:border-slate-700 pt-2 font-bold text-slate-900 dark:text-white text-sm">
            <span>Total Rental:</span>
            <span class="text-agri dark:text-fresh font-black">₹${b.totalAmount.toLocaleString('en-IN')}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="flex items-center justify-end gap-3 pt-4 border-t border-slate-200 dark:border-slate-700">
      <button onclick="closeBookingDetailsModal()" class="btn-secondary text-xs py-2 px-4">Close</button>
      <button onclick="closeBookingDetailsModal(); trackBookingStatus('${b.id}');" class="btn-secondary text-xs py-2 px-4 text-agri border-agri">
        <i class="fa-solid fa-location-dot mr-1"></i> Track Live Status
      </button>
      <button onclick="closeBookingDetailsModal(); viewInvoiceModal('${b.id}');" class="btn-primary text-xs py-2 px-4">
        <i class="fa-solid fa-print mr-1"></i> View Tax Invoice
      </button>
    </div>
  `;

  modal.classList.add('active');
}

function closeBookingDetailsModal() {
  document.getElementById('bookingDetailsModal')?.classList.remove('active');
}

// 2. Track Rental Status Modal (Multi-step pipeline)
function trackBookingStatus(id) {
  const bookings = getStoredBookings();
  const b = bookings.find(item => item.id === id);
  if (!b) return;

  const modal = document.getElementById('trackingModal');
  const content = document.getElementById('trackingModalContent');
  if (!modal || !content) return;

  const stage = b.currentStage || (b.status === 'Completed' ? 5 : b.status === 'Active' ? 3 : 1);

  content.innerHTML = `
    <div class="flex items-start justify-between pb-4 border-b border-slate-200 dark:border-slate-700">
      <div>
        <span class="text-xs font-mono font-bold text-agri block mb-1">LIVE RENTAL WORKFLOW TRACKER</span>
        <h3 class="text-xl font-black text-slate-900 dark:text-white font-heading">${b.equipmentName}</h3>
        <p class="text-xs text-muted">Booking Reference: <strong class="text-slate-800 dark:text-slate-200 font-mono">${b.id}</strong></p>
      </div>
      <button onclick="closeTrackingModal()" class="text-slate-400 hover:text-slate-700 dark:hover:text-white p-1">
        <i class="fa-solid fa-xmark text-xl"></i>
      </button>
    </div>

    <div class="py-6">
      <!-- 5-Step Progress Stepper -->
      <div class="space-y-6">
        <!-- Step 1 -->
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0 ${stage >= 1 ? 'bg-agri text-white ring-4 ring-agri/20' : 'bg-slate-200 text-slate-600'}">
            <i class="fa-solid ${stage > 1 ? 'fa-check' : 'fa-clipboard-check'}"></i>
          </div>
          <div class="flex-1 pt-1">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">1. 50-Point Pre-Dispatch Mechanical Checklist Completed</h4>
            <p class="text-xs text-slate-600 dark:text-slate-300">Engine oils, blade calibration, tyre pressure, and fuel checked at AgroRent Ludhiana Depot.</p>
            <span class="text-[10px] text-green-600 dark:text-green-400 font-semibold block mt-0.5">Completed on ${b.bookingDate}</span>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0 ${stage >= 2 ? 'bg-agri text-white ring-4 ring-agri/20' : 'bg-slate-200 text-slate-600'}">
            <i class="fa-solid ${stage > 2 ? 'fa-check' : 'fa-truck-ramp-box'}"></i>
          </div>
          <div class="flex-1 pt-1">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">2. Flatbed Transport & Farm Gate Delivery</h4>
            <p class="text-xs text-slate-600 dark:text-slate-300">Machinery transported to ${b.location}. Handover checklist signed.</p>
            <span class="text-[10px] ${stage >= 2 ? 'text-green-600 dark:text-green-400 font-semibold' : 'text-slate-400'} block mt-0.5">
              ${stage >= 2 ? `Delivered on ${b.startDate}` : 'Scheduled for dispatch'}
            </span>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0 ${stage >= 3 ? 'bg-agri text-white ring-4 ring-agri/20 animate-pulse' : 'bg-slate-200 text-slate-600'}">
            <i class="fa-solid ${stage > 3 ? 'fa-check' : 'fa-tractor'}"></i>
          </div>
          <div class="flex-1 pt-1">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">3. Active Field Deployment & GPS Hour Logging</h4>
            <p class="text-xs text-slate-600 dark:text-slate-300">Live coordinates: ${b.gpsStatus} | Telemetry: ${b.engineHours}</p>
            <span class="text-[10px] ${stage >= 3 ? 'text-green-600 dark:text-green-400 font-semibold' : 'text-slate-400'} block mt-0.5">
              ${stage === 3 ? 'Active Now - Operator working in fields' : stage > 3 ? 'Operation Finished' : 'Pending start'}
            </span>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0 ${stage >= 4 ? 'bg-agri text-white ring-4 ring-agri/20' : 'bg-slate-200 text-slate-600'}">
            <i class="fa-solid ${stage > 4 ? 'fa-check' : 'fa-hourglass-end'}"></i>
          </div>
          <div class="flex-1 pt-1">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">4. Harvest / Tillage Completion & Post-Use Inspection</h4>
            <p class="text-xs text-slate-600 dark:text-slate-300">Machine cleaning, fuel reconciliation, and wear-and-tear assessment.</p>
            <span class="text-[10px] ${stage >= 4 ? 'text-green-600 dark:text-green-400 font-semibold' : 'text-slate-400'} block mt-0.5">
              ${stage >= 4 ? `Completed on ${b.endDate}` : `Scheduled return on ${b.endDate}`}
            </span>
          </div>
        </div>

        <!-- Step 5 -->
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0 ${stage >= 5 ? 'bg-agri text-white ring-4 ring-agri/20' : 'bg-slate-200 text-slate-600'}">
            <i class="fa-solid fa-circle-check"></i>
          </div>
          <div class="flex-1 pt-1">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">5. Deposit Settlement & Official GST Tax Receipt</h4>
            <p class="text-xs text-slate-600 dark:text-slate-300">Refund of ₹${b.deposit.toLocaleString('en-IN')} processed to farmer bank account.</p>
            <span class="text-[10px] ${stage >= 5 ? 'text-green-600 dark:text-green-400 font-semibold' : 'text-slate-400'} block mt-0.5">
              ${stage >= 5 ? 'Fully Settled & Closed' : 'Pending completion'}
            </span>
          </div>
        </div>
      </div>
    </div>

    <div class="flex items-center justify-end gap-3 pt-4 border-t border-slate-200 dark:border-slate-700">
      <button onclick="closeTrackingModal()" class="btn-secondary text-xs py-2 px-4">Close</button>
      <button onclick="requestFieldAssistance('${b.id}'); closeTrackingModal();" class="btn-primary text-xs py-2 px-4">
        <i class="fa-solid fa-headset mr-1"></i> Contact Field Dispatch
      </button>
    </div>
  `;

  modal.classList.add('active');
}

function closeTrackingModal() {
  document.getElementById('trackingModal')?.classList.remove('active');
}

// 3. Cancel Booking Modal & Action
let pendingCancelId = null;

function openCancelModal(id) {
  pendingCancelId = id;
  const bookings = getStoredBookings();
  const b = bookings.find(item => item.id === id);
  if (!b) return;

  const modal = document.getElementById('cancelModal');
  const detailsEl = document.getElementById('cancelModalDetails');
  if (detailsEl) {
    detailsEl.textContent = `Are you sure you want to cancel booking ${b.id} for "${b.equipmentName}"? A full refund of ₹${b.totalAmount.toLocaleString('en-IN')} will be credited.`;
  }
  if (modal) modal.classList.add('active');
}

function closeCancelModal() {
  pendingCancelId = null;
  document.getElementById('cancelModal')?.classList.remove('active');
}

function confirmCancelBooking() {
  if (!pendingCancelId) return;

  const bookings = getStoredBookings();
  const b = bookings.find(item => item.id === pendingCancelId);
  if (b) {
    b.status = 'Cancelled';
    b.pendingAmount = 0;
    saveBookings(bookings);
    renderDashboardData();
    showDashboardToast(`Booking ${b.id} has been cancelled. Full refund of ₹${b.totalAmount.toLocaleString('en-IN')} initiated!`, "success");
  }
  closeCancelModal();
}

// 4. View Invoice Modal (Integrated with InvoiceManager)
function viewInvoiceModal(id) {
  if (window.InvoiceManager && typeof InvoiceManager.renderModal === 'function') {
    InvoiceManager.renderModal(id);
  } else {
    alert(`Tax Invoice #INV-${id} for AgroRent Booking.`);
  }
}

// 5. Extend Rental Prompt
function extendRentalPrompt(id) {
  const addDays = prompt("How many additional days would you like to extend this machinery rental?", "2");
  if (addDays && parseInt(addDays) > 0) {
    const days = parseInt(addDays);
    const bookings = getStoredBookings();
    const b = bookings.find(item => item.id === id);
    if (b) {
      b.durationDays += days;
      const oldEnd = new Date(b.endDate);
      oldEnd.setDate(oldEnd.getDate() + days);
      b.endDate = oldEnd.toISOString().split('T')[0];

      const dailyRate = Math.round(b.baseCost / (b.durationDays - days));
      b.baseCost += dailyRate * days;
      b.totalAmount += dailyRate * days;
      b.pendingAmount += dailyRate * days;

      saveBookings(bookings);
      renderDashboardData();
      showDashboardToast(`Rental extended by ${days} days until ${b.endDate}! New pending balance: ₹${b.pendingAmount.toLocaleString('en-IN')}`, "success");
    }
  }
}

// 6. Request Field Assistance
function requestFieldAssistance(id) {
  showDashboardToast(`Field support technician dispatched for booking ${id}. Hotline: +91 94123 00000`, "success");
}

// 7. Settle Pending Balance (Demo Feature)
function settlePendingPayment() {
  const bookings = getStoredBookings();
  let settledCount = 0;
  bookings.forEach(b => {
    if (b.pendingAmount > 0) {
      b.paidAmount += b.pendingAmount;
      b.pendingAmount = 0;
      b.paymentStatus = "Paid in Full";
      settledCount++;
    }
  });

  if (settledCount > 0) {
    saveBookings(bookings);
    renderDashboardData();
    showDashboardToast("All pending payments (₹8,500) successfully cleared via UPI Demo! Invoices updated.", "success");
  } else {
    showDashboardToast("No pending balance found. All machinery invoices are already paid in full!", "success");
  }
}

// 8. Toast Helper
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

// Expose globals for onclick handlers
window.renderDashboardData = renderDashboardData;
window.viewBookingDetails = viewBookingDetails;
window.closeBookingDetailsModal = closeBookingDetailsModal;
window.trackBookingStatus = trackBookingStatus;
window.closeTrackingModal = closeTrackingModal;
window.openCancelModal = openCancelModal;
window.closeCancelModal = closeCancelModal;
window.confirmCancelBooking = confirmCancelBooking;
window.viewInvoiceModal = viewInvoiceModal;
window.extendRentalPrompt = extendRentalPrompt;
window.requestFieldAssistance = requestFieldAssistance;
window.settlePendingPayment = settlePendingPayment;
window.showDashboardToast = showDashboardToast;
