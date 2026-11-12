with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_testimonial_block = """          <!-- Verified Farmer Testimonial Card -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-5 shadow-sm">
            <div class="flex items-center gap-2 text-gold text-xs mb-2">
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <span class="text-slate-700 dark:text-slate-300 font-bold ml-1">4.9 / 5</span>
              <span class="text-muted text-[11px]">(1,250+ Farmers)</span>
            </div>
            <p class="text-xs text-slate-600 dark:text-slate-300 italic leading-relaxed mb-3">
              "Rented the Mahindra 575 DI with the 6ft rotavator for 3 days during peak tilling. The machine arrived sharp, driver was skilled, and my security deposit was returned within 2 hours of return inspection."
            </p>
            <div class="flex items-center justify-between text-xs pt-2 border-t border-slate-100 dark:border-slate-700">
              <div class="flex items-center gap-2">
                <div class="w-6 h-6 rounded-full bg-agri/15 text-agri font-bold text-[10px] flex items-center justify-center">
                  GS
                </div>
                <div>
                  <strong class="text-slate-800 dark:text-white block text-[11px]">Gurpreet Singh</strong>
                  <span class="text-muted text-[10px]">Patiala, Punjab (18 Acres)</span>
                </div>
              </div>
              <span class="inline-flex items-center gap-1 text-[10px] font-bold text-agri">
                <i class="fa-solid fa-circle-check"></i> Verified Booking
              </span>
            </div>
          </div>"""

new_testimonial_and_dispatch = """          <!-- Verified Farmer Testimonial Card -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-5 shadow-sm">
            <div class="flex items-center gap-2 text-gold text-xs mb-2">
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <span class="text-slate-700 dark:text-slate-300 font-bold ml-1">4.9 / 5</span>
              <span class="text-muted text-[11px]">(1,250+ Farmers)</span>
            </div>
            <p class="text-xs text-slate-600 dark:text-slate-300 italic leading-relaxed mb-3">
              "Rented the Mahindra 575 DI with the 6ft rotavator for 3 days during peak tilling. The machine arrived sharp, driver was skilled, and my security deposit was returned within 2 hours of return inspection."
            </p>
            <div class="flex items-center justify-between text-xs pt-2 border-t border-slate-100 dark:border-slate-700">
              <div class="flex items-center gap-2">
                <div class="w-6 h-6 rounded-full bg-agri/15 text-agri font-bold text-[10px] flex items-center justify-center">
                  GS
                </div>
                <div>
                  <strong class="text-slate-800 dark:text-white block text-[11px]">Gurpreet Singh</strong>
                  <span class="text-muted text-[10px]">Patiala, Punjab (18 Acres)</span>
                </div>
              </div>
              <span class="inline-flex items-center gap-1 text-[10px] font-bold text-agri">
                <i class="fa-solid fa-circle-check"></i> Verified Booking
              </span>
            </div>
          </div>

          <!-- Live Dispatch & Delivery Updates Card (Fills Bottom Right Gap) -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-5 shadow-sm">
            <div class="flex items-center justify-between pb-2.5 mb-3 border-b border-slate-100 dark:border-slate-700">
              <h4 class="font-bold text-xs uppercase tracking-wider text-slate-900 dark:text-white flex items-center gap-2">
                <i class="fa-solid fa-location-dot text-agri"></i> Live Dispatch & Delivery Updates
              </h4>
              <span class="text-[10px] font-bold text-agri bg-green-50 dark:bg-green-900/30 px-2 py-0.5 rounded">Real-Time SMS</span>
            </div>

            <div class="space-y-2.5 text-xs text-slate-600 dark:text-slate-300">
              <div class="flex items-start gap-2.5">
                <i class="fa-solid fa-comment-sms text-agri mt-0.5 shrink-0 text-sm"></i>
                <p class="leading-relaxed">
                  <strong class="text-slate-900 dark:text-white font-semibold">Instant SMS Confirmation:</strong> Booking ID, assigned tractor driver name & phone number sent immediately.
                </p>
              </div>

              <div class="flex items-start gap-2.5">
                <i class="fa-solid fa-truck-ramp-box text-agri mt-0.5 shrink-0 text-sm"></i>
                <p class="leading-relaxed">
                  <strong class="text-slate-900 dark:text-white font-semibold">Doorstep Field Tracking:</strong> Live dispatch alert when flatbed carrier leaves rural machinery yard with your tractor.
                </p>
              </div>

              <div class="flex items-start gap-2.5">
                <i class="fa-solid fa-gauge-high text-agri mt-0.5 shrink-0 text-sm"></i>
                <p class="leading-relaxed">
                  <strong class="text-slate-900 dark:text-white font-semibold">GPS Hour-Meter Billing:</strong> Transparent start/stop engine hours logged digitally on farmer portal.
                </p>
              </div>
            </div>
          </div>"""

if old_testimonial_block in html:
    html = html.replace(old_testimonial_block, new_testimonial_and_dispatch, 1)
    with open('booking.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added Live Dispatch Card to booking.html successfully!")
else:
    print("Could not find old_testimonial_block!")
