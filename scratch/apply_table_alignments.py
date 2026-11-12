import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Section 4 Table
sec4_old_match = re.search(r'(id="tractorMatrix".*?)(<div class="table-responsive[^"]*">.*?<table[^>]*>.*?</table>\s*</div>)', html, re.DOTALL)

new_sec4_table = """<div class="pricing-table-container rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm bg-white dark:bg-[#18231B] reveal-on-scroll">
          <table class="pricing-table w-full border-collapse min-w-[940px]">
            <thead>
              <tr class="bg-slate-50 dark:bg-[#121813] border-b border-gray-200 dark:border-gray-800 text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300">
                <th class="py-4 px-6 text-left whitespace-nowrap min-w-[240px]">Tractor Model</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[110px]">Horsepower</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[150px]">Drive Type</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[130px]">Lift Capacity</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[120px]">Hourly Rate</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[130px]">Daily Rate</th>
                <th class="py-4 px-6 text-center whitespace-nowrap min-w-[120px]">Rent Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 dark:divide-gray-800 text-xs sm:text-sm">
              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-4 px-6 font-bold text-slate-900 dark:text-white align-middle">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-tractor text-agri"></i>
                    <span>Sonalika GT 22 Orchard Mini</span>
                  </div>
                </td>
                <td class="py-4 px-4 text-center align-middle font-bold text-agri dark:text-fresh whitespace-nowrap">22 HP</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">2WD Compact Narrow</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">650 kg</td>
                <td class="py-4 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹350 / hr</td>
                <td class="py-4 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹2,200 / day</td>
                <td class="py-4 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=mini-245" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-4 px-6 font-bold text-slate-900 dark:text-white align-middle">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-tractor text-agri"></i>
                    <span>Mahindra 575 DI High-Power</span>
                  </div>
                </td>
                <td class="py-4 px-4 text-center align-middle font-bold text-agri dark:text-fresh whitespace-nowrap">45 HP</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">2WD Heavy Duty</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">1,600 kg</td>
                <td class="py-4 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹500 / hr</td>
                <td class="py-4 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹3,500 / day</td>
                <td class="py-4 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=tr-575" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-4 px-6 font-bold text-slate-900 dark:text-white align-middle">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-tractor text-agri"></i>
                    <span>Swaraj 855 FE Heavy Cultivation</span>
                  </div>
                </td>
                <td class="py-4 px-4 text-center align-middle font-bold text-agri dark:text-fresh whitespace-nowrap">52 HP</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">2WD High Displacement</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">1,700 kg</td>
                <td class="py-4 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹580 / hr</td>
                <td class="py-4 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹4,000 / day</td>
                <td class="py-4 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=tr-855" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-4 px-6 font-bold text-slate-900 dark:text-white align-middle">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-tractor text-agri"></i>
                    <span>John Deere 5310 PowerTech</span>
                  </div>
                </td>
                <td class="py-4 px-4 text-center align-middle font-bold text-agri dark:text-fresh whitespace-nowrap">55 HP</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">4WD Turbocharged</td>
                <td class="py-4 px-4 text-center align-middle text-muted whitespace-nowrap">2,000 kg</td>
                <td class="py-4 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹650 / hr</td>
                <td class="py-4 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹4,500 / day</td>
                <td class="py-4 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=tr-5310" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>"""

if sec4_old_match:
    html = html[:sec4_old_match.start(2)] + new_sec4_table + html[sec4_old_match.end(2):]
    print("Replaced Section 4 table successfully!")
else:
    print("Could not match Section 4 table!")

# 2. Update Section 5 Table
sec5_old_match = re.search(r'(Standalone Farm Implement.*?)(<div class="table-responsive[^"]*">.*?<table[^>]*>.*?</table>\s*</div>)', html, re.DOTALL)

