import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

sec4_match = re.search(r'(Tractor Specifications & Price Matrix.*?)(<div class="table-responsive rounded-2xl[^"]*">.*?<table.*?</table>\s*</div>)', html, re.DOTALL)

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

if sec4_match:
    html = html[:sec4_match.start(2)] + new_sec4_table + html[sec4_match.end(2):]
    with open('rates-pricing.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced Section 4 table successfully!")
else:
    print("Could not match Section 4 table!")
