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
      rateTabs.forEach(t => {
        t.classList.remove('active', 'bg-agri', 'text-white', 'shadow-md', 'bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-200');
        t.classList.add('text-white/80', 'hover:text-white');
      });

      tab.classList.remove('text-white/80', 'bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-200');
      tab.classList.add('active', 'bg-agri', 'text-white', 'shadow-md');

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

      // Highlight corresponding card if present
      const cards = document.querySelectorAll('.pricing-card[data-card-period]');
      cards.forEach(card => {
        if (card.getAttribute('data-card-period') === period) {
          card.classList.add('ring-2', 'ring-agri', 'dark:ring-fresh');
        } else {
          card.classList.remove('ring-2', 'ring-agri', 'dark:ring-fresh');
        }
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
  const calcCostLabel = document.getElementById('calcCostLabel');
  const calcInclusionBadge = document.getElementById('calcInclusionBadge');
  const calcInclusionExplain = document.getElementById('calcInclusionExplain');
  const bookEstimateBtn = document.getElementById('calcBookBtn');

  const OPERATION_RATES = {
    plough: {
      name: "Mahindra 575 DI (45 HP) + 3-MB Plough",
      equipId: "tr-575",
      hoursPerAcre: 1.0,
      hourlyRate: 800,
      fuelPerAcre: 5.5,
      driverRatePerHour: 100, // ₹700-800/day utility operator
      driverIncluded: false,
      manualCostPerAcre: 2200
    },
    rotavate: {
      name: "Mahindra 575 DI (45 HP) + 6ft Rotavator",
      equipId: "rot-48",
      hoursPerAcre: 0.8,
      hourlyRate: 750,
      fuelPerAcre: 4.8,
      driverRatePerHour: 100,
      driverIncluded: false,
      manualCostPerAcre: 1800
    },
    seeding: {
      name: "John Deere 5310 (4WD) + Happy Seeder",
      equipId: "seed-super",
      hoursPerAcre: 0.75,
      hourlyRate: 1000,
      fuelPerAcre: 4.2,
      driverRatePerHour: 100,
      driverIncluded: false,
      manualCostPerAcre: 2000
    },
    spraying: {
      name: "Sonalika GT 22 (Mini) + 500L Sprayer",
      equipId: "spray-500",
      hoursPerAcre: 0.25,
      hourlyRate: 630,
      fuelPerAcre: 1.5,
      driverRatePerHour: 75, // ₹600/day mini tractor operator
      driverIncluded: false,
      manualCostPerAcre: 900
    },
    harvest: {
      name: "Preet 987 Multi-Crop Combine Harvester",
      equipId: "harv-9000",
      hoursPerAcre: 0.28,
      hourlyRate: 2200,
      fuelPerAcre: 6.0,
      driverRatePerHour: 0, // Included Master Pilot
      driverIncluded: true,
      manualCostPerAcre: 4500
    },
    transport: {
      name: "Mahindra 575 DI + 8-Tonne Hydraulic Trailer",
      equipId: "trail-8t",
      hoursPerAcre: 0.5,
      hourlyRate: 720,
      fuelPerAcre: 3.0,
      driverRatePerHour: 100,
      driverIncluded: false,
      manualCostPerAcre: 1500
    }
  };

  function updateEstimator() {
    if (!operationSelect || !acreageSlider) return;

    const opKey = operationSelect.value || 'plough';
    const acres = parseInt(acreageSlider.value) || 5;
    const op = OPERATION_RATES[opKey] || OPERATION_RATES.plough;

    // Harvester always includes Master Pilot
    if (op.driverIncluded) {
      if (operatorCheckbox) {
        operatorCheckbox.checked = true;
        operatorCheckbox.disabled = true;
      }
    } else {
      if (operatorCheckbox) {
        operatorCheckbox.disabled = false;
      }
    }

    const withOperator = operatorCheckbox ? operatorCheckbox.checked : true;
    const withFuel = fuelCheckbox ? fuelCheckbox.checked : false;

    const totalHours = Math.max(1, Math.round(acres * op.hoursPerAcre * 10) / 10);
    const baseCost = Math.round(totalHours * op.hourlyRate);
    
    // Operator calculation
    const operatorCost = (withOperator && !op.driverIncluded) 
      ? Math.round(totalHours * op.driverRatePerHour) 
      : 0;

    // Fuel calculation (₹92/liter agricultural diesel)
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
    
    // Dynamic Inclusions & Cost Labels
    if (calcCostLabel) {
      if (op.driverIncluded && withFuel) {
        calcCostLabel.textContent = 'incl. master pilot & fuel';
      } else if (op.driverIncluded) {
        calcCostLabel.textContent = 'incl. master pilot';
      } else if (withOperator && withFuel) {
        calcCostLabel.textContent = 'incl. driver & fuel';
      } else if (withOperator) {
        calcCostLabel.textContent = 'incl. driver';
      } else if (withFuel) {
        calcCostLabel.textContent = 'incl. fuel (bare machine)';
      } else {
        calcCostLabel.textContent = 'bare machine only';
      }
    }

    if (calcInclusionBadge) {
      if (op.driverIncluded && withFuel) {
        calcInclusionBadge.textContent = 'Harvester + Master Pilot Included + Diesel Fuel Covered';
      } else if (op.driverIncluded) {
        calcInclusionBadge.textContent = 'Harvester + Master Pilot Included | Diesel Excluded';
      } else if (withOperator && withFuel) {
        calcInclusionBadge.textContent = 'Machine + Driver + Diesel Fuel 100% Included';
      } else if (withOperator) {
        calcInclusionBadge.textContent = 'Machine + Driver Included | Diesel Excluded';
      } else if (withFuel) {
        calcInclusionBadge.textContent = 'Bare Machine + Diesel Fuel Included | Driver Excluded';
      } else {
        calcInclusionBadge.textContent = 'Bare Machine Only | Fuel & Driver Excluded';
      }
    }

    if (calcInclusionExplain) {
      if (op.driverIncluded && withFuel) {
        calcInclusionExplain.textContent = 'Complete turnkey harvesting: Preet 987 Harvester, certified master pilot, and pre-filled diesel fuel all included.';
      } else if (op.driverIncluded) {
        calcInclusionExplain.textContent = 'Machine + Certified Harvester Master Pilot included in base tariff. Diesel fuel is farmer-supplied or billed at ₹92/L.';
      } else if (withOperator && withFuel) {
        calcInclusionExplain.textContent = 'Complete turnkey package: Equipment, certified operator, and diesel fuel all covered with zero extra fees.';
      } else if (withOperator) {
        calcInclusionExplain.textContent = 'Machine + Certified Driver included. Diesel fuel is excluded (farmer supplied or pre-filled on demand at ₹92/L).';
      } else if (withFuel) {
        calcInclusionExplain.textContent = 'Bare machine rental with pre-filled diesel fuel. Farmer provides their own certified tractor driver.';
      } else {
        calcInclusionExplain.textContent = 'Base machine rental only. Certified driver and diesel fuel are to be supplied by the farmer.';
      }
    }

    if (bookEstimateBtn) {
      bookEstimateBtn.href = `booking.html?id=${op.equipId}&acres=${acres}&operator=${withOperator ? 1 : 0}&fuel=${withFuel ? 1 : 0}`;
    }
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
