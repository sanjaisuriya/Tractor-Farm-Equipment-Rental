with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Find the form container
# `<div class="lg:col-span-7 bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 sm:p-8 shadow-sm">\s*<form id="equipmentBookingForm"`
old_form_start = '<div class="lg:col-span-7 bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 sm:p-8 shadow-sm">\n          <form id="equipmentBookingForm"'
new_form_start = '<div class="lg:col-span-7 space-y-6">\n          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 sm:p-8 shadow-sm">\n          <form id="equipmentBookingForm"'

if old_form_start in html:
    html = html.replace(old_form_start, new_form_start, 1)
    print("Replaced form start successfully!")
else:
    print("Could not find old_form_start!")

# Find the form end and add the two new cards before the closing of lg:col-span-7
old_form_end = """              <button type="submit" class="btn-primary w-full py-4 text-base font-bold justify-center shadow-lg">
                <i class="fa-solid fa-check-circle"></i> Confirm Machinery Booking
              </button>
              <p class="text-[11px] text-center text-muted mt-2">
                By booking, you agree to AgroRent standard farm machinery terms & instant deposit refund policy.
              </p>
            </div>

          </form>
        </div>"""

new_cards = """              <button type="submit" class="btn-primary w-full py-4 text-base font-bold justify-center shadow-lg">
                <i class="fa-solid fa-check-circle"></i> Confirm Machinery Booking
              </button>
              <p class="text-[11px] text-center text-muted mt-2">
                By booking, you agree to AgroRent standard farm machinery terms & instant deposit refund policy.
              </p>
            </div>

          </form>
        </div>

        <!-- Farmer Pre-Handover Checklist & Simple Verification -->
        <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 sm:p-7 shadow-sm">
          <div class="flex items-center justify-between pb-3 mb-4 border-b border-slate-100 dark:border-slate-700">
            <h4 class="font-bold text-base text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-clipboard-check text-agri"></i> Field Handover & Simple Verification
            </h4>
            <span class="text-[11px] font-bold text-agri bg-green-50 dark:bg-green-900/30 px-2.5 py-1 rounded-md">Zero Paperwork Delay</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
            <div class="flex items-start gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60">
              <div class="w-8 h-8 rounded-lg bg-green-100 dark:bg-green-900/40 text-agri flex items-center justify-center shrink-0 font-bold text-xs mt-0.5">
                1
              </div>
              <div>
                <strong class="text-slate-900 dark:text-white block font-bold mb-0.5">Simple ID Verification</strong>
                <p class="text-muted leading-relaxed">Present any valid photo ID (Aadhaar, Voter ID, or Kisan Credit Card) during doorstep delivery.</p>
              </div>
            </div>

            <div class="flex items-start gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60">
              <div class="w-8 h-8 rounded-lg bg-green-100 dark:bg-green-900/40 text-agri flex items-center justify-center shrink-0 font-bold text-xs mt-0.5">
                2
              </div>
              <div>
                <strong class="text-slate-900 dark:text-white block font-bold mb-0.5">Joint Machine Inspection</strong>
                <p class="text-muted leading-relaxed">Check fuel levels, digital hour meter reading, and implement attachment with our delivery pilot.</p>
              </div>
            </div>

            <div class="flex items-start gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60">
              <div class="w-8 h-8 rounded-lg bg-green-100 dark:bg-green-900/40 text-agri flex items-center justify-center shrink-0 font-bold text-xs mt-0.5">
                3
              </div>
              <div>
                <strong class="text-slate-900 dark:text-white block font-bold mb-0.5">Pay on Field Delivery</strong>
                <p class="text-muted leading-relaxed">Pay rental balance via UPI, cash, or bank transfer only after inspecting the machine in your field.</p>
              </div>
            </div>

            <div class="flex items-start gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60">
              <div class="w-8 h-8 rounded-lg bg-green-100 dark:bg-green-900/40 text-agri flex items-center justify-center shrink-0 font-bold text-xs mt-0.5">
                4
              </div>
              <div>
                <strong class="text-slate-900 dark:text-white block font-bold mb-0.5">4-Hour Deposit Return</strong>
                <p class="text-muted leading-relaxed">Security deposit credited straight to your UPI / bank account within 4 hours of post-work collection.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Flexible Farmer Payment Options -->
        <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 sm:p-7 shadow-sm">
          <div class="flex items-center justify-between pb-3 mb-4 border-b border-slate-100 dark:border-slate-700">
            <h4 class="font-bold text-base text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-credit-card text-agri"></i> Flexible Farmer Payment Methods
            </h4>
            <span class="text-[11px] font-bold text-slate-600 dark:text-slate-400 flex items-center gap-1">
              <i class="fa-solid fa-lock text-agri"></i> 100% Secure
            </span>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60 flex flex-col items-center">
              <div class="w-10 h-10 rounded-full bg-blue-50 dark:bg-blue-900/30 text-blue-600 flex items-center justify-center text-lg mb-2">
                <i class="fa-brands fa-google-pay"></i>
              </div>
              <strong class="text-xs font-bold text-slate-900 dark:text-white">UPI & GPay</strong>
              <span class="text-[10px] text-muted mt-0.5">Instant 0-Fee</span>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60 flex flex-col items-center">
              <div class="w-10 h-10 rounded-full bg-purple-50 dark:bg-purple-900/30 text-purple-600 flex items-center justify-center text-lg mb-2">
                <i class="fa-solid fa-mobile-screen-button"></i>
              </div>
              <strong class="text-xs font-bold text-slate-900 dark:text-white">PhonePe / Paytm</strong>
              <span class="text-[10px] text-muted mt-0.5">Quick Scan</span>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60 flex flex-col items-center">
              <div class="w-10 h-10 rounded-full bg-emerald-50 dark:bg-emerald-900/30 text-emerald-600 flex items-center justify-center text-lg mb-2">
                <i class="fa-solid fa-id-card"></i>
              </div>
              <strong class="text-xs font-bold text-slate-900 dark:text-white">KCC Billing</strong>
              <span class="text-[10px] text-muted mt-0.5">Crop Flexi-Credit</span>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/40 border border-slate-100 dark:border-slate-700/60 flex flex-col items-center">
              <div class="w-10 h-10 rounded-full bg-amber-50 dark:bg-amber-900/30 text-amber-600 flex items-center justify-center text-lg mb-2">
                <i class="fa-solid fa-building-columns"></i>
              </div>
              <strong class="text-xs font-bold text-slate-900 dark:text-white">Bank Transfer</strong>
              <span class="text-[10px] text-muted mt-0.5">NEFT / RTGS</span>
            </div>
          </div>

          <p class="text-[11px] text-muted text-center mt-3 pt-3 border-t border-slate-100 dark:border-slate-700/60">
            * Payment is required only upon machine arrival and test-run in your field. Official GST e-invoice issued immediately.
          </p>
        </div>
      </div>"""

if old_form_end in html:
    html = html.replace(old_form_end, new_cards, 1)
    print("Added new cards to left column successfully!")
else:
    print("Could not find old_form_end!")

with open('booking.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated booking.html successfully!")
