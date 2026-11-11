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

    const isPending = (booking.pendingAmount || 0) > 0;

    invoiceContainer.innerHTML = `
      <div class="p-6 sm:p-8 bg-white text-slate-800">
        <!-- Invoice Header -->
        <div class="flex items-start justify-between border-b pb-6 mb-6">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-forest flex items-center justify-center text-white text-2xl font-black shadow">
              <i class="fa-solid fa-tractor text-gold"></i>
            </div>
            <div>
              <h1 class="text-2xl font-black text-forest tracking-tight">AGRO<span class="text-agri">RENT</span></h1>
              <p class="text-xs text-slate-500 font-medium">Tractor & Farm Equipment Rental Platform</p>
              <p class="text-[11px] text-slate-400">GSTIN: 03AABCA1234F1Z6 | Reg: PB-LUD-2024</p>
            </div>
          </div>
          <div class="text-right">
            <span class="inline-block px-3 py-1 rounded-full font-bold text-xs uppercase tracking-wider mb-1 ${isPending ? 'bg-amber-100 text-amber-800 border border-amber-300' : 'bg-green-100 text-green-800 border border-green-300'}">
              ${isPending ? `PARTIALLY PAID (PENDING: ₹${booking.pendingAmount.toLocaleString('en-IN')})` : 'PAID TAX INVOICE'}
            </span>
            <p class="text-sm font-bold text-slate-800">Invoice #: INV-${booking.id}</p>
            <p class="text-xs text-slate-500">Booking Ref: ${booking.id}</p>
            <p class="text-xs text-slate-500">Date: ${booking.invoiceDate || booking.bookingDate}</p>
          </div>
        </div>

        <!-- Farmer & Rental Info -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-8 text-xs sm:text-sm">
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <h4 class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2 flex items-center gap-1.5">
              <i class="fa-solid fa-user-check text-agri"></i> Billed To (Farmer):
            </h4>
            <p class="font-bold text-slate-900 text-base">${booking.farmerName}</p>
            <p class="text-slate-600"><i class="fa-solid fa-phone text-xs mr-1 text-slate-400"></i> ${booking.mobile}</p>
            <p class="text-slate-600"><i class="fa-solid fa-envelope text-xs mr-1 text-slate-400"></i> ${booking.email}</p>
            <p class="text-slate-600"><i class="fa-solid fa-location-dot text-xs mr-1 text-slate-400"></i> ${booking.location}</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <h4 class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2 flex items-center gap-1.5">
              <i class="fa-solid fa-tractor text-agri"></i> Machinery & Schedule:
            </h4>
            <p class="font-bold text-slate-900 text-base">${booking.equipmentName}</p>
            <p class="text-slate-600">Category: <span class="font-medium">${booking.equipmentCategory}</span></p>
            <p class="text-slate-600">Period: <span class="font-medium">${booking.startDate}</span> to <span class="font-medium">${booking.endDate}</span></p>
            <p class="text-slate-600">Duration: <strong class="text-forest font-bold">${booking.durationDays} Days</strong></p>
          </div>
        </div>

        <!-- Line Items Table -->
        <div class="border border-slate-200 rounded-xl overflow-hidden mb-6">
          <table class="w-full text-left text-xs sm:text-sm border-collapse">
            <thead>
              <tr class="bg-slate-100 text-slate-700 uppercase text-xs font-bold border-b border-slate-200">
                <th class="p-3">Description</th>
                <th class="p-3 text-center">Period</th>
                <th class="p-3 text-right">Daily Rate</th>
                <th class="p-3 text-right">Amount (₹)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200">
              <tr>
                <td class="p-3">
                  <p class="font-bold text-slate-900">${booking.equipmentName}</p>
                  <p class="text-xs text-slate-500">Farm machinery lease with 50-point pre-delivery check</p>
                </td>
                <td class="p-3 text-center font-medium">${booking.durationDays} Days</td>
                <td class="p-3 text-right">₹${Math.round(booking.baseCost / (booking.durationDays || 1)).toLocaleString('en-IN')}</td>
                <td class="p-3 text-right font-bold">₹${booking.baseCost.toLocaleString('en-IN')}</td>
              </tr>
              ${booking.hasOperator ? `
              <tr>
                <td class="p-3">
                  <p class="font-bold text-slate-900">Certified Equipment Operator</p>
                  <p class="text-xs text-slate-500">${booking.operatorName || 'Expert tractor pilot'}</p>
                </td>
                <td class="p-3 text-center font-medium">${booking.durationDays} Days</td>
                <td class="p-3 text-right">₹${Math.round((booking.operatorCost || 0) / (booking.durationDays || 1)).toLocaleString('en-IN')}</td>
                <td class="p-3 text-right font-bold">₹${(booking.operatorCost || 0).toLocaleString('en-IN')}</td>
              </tr>` : ''}
              ${booking.hasDelivery ? `
              <tr>
                <td class="p-3">
                  <p class="font-bold text-slate-900">Farm Gate Transport & Flatbed Transit</p>
                  <p class="text-xs text-slate-500">Depot to farm delivery & retrieval</p>
                </td>
                <td class="p-3 text-center font-medium">1 Trip</td>
                <td class="p-3 text-right">₹${(booking.deliveryCost || 0).toLocaleString('en-IN')}</td>
                <td class="p-3 text-right font-bold">₹${(booking.deliveryCost || 0).toLocaleString('en-IN')}</td>
              </tr>` : ''}
              <tr>
                <td class="p-3">
                  <p class="font-bold text-slate-900">Refundable Security Deposit</p>
                  <p class="text-xs text-slate-500">Credited to farmer bank upon return inspection</p>
                </td>
                <td class="p-3 text-center font-medium">1 Unit</td>
                <td class="p-3 text-right">₹${(booking.deposit || 0).toLocaleString('en-IN')}</td>
                <td class="p-3 text-right font-bold">₹${(booking.deposit || 0).toLocaleString('en-IN')}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Total Breakdown -->
        <div class="flex justify-end mb-8">
          <div class="w-full sm:w-80 space-y-2 text-xs sm:text-sm p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="flex justify-between text-slate-600">
              <span>Machinery Subtotal:</span>
              <span class="font-bold">₹${(booking.baseCost + (booking.operatorCost || 0) + (booking.deliveryCost || 0)).toLocaleString('en-IN')}</span>
            </div>
            <div class="flex justify-between text-slate-600">
              <span>Security Deposit:</span>
              <span class="font-bold">₹${(booking.deposit || 0).toLocaleString('en-IN')}</span>
            </div>
            <div class="flex justify-between text-slate-600">
              <span>GST (Agricultural Service Exemption):</span>
              <span class="font-bold text-green-600">₹0.00 (Exempt)</span>
            </div>
            <div class="border-t border-slate-300 pt-2 flex justify-between font-black text-base text-forest">
              <span>Total Rental Amount:</span>
              <span>₹${booking.totalAmount.toLocaleString('en-IN')}</span>
            </div>
            <div class="flex justify-between text-xs text-green-700 font-semibold pt-1 border-t border-slate-200">
              <span>Amount Paid:</span>
              <span>₹${(booking.paidAmount || booking.totalAmount).toLocaleString('en-IN')}</span>
            </div>
            ${isPending ? `
            <div class="flex justify-between text-xs text-amber-700 font-bold">
              <span>Balance Due:</span>
              <span>₹${booking.pendingAmount.toLocaleString('en-IN')}</span>
            </div>` : ''}
          </div>
        </div>

        <!-- Footer / Terms -->
        <div class="border-t pt-4 text-[11px] text-slate-500 space-y-1">
          <p class="font-bold text-slate-700 mb-1">AgroRent Rental Guarantees & Terms:</p>
          <p>1. Equipment is pre-calibrated and fully insured under AgroRent Field Shield.</p>
          <p>2. In case of mechanical stoppage, standby replacement is dispatched within 3 hours.</p>
          <p>3. Security deposits are automatically refunded to farmer's UPI / account within 24 hours of equipment return.</p>
          <p>4. 24/7 Farmer Helpline: 1800-456-7890 (Toll-Free) | support@agrorent.in</p>
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
