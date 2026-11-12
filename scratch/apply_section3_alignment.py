import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Card 1, 2, 3, 4 markup in Section 3
old_sec3_pattern = r'(<!-- Card 1: Hourly Flexible -->.*?</div>\s*<!-- Card 2: Standard Daily Rental.*?</div>\s*<!-- Card 3: Weekly Rental Plan.*?</div>\s*<!-- Card 4: Monthly Season Pass.*?</div>\s*</div>)'

# Let's locate the exact grid container inside Section 3
grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 lg:gap-8 items-stretch">)(.*?)(</div>\s*</div>\s*</section>)', html, re.DOTALL)

if not grid_match:
    print("Grid container in Section 3 not found directly! Searching...")
    # let's find pricingPlans
    sec3 = re.search(r'id="pricingPlans".*?</section>', html, re.DOTALL)
    print("Found sec3 length:", len(sec3.group(0)) if sec3 else 0)

new_cards_html = """          <!-- Card 1: Hourly Flexible -->
          <div class="pricing-card reveal-on-scroll" data-card-period="hourly">
            <div class="pricing-img-wrapper">
              <img 
                src="assets/images/pricing/plan-hourly-tractor.jpg" 
                alt="Indian tractor operating in an agricultural field" 
                loading="lazy" 
              />
              <span class="absolute bottom-2 left-2 px-2.5 py-1 rounded-md bg-forest/85 backdrop-blur-md text-white text-[11px] font-semibold flex items-center gap-1 shadow-sm">
                <i class="fa-solid fa-clock text-gold"></i> Short Tasks
              </span>
            </div>

            <div class="pricing-card-header">
              <span class="text-[11px] font-bold uppercase tracking-wider text-muted mb-1 block">Quick Field Tasks</span>
              <h3 class="text-xl font-black text-slate-900 dark:text-white font-heading">Hourly Flexible</h3>
              <p class="pricing-card-desc text-muted mt-1 leading-relaxed">
                Ideal for quick field tasks, small acreage tilling, canal irrigation pumping, and short harvest haulage runs.
              </p>
            </div>

            <div class="pricing-price-block">
              <div class="flex items-baseline gap-1.5">
                <span class="text-3xl sm:text-4xl font-black text-agri dark:text-fresh font-heading dynamic-price-value" data-hourly="450" data-daily="3200" data-weekly="19000" data-monthly="65000">₹450</span>
                <span class="text-xs font-bold text-muted dynamic-period-label">/ hour</span>
              </div>
              <span class="pricing-price-note text-muted">Starting from ₹350/hr • 2-hour minimum</span>
            </div>

            <ul class="pricing-features text-slate-700 dark:text-slate-300">
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Fleet Access:</strong> 22 - 50 HP field-tested diesel tractors</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>GPS Hour Meter:</strong> Pay strictly for running engine hours</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Attachment Pairing:</strong> Add ploughs, rotavators, or pumps</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Driver On-Demand:</strong> Optional certified driver (+₹100/hr)</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Zero Surge Tariff:</strong> Transparent, locked rate year-round</span>
              </li>
            </ul>

            <a href="booking.html?plan=hourly" class="btn-secondary w-full justify-center text-xs py-3 font-bold mt-auto shadow-sm">
              Book Now
            </a>
          </div>

          <!-- Card 2: Standard Daily Rental (Featured) -->
          <div class="pricing-card featured reveal-on-scroll" style="transition-delay: 0.1s;" data-card-period="daily">
            <span class="pricing-badge-popular">MOST POPULAR</span>

            <div class="pricing-img-wrapper">
              <img 
                src="assets/images/pricing/plan-daily-rotavator.jpg" 
                alt="Tractor with attached rotavator tilling soil" 
                loading="lazy" 
              />
              <span class="absolute bottom-2 left-2 px-2.5 py-1 rounded-md bg-forest/85 backdrop-blur-md text-white text-[11px] font-semibold flex items-center gap-1 shadow-sm">
                <i class="fa-solid fa-gear text-gold"></i> Full Shift
              </span>
            </div>

            <div class="pricing-card-header">
              <span class="text-[11px] font-bold uppercase tracking-wider text-agri dark:text-fresh font-extrabold mb-1 block">Full-Day Cultivation</span>
              <h3 class="text-xl font-black text-slate-900 dark:text-white font-heading">Standard Daily Rental</h3>
              <p class="pricing-card-desc text-muted mt-1 leading-relaxed">
                Full 8-hour field shift for primary ploughing, rotary tilling, laser levelling, or multi-field operations.
              </p>
            </div>

            <div class="pricing-price-block">
              <div class="flex items-baseline gap-1.5">
                <span class="text-3xl sm:text-4xl font-black text-agri dark:text-fresh font-heading dynamic-price-value" data-hourly="500" data-daily="3500" data-weekly="21000" data-monthly="75000">₹3,500</span>
                <span class="text-xs font-bold text-muted dynamic-period-label">/ day</span>
              </div>
              <span class="pricing-price-note text-agri dark:text-fresh font-semibold">Full 8-hour shift • Free delivery &lt;10km</span>
            </div>

            <ul class="pricing-features text-slate-700 dark:text-slate-300">
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>High-Torque Power:</strong> 45 - 55 HP Mahindra / Swaraj diesel</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Free Farm Transit:</strong> 100% free delivery within 10 km</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Midday Implement Swap:</strong> Switch tools at our local hub</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Breakdown Guarantee:</strong> 2-hr replacement van support</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Clean Fuel Tank:</strong> Pre-tested, water-free diesel certified</span>
              </li>
            </ul>

            <a href="booking.html?plan=daily" class="btn-primary w-full justify-center text-xs py-3 font-bold mt-auto shadow-md">
              Book Daily Pass
            </a>
          </div>

          <!-- Card 3: Weekly Rental Plan -->
          <div class="pricing-card reveal-on-scroll" style="transition-delay: 0.2s;" data-card-period="weekly">
            <div class="pricing-img-wrapper">
              <img 
                src="assets/images/pricing/plan-weekly-harvester.jpg" 
                alt="Combine harvester working in a paddy field" 
                loading="lazy" 
              />
              <span class="absolute bottom-2 left-2 px-2.5 py-1 rounded-md bg-forest/85 backdrop-blur-md text-white text-[11px] font-semibold flex items-center gap-1 shadow-sm">
                <i class="fa-solid fa-calendar-week text-gold"></i> Save 15%
              </span>
            </div>

            <div class="pricing-card-header">
              <span class="text-[11px] font-bold uppercase tracking-wider text-agri dark:text-fresh font-extrabold mb-1 block">Save 15% Bundled</span>
              <h3 class="text-xl font-black text-slate-900 dark:text-white font-heading">Weekly Rental Plan</h3>
              <p class="pricing-card-desc text-muted mt-1 leading-relaxed">
                Multi-day continuous farming pass for intensive sowing windows, complete village acreage, or harvest cycles.
              </p>
            </div>

            <div class="pricing-price-block">
              <div class="flex items-baseline gap-1.5">
                <span class="text-3xl sm:text-4xl font-black text-agri dark:text-fresh font-heading dynamic-price-value" data-hourly="2800" data-daily="3200" data-weekly="19500" data-monthly="75000">₹19,500</span>
                <span class="text-xs font-bold text-muted dynamic-period-label">/ week</span>
              </div>
              <span class="pricing-price-note text-agri dark:text-fresh font-semibold">15% discount applied • 7 continuous days</span>
            </div>

            <ul class="pricing-features text-slate-700 dark:text-slate-300">
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>7 Consecutive Days:</strong> 56 total field operating hours</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Cost Savings:</strong> ₹5,000 lower than single-day billing</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Weekend Priority:</strong> Guaranteed machinery availability</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Dedicated Mechanic:</strong> Standby maintenance technician</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Free Transit:</strong> Low-bed trailer farm delivery included</span>
              </li>
            </ul>

            <a href="booking.html?plan=weekly" class="btn-secondary w-full justify-center text-xs py-3 font-bold mt-auto shadow-sm">
              Book Now
            </a>
          </div>

          <!-- Card 4: Monthly Season Pass -->
          <div class="pricing-card reveal-on-scroll" style="transition-delay: 0.3s;" data-card-period="monthly">
            <div class="pricing-img-wrapper">
              <img 
                src="assets/images/pricing/plan-monthly-fleet.jpg" 
                alt="Multiple tractors and agricultural machinery fleet" 
                loading="lazy" 
              />
              <span class="absolute bottom-2 left-2 px-2.5 py-1 rounded-md bg-forest/85 backdrop-blur-md text-white text-[11px] font-semibold flex items-center gap-1 shadow-sm">
                <i class="fa-solid fa-boxes-stacked text-gold"></i> Full Fleet
              </span>
            </div>

            <div class="pricing-card-header">
              <span class="text-[11px] font-bold uppercase tracking-wider text-yellow-800 dark:text-gold mb-1 block">Complete Season Pass</span>
              <h3 class="text-xl font-black text-slate-900 dark:text-white font-heading">Monthly Season Pass</h3>
              <p class="pricing-card-desc text-muted mt-1 leading-relaxed">
                Dedicated on-farm machinery deployment for full crop season management without ownership costs.
              </p>
            </div>

            <div class="pricing-price-block">
              <div class="flex items-baseline gap-1.5">
                <span class="text-3xl sm:text-4xl font-black text-agri dark:text-fresh font-heading dynamic-price-value" data-hourly="1100" data-daily="7500" data-weekly="45000" data-monthly="65000">₹65,000</span>
                <span class="text-xs font-bold text-muted dynamic-period-label">/ month</span>
              </div>
              <span class="pricing-price-note text-yellow-800 dark:text-gold font-semibold">Unlimited tool swaps • Post-harvest KCC</span>
            </div>

            <ul class="pricing-features text-slate-700 dark:text-slate-300">
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>30-Day Deployment:</strong> Parked directly at your farmhouse</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Free Implement Swaps:</strong> Ploughs, rotavator, seeder, trolley</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Zero Deposit:</strong> No security deposit for verified FPOs</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Fortnightly Service:</strong> Regular lubrication & maintenance</span>
              </li>
              <li>
                <i class="fa-solid fa-circle-check text-agri"></i>
                <span><strong>Post-Harvest Pay:</strong> Flexible credit settlement options</span>
              </li>
            </ul>

            <a href="booking.html?plan=monthly" class="btn-secondary w-full justify-center text-xs py-3 font-bold mt-auto shadow-sm">
              Book Now
            </a>
          </div>
"""

prefix = grid_match.group(1)
suffix = grid_match.group(3)

new_html = html[:grid_match.start(2)] + "\n" + new_cards_html + "\n        " + html[grid_match.end(2):]

with open('rates-pricing.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated rates-pricing.html Section 3 successfully!")