new_sec5_table = """<div class="pricing-table-container rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm bg-white dark:bg-[#18231B] reveal-on-scroll">
          <table class="pricing-table w-full border-collapse min-w-[980px]">
            <thead>
              <tr class="bg-slate-100/70 dark:bg-[#121813] border-b border-gray-200 dark:border-gray-800 text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300">
                <th class="py-4 px-6 text-left whitespace-nowrap min-w-[240px]">Equipment / Implement</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[110px]">Category</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[150px]">Tractor Power Required</th>
                <th class="py-4 px-5 text-left whitespace-nowrap min-w-[200px]">Working Capacity</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[120px]">Hourly Rate</th>
                <th class="py-4 px-4 text-center whitespace-nowrap min-w-[130px]">Daily Rate</th>
                <th class="py-4 px-6 text-center whitespace-nowrap min-w-[120px]">Rent Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 dark:divide-gray-800 text-xs sm:text-sm">
              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Shaktiman Semi-Champion 6ft Rotavator</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Tillage</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">40 - 50 HP PTO</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">1.25 Acres / hr fine tilth</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹250 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹1,600 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=rot-48" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Fieldking 9-Tyne Spring Loaded Cultivator</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Tillage</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">35 - 45 HP</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">2.2 Acres / hr secondary tillage</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹180 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹1,100 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=cult-9" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Lemken 3-Furrow Reversible MB Plough</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Tillage</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">50 - 65 HP</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">1.0 Acre / hr deep furrow</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹300 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹1,900 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=plough-mb3" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Heavy-Duty 16-Disc Trailed Offset Harrow</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Tillage</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">45 - 60 HP</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">2.5 Acres / hr clod break</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹280 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹1,750 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=harrow-disc" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Dasmesh Happy Seeder & Zero-Till Drill</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Sowing</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">45 - 55 HP PTO</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">1.3 Acres / hr zero stubble burning</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹350 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹2,100 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=seed-super" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Multi-Crop Pneumatic Precision Seed Planter</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Sowing</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">40 - 50 HP</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">2.2 Acres / hr single-seed drop</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹380 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹2,400 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=seed-planter" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Mitra 500L Tractor Mounted Orchard Sprayer</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Spraying</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">24 - 50 HP PTO</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">4.5 Acres / hr fine droplet mist</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹280 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹1,800 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=spray-500" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Hydraulic 40-Nozzle 12-Meter Boom Sprayer</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Spraying</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">35 - 50 HP</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">9.0 Acres / hr wide coverage</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹320 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹2,000 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=spray-boom" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Heavy-Duty Round Straw & Fodder Hay Baler</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Harvesting</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">45 - 60 HP PTO</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">60 Compact Bales / hour</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹700 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹4,200 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=baler-straw" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/80 dark:hover:bg-[#1F2F23]/40 transition">
                <td class="py-3.5 px-6 font-bold text-slate-900 dark:text-white align-middle">Heavy-Duty 8-Tonne Hydraulic Tipping Trailer</td>
                <td class="py-3.5 px-4 text-center align-middle whitespace-nowrap"><span class="badge-cat">Transport</span></td>
                <td class="py-3.5 px-4 text-center align-middle text-muted whitespace-nowrap">40+ HP Tractor</td>
                <td class="py-3.5 px-5 text-left align-middle text-muted">8,000 kg Mandi haulage</td>
                <td class="py-3.5 px-4 text-center align-middle font-semibold text-slate-800 dark:text-slate-200 whitespace-nowrap">₹220 / hr</td>
                <td class="py-3.5 px-4 text-center align-middle font-black text-agri dark:text-fresh whitespace-nowrap">₹1,500 / day</td>
                <td class="py-3.5 px-6 text-center align-middle whitespace-nowrap">
                  <a href="booking.html?id=trail-8t" class="btn-primary text-xs py-1.5 px-4 font-bold inline-block">Rent Now</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>"""

if sec5_old_match:
    html = html[:sec5_old_match.start(2)] + new_sec5_table + html[sec5_old_match.end(2):]
    print("Replaced Section 5 table successfully!")
else:
    print("Could not match Section 5 table!")

with open('rates-pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated rates-pricing.html successfully!")
