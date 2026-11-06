/**
 * Tractor & Farm Equipment Rental - Rates & Pricing Page Logic
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Rate Tier Tab Toggle (Daily / Hourly / Weekly / Monthly)
  const rateTabs = document.querySelectorAll('.rate-period-tab');
  const priceElements = document.querySelectorAll('.dynamic-price-value');
  const periodLabels = document.querySelectorAll('.dynamic-period-label');

  rateTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      rateTabs.forEach(t => t.classList.remove('active', 'bg-agri', 'text-white'));
      rateTabs.forEach(t => t.classList.add('bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-200'));

      tab.classList.remove('bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-200');
      tab.classList.add('active', 'bg-agri', 'text-white');

      const period = tab.getAttribute('data-period'); // 'hourly', 'daily', 'weekly', 'monthly'

      priceElements.forEach(el => {
        const hRate = el.getAttribute('data-hourly');
        const dRate = el.getAttribute('data-daily');
        const wRate = el.getAttribute('data-weekly');
        const mRate = el.getAttribute('data-monthly');

        let price = dRate;
        if (period === 'hourly') price = hRate;
        if (period === 'weekly') price = wRate;
        if (period === 'monthly') price = mRate;

        if (price) {
          el.textContent = `₹${parseInt(price).toLocaleString('en-IN')}`;
        }
      });

      periodLabels.forEach(lbl => {
        if (period === 'hourly') lbl.textContent = '/ hour';
        if (period === 'daily') lbl.textContent = '/ day';
        if (period === 'weekly') lbl.textContent = '/ week';
        if (period === 'monthly') lbl.textContent = '/ month';
      });
    });
  });

  // 2. Interactive Farmland Rental Cost & Acreage Estimator
  const operationSelect = document.getElementById('calcOperation');
  const acreageSlider = document.getElementById('calcAcreageSlider');
  const acreageDisplay = document.getElementById('calcAcreageDisplay');
  const operatorCheckbox = document.getElementById('calcOperatorCheck');
  const fuelCheckbox = document.getElementById('calcFuelCheck');

  const outMachine = document.getElementById('calcOutMachine');
  const outHours = document.getElementById('calcOutHours');
  const outCost = document.getElementById('calcOutCost');
  const outFuel = document.getElementById('calcOutFuel');
  const outSavings = document.getElementById('calcOutSavings');
  const bookEstimateBtn = document.getElementById('calcBookBtn');

  const OPERATION_RATES = {
    plough: {
      name: "Mahindra 575 DI (45 HP) + 3-MB Plough",
      equipId: "tr-575",
      hoursPerAcre: 1.0,
      hourlyRate: 800,
      fuelPerAcre: 5.5,
      manualCostPerAcre: 2200
    },
    rotavate: {
      name: "Mahindra 575 DI (45 HP) + 6ft Rotavator",
      equipId: "rot-48",
      hoursPerAcre: 0.8,
      hourlyRate: 750,
      fuelPerAcre: 4.8,
      manualCostPerAcre: 1800
    },
    seeding: {
      name: "John Deere 5310 (4WD) + Happy Seeder",
      equipId: "seed-super",
      hoursPerAcre: 0.75,
      hourlyRate: 1000,
      fuelPerAcre: 4.2,
      manualCostPerAcre: 2000
    },
    spraying: {
      name: "Sonalika GT 22 (Mini) + 500L Sprayer",
      equipId: "spray-500",
      hoursPerAcre: 0.25,
      hourlyRate: 630,
      fuelPerAcre: 1.5,
      manualCostPerAcre: 900
    },
    harvest: {
      name: "Preet 987 Multi-Crop Combine Harvester",
      equipId: "harv-9000",
      hoursPerAcre: 0.28,
      hourlyRate: 2200,
      fuelPerAcre: 6.0,
      manualCostPerAcre: 4500
    },
    transport: {
      name: "Mahindra 575 DI + 8-Tonne Hydraulic Trailer",
      equipId: "trail-8t",
      hoursPerAcre: 0.5,
      hourlyRate: 720,
      fuelPerAcre: 3.0,
      manualCostPerAcre: 1500
    }
  };

  function updateEstimator() {
    if (!operationSelect || !acreageSlider) return;

    const opKey = operationSelect.value || 'plough';
    const acres = parseInt(acreageSlider.value) || 5;
    const withOperator = operatorCheckbox ? operatorCheckbox.checked : true;
    const withFuel = fuelCheckbox ? fuelCheckbox.checked : false;

    const op = OPERATION_RATES[opKey] || OPERATION_RATES.plough;
    const totalHours = Math.max(1, Math.round(acres * op.hoursPerAcre * 10) / 10);
    const baseCost = Math.round(totalHours * op.hourlyRate);
    const operatorCost = withOperator ? Math.round(totalHours * 120) : 0;
    const fuelLiters = Math.round(acres * op.fuelPerAcre);
    const fuelCost = withFuel ? Math.round(fuelLiters * 92) : 0;

    const totalCost = baseCost + operatorCost + fuelCost;
    const manualTotal = acres * op.manualCostPerAcre;
    const savings = Math.max(500, manualTotal - totalCost);

    if (acreageDisplay) acreageDisplay.textContent = `${acres} ${acres === 1 ? 'Acre' : 'Acres'}`;
    if (outMachine) outMachine.textContent = op.name;
    if (outHours) outHours.textContent = `~${totalHours} Hours`;
    if (outCost) outCost.textContent = `₹${totalCost.toLocaleString('en-IN')}`;
    if (outFuel) outFuel.textContent = `~${fuelLiters} Liters`;
    if (outSavings) outSavings.textContent = `Save approx. ₹${savings.toLocaleString('en-IN')} vs manual labour`;
    if (bookEstimateBtn) bookEstimateBtn.href = `booking.html?id=${op.equipId}&acres=${acres}&operator=${withOperator ? 1 : 0}`;
  }

  if (operationSelect) operationSelect.addEventListener('change', updateEstimator);
  if (acreageSlider) acreageSlider.addEventListener('input', updateEstimator);
  if (operatorCheckbox) operatorCheckbox.addEventListener('change', updateEstimator);
  if (fuelCheckbox) fuelCheckbox.addEventListener('change', updateEstimator);

  updateEstimator();

  // 3. FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const header = item.querySelector('.faq-header');
    if (header) {
      header.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isActive) {
          item.classList.add('active');
        }
      });
    }
  });
});
