import re

with open('equipment.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Category Images
cat_replacements = [
    (r'<img src="assets/images/equipment/tractor\.jpg" alt="Agricultural Tractors"', 
     '<img src="assets/images/equipment/cat-tractors.jpg" alt="Agricultural Tractors"'),
    (r'<img src="assets/images/equipment/rotavator\.jpg" alt="Tillage Equipment"', 
     '<img src="assets/images/equipment/cat-tillage.jpg" alt="Tillage Equipment"'),
    (r'<img src="assets/images/equipment/seed-drill\.jpg" alt="Sowing Equipment"', 
     '<img src="assets/images/equipment/cat-sowing.jpg" alt="Sowing Equipment"'),
    (r'<img src="assets/images/equipment/sprayer\.jpg" alt="Spraying Equipment"', 
     '<img src="assets/images/equipment/cat-spraying.jpg" alt="Spraying Equipment"'),
    (r'<img src="assets/images/equipment/harvester\.jpg" alt="Harvesting Equipment"', 
     '<img src="assets/images/equipment/cat-harvesting.jpg" alt="Harvesting Equipment"'),
    (r'<img src="assets/images/equipment/trailer\.jpg" alt="Transport Equipment"', 
     '<img src="assets/images/equipment/cat-transport.jpg" alt="Transport Equipment"')
]

for pat, rep in cat_replacements:
    html, n = re.subn(pat, rep, html)
    print(f"Category replace '{pat[:35]}': {n}")

# 2. Update Farming Operations & Crop Cycle (add images to the 5 stages)
crop_cycle_old = '''        <!-- 5 Crop Stage Step Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
          
          <!-- Stage 1 -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="w-9 h-9 rounded-xl bg-forest text-gold font-black flex items-center justify-center text-sm shadow-md font-heading">01</span>
                <span class="text-xs font-bold text-agri dark:text-fresh uppercase tracking-wider">Phase 1</span>
              </div>
              <div class="w-12 h-12 rounded-xl bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-2xl mb-4">
                <i class="fa-solid fa-share-nodes"></i>
              </div>
              <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                Primary Land Tillage & Deep Plowing
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                Inverts tough hardpan soil, incorporates crop residues, and destroys deep weed roots before sowing.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 50 - 75 HP (4WD)</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> Reversible MB Plough, Subsoiler</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹650 / hr</span>
            </div>
          </div>

          <!-- Stage 2 -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="w-9 h-9 rounded-xl bg-forest text-gold font-black flex items-center justify-center text-sm shadow-md font-heading">02</span>
                <span class="text-xs font-bold text-agri dark:text-fresh uppercase tracking-wider">Phase 2</span>
              </div>
              <div class="w-12 h-12 rounded-xl bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-2xl mb-4">
                <i class="fa-solid fa-gear"></i>
              </div>
              <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                Secondary Soil Pulverization & Tilth
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                Crushes soil clods into fine tilth, levels seedbeds, and ensures moisture retention for rapid germination.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 45 - 55 HP</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> 6-7ft Rotavator, Disc Harrow</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹350 / hr</span>
            </div>
          </div>

          <!-- Stage 3 -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="w-9 h-9 rounded-xl bg-forest text-gold font-black flex items-center justify-center text-sm shadow-md font-heading">03</span>
                <span class="text-xs font-bold text-agri dark:text-fresh uppercase tracking-wider">Phase 3</span>
              </div>
              <div class="w-12 h-12 rounded-xl bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-2xl mb-4">
                <i class="fa-solid fa-seedling"></i>
              </div>
              <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                Precision Sowing & Fertilizer Placement
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                Deposits seeds and basal fertilizer at exact depths with uniform row spacing to maximize germination rate.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 40 - 55 HP</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> Happy Seeder, Zero-Till Drill</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹400 / hr</span>
            </div>
          </div>

          <!-- Stage 4 -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="w-9 h-9 rounded-xl bg-forest text-gold font-black flex items-center justify-center text-sm shadow-md font-heading">04</span>
                <span class="text-xs font-bold text-agri dark:text-fresh uppercase tracking-wider">Phase 4</span>
              </div>
              <div class="w-12 h-12 rounded-xl bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-2xl mb-4">
                <i class="fa-solid fa-spray-can"></i>
              </div>
              <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                Crop Protection & Boom Spraying
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                Delivers uniform droplet coverage for foliar nutrients, pest management, and weed control without crop trampling.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 20 - 45 HP (High Clearance)</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> 12m Boom Sprayer, HTP Sprayer</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹350 / hr</span>
            </div>
          </div>

          <!-- Stage 5 -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="w-9 h-9 rounded-xl bg-forest text-gold font-black flex items-center justify-center text-sm shadow-md font-heading">05</span>
                <span class="text-xs font-bold text-agri dark:text-fresh uppercase tracking-wider">Phase 5</span>
              </div>
              <div class="w-12 h-12 rounded-xl bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-2xl mb-4">
                <i class="fa-solid fa-wheat-awn"></i>
              </div>
              <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                Harvesting, Threshing & Haulage
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                Rapid multi-crop harvesting with under 1% grain loss and immediate tipping trailer haulage directly to market.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Machinery:</strong> 75 - 110 HP Harvesters</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> Combine Harvester, 8-Ton Trolley</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹1,800 / hr</span>
            </div>
          </div>

        </div>'''

crop_cycle_new = '''        <!-- 5 Crop Stage Step Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
          
          <!-- Stage 1 -->
          <div class="group rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div>
              <div class="relative h-36 overflow-hidden bg-slate-200 dark:bg-slate-800">
                <img src="assets/images/equipment/cycle-phase-1-plough.jpg" alt="Primary Land Tillage & Deep Plowing" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
                <div class="absolute top-3 left-3">
                  <span class="w-8 h-8 rounded-lg bg-forest/90 text-gold font-black flex items-center justify-center text-xs shadow-md font-heading backdrop-blur-sm border border-white/10">01</span>
                </div>
                <div class="absolute bottom-2.5 right-3">
                  <span class="text-[11px] font-bold text-white uppercase tracking-wider bg-forest/80 px-2 py-0.5 rounded backdrop-blur-sm border border-white/10">Phase 1</span>
                </div>
              </div>
              <div class="p-5">
                <div class="w-9 h-9 rounded-lg bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-lg mb-3">
                  <i class="fa-solid fa-share-nodes"></i>
                </div>
                <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                  Primary Land Tillage & Deep Plowing
                </h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                  Inverts tough hardpan soil, incorporates crop residues, and destroys deep weed roots before sowing.
                </p>
              </div>
            </div>
            <div class="px-5 pb-5 pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 50 - 75 HP (4WD)</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> Reversible MB Plough, Subsoiler</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹650 / hr</span>
            </div>
          </div>

          <!-- Stage 2 -->
          <div class="group rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div>
              <div class="relative h-36 overflow-hidden bg-slate-200 dark:bg-slate-800">
                <img src="assets/images/equipment/cycle-phase-2-rotavator.jpg" alt="Secondary Soil Pulverization & Tilth" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
                <div class="absolute top-3 left-3">
                  <span class="w-8 h-8 rounded-lg bg-forest/90 text-gold font-black flex items-center justify-center text-xs shadow-md font-heading backdrop-blur-sm border border-white/10">02</span>
                </div>
                <div class="absolute bottom-2.5 right-3">
                  <span class="text-[11px] font-bold text-white uppercase tracking-wider bg-forest/80 px-2 py-0.5 rounded backdrop-blur-sm border border-white/10">Phase 2</span>
                </div>
              </div>
              <div class="p-5">
                <div class="w-9 h-9 rounded-lg bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-lg mb-3">
                  <i class="fa-solid fa-gear"></i>
                </div>
                <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                  Secondary Soil Pulverization & Tilth
                </h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                  Crushes soil clods into fine tilth, levels seedbeds, and ensures moisture retention for rapid germination.
                </p>
              </div>
            </div>
            <div class="px-5 pb-5 pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 45 - 55 HP</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> 6-7ft Rotavator, Disc Harrow</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹350 / hr</span>
            </div>
          </div>

          <!-- Stage 3 -->
          <div class="group rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div>
              <div class="relative h-36 overflow-hidden bg-slate-200 dark:bg-slate-800">
                <img src="assets/images/equipment/cycle-phase-3-seeder.jpg" alt="Precision Sowing & Fertilizer Placement" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
                <div class="absolute top-3 left-3">
                  <span class="w-8 h-8 rounded-lg bg-forest/90 text-gold font-black flex items-center justify-center text-xs shadow-md font-heading backdrop-blur-sm border border-white/10">03</span>
                </div>
                <div class="absolute bottom-2.5 right-3">
                  <span class="text-[11px] font-bold text-white uppercase tracking-wider bg-forest/80 px-2 py-0.5 rounded backdrop-blur-sm border border-white/10">Phase 3</span>
                </div>
              </div>
              <div class="p-5">
                <div class="w-9 h-9 rounded-lg bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-lg mb-3">
                  <i class="fa-solid fa-seedling"></i>
                </div>
                <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                  Precision Sowing & Fertilizer Placement
                </h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                  Deposits seeds and basal fertilizer at exact depths with uniform row spacing to maximize germination rate.
                </p>
              </div>
            </div>
            <div class="px-5 pb-5 pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 40 - 55 HP</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> Happy Seeder, Zero-Till Drill</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹400 / hr</span>
            </div>
          </div>

          <!-- Stage 4 -->
          <div class="group rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div>
              <div class="relative h-36 overflow-hidden bg-slate-200 dark:bg-slate-800">
                <img src="assets/images/equipment/cycle-phase-4-spraying.jpg" alt="Crop Protection & Boom Spraying" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
                <div class="absolute top-3 left-3">
                  <span class="w-8 h-8 rounded-lg bg-forest/90 text-gold font-black flex items-center justify-center text-xs shadow-md font-heading backdrop-blur-sm border border-white/10">04</span>
                </div>
                <div class="absolute bottom-2.5 right-3">
                  <span class="text-[11px] font-bold text-white uppercase tracking-wider bg-forest/80 px-2 py-0.5 rounded backdrop-blur-sm border border-white/10">Phase 4</span>
                </div>
              </div>
              <div class="p-5">
                <div class="w-9 h-9 rounded-lg bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-lg mb-3">
                  <i class="fa-solid fa-spray-can"></i>
                </div>
                <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                  Crop Protection & Boom Spraying
                </h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                  Delivers uniform droplet coverage for foliar nutrients, pest management, and weed control without crop trampling.
                </p>
              </div>
            </div>
            <div class="px-5 pb-5 pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Tractors:</strong> 20 - 45 HP (High Clearance)</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> 12m Boom Sprayer, HTP Sprayer</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹350 / hr</span>
            </div>
          </div>

          <!-- Stage 5 -->
          <div class="group rounded-2xl bg-white dark:bg-[#1A261D] border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div>
              <div class="relative h-36 overflow-hidden bg-slate-200 dark:bg-slate-800">
                <img src="assets/images/equipment/cycle-phase-5-harvesting.jpg" alt="Harvesting, Threshing & Haulage" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
                <div class="absolute top-3 left-3">
                  <span class="w-8 h-8 rounded-lg bg-forest/90 text-gold font-black flex items-center justify-center text-xs shadow-md font-heading backdrop-blur-sm border border-white/10">05</span>
                </div>
                <div class="absolute bottom-2.5 right-3">
                  <span class="text-[11px] font-bold text-white uppercase tracking-wider bg-forest/80 px-2 py-0.5 rounded backdrop-blur-sm border border-white/10">Phase 5</span>
                </div>
              </div>
              <div class="p-5">
                <div class="w-9 h-9 rounded-lg bg-agri/10 text-agri dark:text-fresh flex items-center justify-center text-lg mb-3">
                  <i class="fa-solid fa-wheat-awn"></i>
                </div>
                <h3 class="text-base font-bold font-heading text-forest dark:text-white mb-2">
                  Harvesting, Threshing & Haulage
                </h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                  Rapid multi-crop harvesting with under 1% grain loss and immediate tipping trailer haulage directly to market.
                </p>
              </div>
            </div>
            <div class="px-5 pb-5 pt-3 border-t border-slate-100 dark:border-slate-700/60 space-y-1 text-xs">
              <p class="text-slate-500 dark:text-slate-400"><strong>Machinery:</strong> 75 - 110 HP Harvesters</p>
              <p class="text-slate-500 dark:text-slate-400"><strong>Tools:</strong> Combine Harvester, 8-Ton Trolley</p>
              <span class="inline-block mt-2 font-bold text-agri dark:text-fresh">From ₹1,800 / hr</span>
            </div>
          </div>

        </div>'''

if crop_cycle_old in html:
    html = html.replace(crop_cycle_old, crop_cycle_new)
    print("Replaced crop cycle section successfully!")
else:
    print("WARNING: crop_cycle_old not found in equipment.html, checking fuzzy replace...")

# 3. Update Bottom CTA background
cta_old = '<section class="py-12 sm:py-16 bg-gradient-to-r from-forest via-[#1D4E36] to-forest text-white relative overflow-hidden">'
cta_new = '<section class="py-12 sm:py-16 text-white relative overflow-hidden" style="background: linear-gradient(rgba(10, 35, 18, 0.88), rgba(10, 35, 18, 0.92)), url(\'assets/images/equipment/final-cta-tractor.jpg\') center/cover no-repeat;">'

if cta_old in html:
    html = html.replace(cta_old, cta_new)
    print("Replaced Bottom CTA background successfully!")
else:
    print("WARNING: cta_old not found!")

# 4. Enhance FAQ with question icons
faq_old = '<summary class="flex items-center justify-between cursor-pointer font-bold font-heading text-forest dark:text-white text-sm sm:text-base list-none">\n              <span>'
faq_new = '<summary class="flex items-center justify-between cursor-pointer font-bold font-heading text-forest dark:text-white text-sm sm:text-base list-none">\n              <span class="flex items-center gap-2.5"><i class="fa-solid fa-circle-question text-agri dark:text-fresh text-sm shrink-0"></i><span>'

# Update closing span in summary
# Each question is: <span>...</span>
# Let's replace systematically:
html = re.sub(r'<summary class="flex items-center justify-between cursor-pointer font-bold font-heading text-forest dark:text-white text-sm sm:text-base list-none">\s*<span>([^<]+)</span>',
              r'<summary class="flex items-center justify-between cursor-pointer font-bold font-heading text-forest dark:text-white text-sm sm:text-base list-none">\n              <span class="flex items-center gap-2.5"><i class="fa-solid fa-circle-question text-agri dark:text-fresh text-sm shrink-0"></i><span>\1</span></span>',
              html)
print("Updated FAQ question icons!")

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved equipment.html successfully!")
