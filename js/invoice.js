/**
 * Tractor & Farm Equipment Rental - Invoice Generator & Printing System
 */

const InvoiceManager = {
  getBooking(bookingId) {
    const bookings = JSON.parse(localStorage.getItem('trarent_bookings') || '[]');
    return bookings.find(b => b.id === bookingId) || bookings[0];
  },

  renderModal(bookingId) {
    const booking = this.getBooking(bookingId);
    if (!booking) return;

    const modal = document.getElementById('invoiceModal');
    if (!modal) return;

    const invoiceContainer = document.getElementById('invoicePrintArea');
    if (!invoiceContainer) return;

    invoiceContainer.innerHTML = `
      <div class="p-8 bg-white text-slate-800">
        <!-- Invoice Header -->
        <div class="flex items-start justify-between border-b pb-6 mb-6">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-forest flex items-center justify-center text-white text-2xl font-black">
              <i class="fa-solid fa-tractor"></i>
            </div>
            <div>
              <h1 class="text-2xl font-black text-forest">AGRORENT</h1>
              <p class="text-xs text-slate-500">Tractor & Farm Equipment Rental Platform</p>
              <p class="text-xs text-slate-500">GSTIN: 03AABCA1234F1Z6 | Reg: PB-LUD-2024</p>
            </div>
          </div>
          <div class="text-right">
            <span class="inline-block px-3 py-1 bg-green-100 text-green-800 rounded-full font-bold text-xs uppercase tracking-wider mb-1">
              PAID TAX INVOICE
            </span>
            <p class="text-sm font-bold text-slate-700">Invoice #: INV-${booking.id}</p>
            <p class="text-xs text-slate-500">Booking ID: ${booking.id}</p>
            <p class="text-xs text-slate-500">Date: ${booking.invoiceDate || booking.bookingDate}</p>
          </div>
        </div>

        <!-- Farmer & Rental Info -->
        <div class="grid grid-cols-2 gap-6 mb-8 text-sm">
          <div>
            <h4 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Billed To (Farmer):</h4>
            <p class="font-bold text-slate-900 text-base">${booking.farmerName}</p>
            <p class="text-slate-600"><i class="fa-solid fa-phone text-xs mr-1"></i> ${booking.mobile}</p>
            <p class="text-slate-600"><i class="fa-solid fa-envelope text-xs mr-1"></i> ${booking.email}</p>
            <p class="text-slate-600"><i class="fa-solid fa-location-dot text-xs mr-1"></i> ${booking.location}</p>
          </div>
          <div>
            <h4 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Machinery & Period:</h4>
            <p class="font-bold text-slate-900 text-base">${booking.equipmentName}</p>
            <p class="text-slate-600">Category: <span class="font-medium">${booking.equipmentCategory}</span></p>
            <p class="text-slate-600">Period: <span class="font-medium">${booking.startDate}</span> to <span class="font-medium">${booking.endDate}</span></p>
            <p class="text-slate-600">Duration: <span class="font-bold text-forest">${booking.durationDays} Days</span></p>
          </div>
        </div>

        <!-- Line Items Table -->
        <table class="w-full text-left text-sm border-collapse mb-6">
          <thead>
            <tr class="bg-slate-100 text-slate-600 uppercase text-xs">
              <th class="p-3 font-semibold">Description</th>
              <th class="p-3 font-semibold text-center">Qty / Days</th>
              <th class="p-3 font-semibold text-right">Rate</th>
              <th class="p-3 font-semibold text-right">Amount (₹)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
            <tr>
              <td class="p-3">
                <p class="font-bold text-slate-800">${booking.equipmentName} Rental</p>
                <p class="text-xs text-slate-500">Farm machinery lease with standard maintenance coverage</p>
              </td>
              <td class="p-3 text-center">${booking.durationDays} Days</td>
              <td class="p-3 text-right">₹${Math.round(booking.baseCost / (booking.durationDays || 1)).toLocaleString('en-IN')}</td>
              <td class="p-3 text-right font-medium">₹${booking.baseCost.toLocaleString('en-IN')}</td>
            </tr>
            ${booking.hasOperator ? `
            <tr>
              <td class="p-3">
                <p class="font-bold text-slate-800">Certified Equipment Operator Charges</p>
                <p class="text-xs text-slate-500">Skilled tractor driver & implement specialist</p>
              </td>
              <td class="p-3 text-center">${booking.durationDays} Days</td>
              <td class="p-3 text-right">₹${Math.round(booking.operatorCost / (booking.durationDays || 1)).toLocaleString('en-IN')}</td>
              <td class="p-3 text-right font-medium">₹${booking.operatorCost.toLocaleString('en-IN')}</td>
            </tr>` : ''}
            ${booking.hasDelivery ? `
            <tr>
              <td class="p-3">
                <p class="font-bold text-slate-800">Direct Farm Doorstep Transportation</p>
                <p class="text-xs text-slate-500">Low-bed trailer transit to farmer's field</p>
              </td>
              <td class="p-3 text-center">1 Trip</td>
              <td class="p-3 text-right">₹${booking.deliveryCost.toLocaleString('en-IN')}</td>
              <td class="p-3 text-right font-medium">₹${booking.deliveryCost.toLocaleString('en-IN')}</td>
            </tr>` : ''}
            <tr>
              <td class="p-3">
                <p class="font-bold text-slate-800">Refundable Security Deposit</p>
                <p class="text-xs text-slate-500">Refunded instantly upon equipment inspection post-rental</p>
              </td>
              <td class="p-3 text-center">1 Unit</td>
              <td class="p-3 text-right">₹${booking.deposit.toLocaleString('en-IN')}</td>
              <td class="p-3 text-right font-medium">₹${booking.deposit.toLocaleString('en-IN')}</td>
            </tr>
          </tbody>
        </table>

        <!-- Total Breakdown -->
        <div class="flex justify-end mb-8">
          <div class="w-64 space-y-2 text-sm">
            <div class="flex justify-between text-slate-600">
              <span>Subtotal:</span>
              <span class="font-medium">₹${(booking.baseCost + booking.operatorCost + booking.deliveryCost).toLocaleString('en-IN')}</span>
            </div>
            <div class="flex justify-between text-slate-600">
              <span>Security Deposit:</span>
              <span class="font-medium">₹${booking.deposit.toLocaleString('en-IN')}</span>
            </div>
            <div class="flex justify-between text-slate-600">
              <span>GST (Agricultural Exemption):</span>
              <span class="font-medium text-green-600">₹0.00</span>
            </div>
            <div class="border-t pt-2 flex justify-between font-black text-lg text-forest">
              <span>Total Paid:</span>
              <span>₹${booking.totalAmount.toLocaleString('en-IN')}</span>
            </div>
          </div>
        </div>

        <!-- Footer / Terms -->
        <div class="border-t pt-4 text-xs text-slate-500">
          <p class="font-bold text-slate-700 mb-1">Rental Terms & Conditions:</p>
          <ul class="list-disc pl-4 space-y-1">
            <li>Equipment inspected and sanitized prior to field dispatch.</li>
            <li>In case of mechanical breakdown, replacement unit is guaranteed within 3 hours.</li>
            <li>Security deposit will be credited back via UPI / Bank within 24 hours of machinery return.</li>
            <li>For 24/7 Field Support Call: 1800 456 7890 (Toll Free).</li>
          </ul>
        </div>
      </div>
    `;

    modal.classList.add('active');
  },

  print() {
    window.print();
  },

  closeModal() {
    const modal = document.getElementById('invoiceModal');
    if (modal) modal.classList.remove('active');
  }
};

window.InvoiceManager = InvoiceManager;
