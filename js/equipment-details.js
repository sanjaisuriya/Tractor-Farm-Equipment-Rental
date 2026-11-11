/**
 * Tractor & Farm Equipment Rental - Equipment Details Page Logic
 */

document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const equipId = params.get('id') || 'tr-575';
  const customImg = params.get('img');
  const item = EquipmentService.getById(equipId);

  if (!item) return;

  if (customImg) {
    item.image = customImg;
    if (item.gallery && !item.gallery.includes(customImg)) {
      item.gallery.unshift(customImg);
    }
  }

  // Set Title & Breadcrumbs
  const titleEl = document.getElementById('detailsTitle');
  const catEl = document.getElementById('detailsCategory');
  const breadcrumbEl = document.getElementById('detailsBreadcrumb');
  const shortDescEl = document.getElementById('detailsShortDesc');
  const longDescEl = document.getElementById('detailsLongDesc');
  const hpBadge = document.getElementById('detailsHpBadge');
  const ratingEl = document.getElementById('detailsRating');
  const reviewsCountEl = document.getElementById('detailsReviewsCount');
  const availBadge = document.getElementById('detailsAvailability');

  if (titleEl) titleEl.textContent = item.name;
  if (catEl) catEl.textContent = item.category;
  if (breadcrumbEl) breadcrumbEl.textContent = item.name;
  if (shortDescEl) shortDescEl.textContent = item.shortDesc;
  if (longDescEl) longDescEl.textContent = item.description;
  if (hpBadge) hpBadge.innerHTML = `<i class="fa-solid fa-gauge-high mr-1"></i> ${item.hp}`;
  if (ratingEl) ratingEl.textContent = item.rating;
  if (reviewsCountEl) reviewsCountEl.textContent = `(${item.reviewsCount} verified farmer reviews)`;

  if (availBadge) {
    const isAvail = item.status === 'Available';
    availBadge.className = `badge-agri ${isAvail ? 'badge-available' : 'badge-booked'}`;
    availBadge.innerHTML = `<i class="fa-solid ${isAvail ? 'fa-circle-check' : 'fa-circle-xmark'}"></i> ${item.status}`;
  }

  // Set Rates
  const hourlyEl = document.getElementById('rateHourly');
  const dailyEl = document.getElementById('rateDaily');
  const weeklyEl = document.getElementById('rateWeekly');
  const monthlyEl = document.getElementById('rateMonthly');
  const operatorEl = document.getElementById('rateOperator');
  const transportEl = document.getElementById('rateTransport');

  if (hourlyEl) hourlyEl.textContent = `₹${item.hourlyRate.toLocaleString('en-IN')}`;
  if (dailyEl) dailyEl.textContent = `₹${item.dailyRate.toLocaleString('en-IN')}`;
  if (weeklyEl) weeklyEl.textContent = `₹${item.weeklyRate.toLocaleString('en-IN')}`;
  if (monthlyEl) monthlyEl.textContent = `₹${item.monthlyRate.toLocaleString('en-IN')}`;
  if (operatorEl) operatorEl.textContent = item.operatorRate > 0 ? `₹${item.operatorRate}/day` : 'N/A (Included or self-operate)';
  if (transportEl) transportEl.textContent = `₹${item.transportRate}/km`;

  // Specs Table
  const specsGrid = document.getElementById('detailsSpecs');
  if (specsGrid) {
    specsGrid.innerHTML = `
      <div class="spec-item"><span class="text-muted">Horsepower:</span><span class="font-bold text-slate-800 dark:text-white">${item.hp}</span></div>
      <div class="spec-item"><span class="text-muted">Engine:</span><span class="font-bold text-slate-800 dark:text-white">${item.engine}</span></div>
      <div class="spec-item"><span class="text-muted">Fuel Type:</span><span class="font-bold text-slate-800 dark:text-white">${item.fuelType}</span></div>
      <div class="spec-item"><span class="text-muted">Working Capacity:</span><span class="font-bold text-slate-800 dark:text-white">${item.workingCapacity}</span></div>
      <div class="spec-item"><span class="text-muted">Operator Option:</span><span class="font-bold text-slate-800 dark:text-white">${item.operatorRate > 0 ? 'Certified Driver Available' : 'Self-operated or tractor-hitched'}</span></div>
      <div class="spec-item"><span class="text-muted">Farm Delivery:</span><span class="font-bold text-slate-800 dark:text-white">Doorstep delivery within 2 hours</span></div>
    `;
  }

  // Features List
  const featuresList = document.getElementById('detailsFeatures');
  if (featuresList && item.features) {
    featuresList.innerHTML = item.features.map(f => `
      <li class="flex items-start gap-2.5 text-sm text-slate-700 dark:text-slate-300">
        <i class="fa-solid fa-circle-check text-agri dark:text-fresh mt-1 flex-shrink-0"></i>
        <span>${f}</span>
      </li>
    `).join('');
  }

  // Gallery
  const mainImg = document.getElementById('mainGalleryImg');
  const thumbsContainer = document.getElementById('galleryThumbnails');

  if (mainImg) {
    mainImg.src = item.image;
    mainImg.alt = item.name;
  }

  if (thumbsContainer && item.gallery) {
    thumbsContainer.innerHTML = item.gallery.map((imgUrl, index) => `
      <img src="${imgUrl}" alt="Thumbnail ${index + 1}" class="gallery-thumb ${index === 0 ? 'active' : ''}" data-full="${imgUrl}" />
    `).join('');

    thumbsContainer.querySelectorAll('.gallery-thumb').forEach(thumb => {
      thumb.addEventListener('click', () => {
        thumbsContainer.querySelectorAll('.gallery-thumb').forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');
        if (mainImg) {
          mainImg.src = thumb.getAttribute('data-full');
        }
      });
    });
  }

  // Book Button links
  const bookBtn = document.getElementById('btnBookThisEquipment');
  if (bookBtn) {
    bookBtn.href = `booking.html?id=${item.id}`;
  }

  // Related Equipment
  const relatedContainer = document.getElementById('relatedEquipmentGrid');
  if (relatedContainer) {
    const related = EQUIPMENT_DATA.filter(e => e.id !== item.id && (e.category === item.category || e.category === 'Tractors')).slice(0, 3);
    relatedContainer.innerHTML = related.map(r => EquipmentService.renderCard(r)).join('');
  }
});
