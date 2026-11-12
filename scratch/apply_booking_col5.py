with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

old_col5_pattern = r'<!-- Live Price Calculation Summary \(Col 5\) -->\s*<div class="lg:col-span-5">.*?</div>\s*</div>\s*</div>\s*</section>'

col5_match = re.search(r'(<!-- Live Price Calculation Summary \(Col 5\) -->\s*<div class="lg:col-span-5">)(.*?)(</div>\s*</div>\s*</div>\s*</section>)', html, re.DOTALL)

if not col5_match:
    print("Could not match col5 with regex! Searching more broadly...")
    # Find start and end
    start_idx = html.find('<!-- Live Price Calculation Summary (Col 5) -->')
    print("Found start_idx:", start_idx)
    end_idx = html.find('</section>', start_idx)
    print("Found end_idx:", end_idx)
    print("Snippet:")
    print(html[start_idx:end_idx])

new_col5_html = """<!-- Live Price Calculation Summary & Farmer Assurances (Col 5) -->
        <div class="lg:col-span-5 space-y-6">
          
          <!-- Summary Card -->
          <div class="booking-summary-card">
            <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-700 pb-4 mb-4">
              <h3 class="font-bold text-lg text-slate-900 dark:text-white flex items-center gap-2">
                <i class="fa-solid fa-calculator text-agri"></i> Cost Summary
              </h3>
              <span class="badge-agri bg-green-100 text-green-800 text-[10px] font-bold">Live Calculator</span>
            </div>

            <div class="space-y-3 mb-6">
              <div class="summary-row">
                <span class="text-muted">Equipment:</span>
                <strong id="sumEquipName" class="text-slate-800 dark:text-white text-right max-w-[200px] truncate">Mahindra 575 DI</strong>
              </div>
              <div class="summary-row">
                <span class="text-muted">Base Daily Rate:</span>
                <span id="sumRatePerDay" class="font-semibold text-slate-800 dark:text-slate-200">₹3,500</span>
              </div>
              <div class="summary-row">
                <span class="text-muted">Rental Duration:</span>
                <strong id="sumDuration" class="text-agri font-bold">2 Days</strong>
              </div>
              <div class="summary-row">
                <span class="text-muted">Equipment Total:</span>
                <span id="sumEquipCost" class="font-semibold text-slate-800 dark:text-slate-200">₹7,000</span>
              </div>
              <div class="summary-row">
                <span class="text-muted">Operator Charges:</span>
                <span id="sumOperatorCost" class="font-semibold text-slate-800 dark:text-slate-200">₹1,400</span>
              </div>
              <div class="summary-row">
                <span class="text-muted">Farm Transit:</span>
                <span id="sumDeliveryCost" class="font-semibold text-slate-800 dark:text-slate-200">₹450</span>
              </div>
              <div class="summary-row">
                <span class="text-muted">Refundable Deposit:</span>
                <span id="sumDeposit" class="font-semibold text-amber-600 dark:text-amber-400">₹1,400</span>
              </div>
            </div>

            <!-- Grand Total -->
            <div class="pt-4 border-t-2 border-slate-200 dark:border-slate-700 flex items-center justify-between mb-6">
              <div>
                <span class="text-xs uppercase tracking-wider font-bold text-muted block">Estimated Total</span>
                <span class="text-[10px] text-green-600 font-semibold">(Deposit 100% Refundable)</span>
              </div>
              <span id="sumTotalAmount" class="summary-total">₹10,250</span>
            </div>

            <div class="p-4 bg-cream/50 dark:bg-slate-900/50 rounded-xl text-xs space-y-2 border border-slate-200 dark:border-slate-700">
              <p class="flex items-center gap-2 text-slate-700 dark:text-slate-300">
                <i class="fa-solid fa-shield-halved text-agri"></i> In-Field mechanical breakdown protection
              </p>
              <p class="flex items-center gap-2 text-slate-700 dark:text-slate-300">
                <i class="fa-solid fa-rotate-left text-agri"></i> Instant deposit credit post equipment return
              </p>
              <p class="flex items-center gap-2 text-slate-700 dark:text-slate-300">
                <i class="fa-solid fa-clock text-agri"></i> On-time doorstep field delivery
              </p>
            </div>
          </div>

          <!-- Farmer Guarantees & Assurances Card -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 shadow-sm">
            <h4 class="font-bold text-base text-slate-900 dark:text-white flex items-center gap-2 mb-4 pb-3 border-b border-slate-100 dark:border-slate-700">
              <i class="fa-solid fa-certificate text-gold"></i> AgroRent Farmer Guarantees
            </h4>
            <div class="space-y-4 text-xs">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-green-50 dark:bg-green-900/30 text-agri flex items-center justify-center shrink-0 mt-0.5">
                  <i class="fa-solid fa-wrench"></i>
                </div>
                <div>
                  <strong class="text-slate-900 dark:text-white block text-xs font-bold">50-Point Pre-Delivery Inspection</strong>
                  <p class="text-muted mt-0.5 leading-relaxed">Engine fluids, PTO, hydraulic lift pressure, clutch, and tyre tread tested before field dispatch.</p>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-green-50 dark:bg-green-900/30 text-agri flex items-center justify-center shrink-0 mt-0.5">
                  <i class="fa-solid fa-bolt"></i>
                </div>
                <div>
                  <strong class="text-slate-900 dark:text-white block text-xs font-bold">2-Hour Breakdown Assistance SLA</strong>
                  <p class="text-muted mt-0.5 leading-relaxed">Local mobile mechanic dispatched to your farmland or an instant replacement tractor arranged.</p>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-green-50 dark:bg-green-900/30 text-agri flex items-center justify-center shrink-0 mt-0.5">
                  <i class="fa-solid fa-hand-holding-dollar"></i>
                </div>
                <div>
                  <strong class="text-slate-900 dark:text-white block text-xs font-bold">4-Hour Deposit Refund SLA</strong>
                  <p class="text-muted mt-0.5 leading-relaxed">Security deposit credited straight to your UPI or bank account within 4 hours of hour-meter return inspection.</p>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-green-50 dark:bg-green-900/30 text-agri flex items-center justify-center shrink-0 mt-0.5">
                  <i class="fa-solid fa-shield-halved"></i>
                </div>
                <div>
                  <strong class="text-slate-900 dark:text-white block text-xs font-bold">Transit & Field Insurance Included</strong>
                  <p class="text-muted mt-0.5 leading-relaxed">Comprehensive insurance coverage against road transit and normal agricultural operating wear & tear.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Need Urgent Booking Assistance Card -->
          <div class="bg-gradient-to-br from-[#173D2B] to-[#2D6A4F] text-white rounded-2xl p-6 shadow-md relative overflow-hidden">
            <div class="relative z-10">
              <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/15 text-gold text-[10px] font-bold uppercase tracking-wider mb-2 backdrop-blur-sm">
                <i class="fa-solid fa-phone-volume"></i> Rural Support Desk
              </span>
              <h4 class="font-bold text-base text-white mb-1.5">Need Booking Assistance?</h4>
              <p class="text-xs text-white/85 leading-relaxed mb-4">
                Have questions regarding custom implement compatibility, multi-day village discounts, or certified driver scheduling? Call our agricultural desk directly.
              </p>
              
              <div class="space-y-2.5">
                <a href="tel:+919876543210" class="flex items-center justify-between p-3 rounded-xl bg-white/10 hover:bg-white/20 transition text-xs font-bold text-white border border-white/10">
                  <span class="flex items-center gap-2">
                    <i class="fa-solid fa-phone text-gold"></i>
                    <span>Toll-Free Helpline</span>
                  </span>
                  <span class="font-mono text-gold">+91 98765 43210</span>
                </a>
                
                <a href="https://wa.me/919876543210" target="_blank" rel="noopener noreferrer" class="flex items-center justify-between p-3 rounded-xl bg-[#25D366]/20 hover:bg-[#25D366]/30 transition text-xs font-bold text-white border border-[#25D366]/30">
                  <span class="flex items-center gap-2">
                    <i class="fa-brands fa-whatsapp text-[#25D366] text-sm"></i>
                    <span>WhatsApp Booking Desk</span>
                  </span>
                  <span class="text-white/80 font-medium">Quick Reply &rarr;</span>
                </a>
              </div>

              <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-white/70">
                <span><i class="fa-regular fa-clock mr-1 text-gold"></i> 6:00 AM – 9:00 PM</span>
                <span>Open All 7 Days</span>
              </div>
            </div>
          </div>

          <!-- Verified Farmer Testimonial Card -->
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

        </div>"""

start_marker = "<!-- Live Price Calculation Summary (Col 5) -->"
start_pos = html.find(start_marker)
end_marker = "</div>\n\n    </div>\n      </section>"
end_pos = html.find(end_marker, start_pos)

if start_pos != -1 and end_pos != -1:
    new_html = html[:start_pos] + new_col5_html + "\n\n      " + html[end_pos:]
    with open('booking.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced Col 5 in booking.html successfully!")
else:
    print("Could not find start/end positions!")
