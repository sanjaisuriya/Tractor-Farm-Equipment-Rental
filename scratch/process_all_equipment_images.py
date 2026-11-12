import os
import hashlib
from PIL import Image

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def crop_and_save(src_path, dest_path, target_size=(800, 520), crop_anchor='center', quality=90):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with Image.open(src_path) as im:
        im = im.convert('RGB')
        w, h = im.size
        tw, th = target_size
        target_ratio = tw / th
        current_ratio = w / h

        if current_ratio > target_ratio:
            # Image is wider: crop sides
            new_w = int(h * target_ratio)
            if crop_anchor == 'center':
                left = (w - new_w) // 2
            elif crop_anchor == 'left':
                left = 0
            else:
                left = w - new_w
            box = (left, 0, left + new_w, h)
        else:
            # Image is taller: crop top/bottom
            new_h = int(w / target_ratio)
            if crop_anchor == 'top':
                top = 0
            elif crop_anchor == 'center':
                top = (h - new_h) // 2
            else:
                top = h - new_h
            box = (0, top, w, top + new_h)

        cropped = im.crop(box)
        resized = cropped.resize(target_size, Image.LANCZOS)
        resized.save(dest_path, 'JPEG', quality=quality)
        print(f"Saved {dest_path}: {resized.size}, {os.path.getsize(dest_path)} bytes")

# 1. CATALOG ITEMS (20 items)
catalog_map = [
    # 1. Mahindra 575 DI High-Power Tractor
    ('assets/images/equipment/mahindra-575-di.jpg', 'assets/images/equipment/mahindra-575-di.jpg', 'center'),
    # 2. John Deere 5310 PowerTech 4WD Tractor
    ('assets/images/equipment/john-deere-5310.jpg', 'assets/images/equipment/john-deere-5310.jpg', 'center'),
    # 3. Sonalika GT 22 Orchard Mini Tractor
    ('assets/images/equipment/sonalika-gt22-mini.jpg', 'assets/images/equipment/sonalika-gt22-mini.jpg', 'center'),
    # 4. Swaraj 855 FE Heavy-Duty Farm Tractor
    ('scratch/equipment_candidates/swaraj_735_fe.jpg', 'assets/images/equipment/swaraj-855-fe.jpg', 'center'),
    # 5. Shaktiman Semi-Champion 6 Feet Rotavator
    ('assets/images/equipment/rotavator-tilling-real.jpg', 'assets/images/equipment/rotavator-tilling.jpg', 'center'),
    # 6. Fieldking 9-Tyne Spring Loaded Cultivator
    ('assets/images/equipment/cultivator.jpg', 'assets/images/equipment/cultivator.jpg', 'center'),
    # 7. Lemken 3-Furrow Reversible MB Plough
    ('assets/images/equipment/plough.jpg', 'assets/images/equipment/plough.jpg', 'center'),
    # 8. Heavy-Duty 16-Disc Trailed Offset Harrow
    ('scratch/equipment_candidates/disc_harrow_real.jpg', 'assets/images/equipment/disc-harrow.jpg', 'center'),
    # 9. Dasmesh Happy Seeder & Zero-Till Seed Drill
    ('assets/images/equipment/dasmesh-happy-seeder.jpg', 'assets/images/equipment/dasmesh-happy-seeder.jpg', 'center'),
    # 10. Multi-Crop Pneumatic Precision Seed Planter
    ('scratch/more_equipment/planter_caseih.jpg', 'assets/images/equipment/precision-seed-planter.jpg', 'center'),
    # 11. Automatic 4-Row Paddy Seeder & Transplanter
    ('scratch/equipment_candidates/paddy_transplanter_india.jpg', 'assets/images/equipment/paddy-transplanter.jpg', 'center'),
    # 12. Mitra 500L Tractor Mounted Orchard & Crop Sprayer
    ('assets/images/equipment/agricultural-sprayer-real.jpg', 'assets/images/equipment/mitra-sprayer.jpg', 'center'),
    # 13. Hydraulic 40-Nozzle 12-Meter Folding Boom Sprayer
    ('scratch/more_equipment/boom_sprayer_caseih.jpg', 'assets/images/equipment/hydraulic-boom-sprayer.jpg', 'center'),
    # 14. High-Pressure HTP Orchard Power Sprayer
    ('scratch/more_equipment/vineyard_sprayer_holder.jpg', 'assets/images/equipment/htp-power-sprayer.jpg', 'center'),
    # 15. Preet 987 Self-Propelled Multi-Crop Combine Harvester
    ('assets/images/equipment/preet-987-harvester.jpg', 'assets/images/equipment/preet-987-harvester.jpg', 'center'),
    # 16. Tractor-Mounted Multi-Crop Reaper Binder
    ('scratch/reaper_bottlesford.jpg', 'assets/images/equipment/reaper-binder.jpg', 'center'),
    # 17. Heavy-Duty Round Straw & Fodder Hay Baler
    ('scratch/equipment_candidates/tractor_baler_field.jpg', 'assets/images/equipment/round-hay-baler.jpg', 'center'),
    # 18. Heavy-Duty 8-Tonne Hydraulic Tipping Trailer
    ('assets/images/equipment/tractor-trailer-real.jpg', 'assets/images/equipment/hydraulic-tipping-trailer.jpg', 'center'),
    # 19. Dual-Axle 12-Tonne Grain Haulage Mandi Trolley
    ('scratch/more_equipment/grain_trailer_belarus.jpg', 'assets/images/equipment/mandi-grain-trolley.jpg', 'center'),
    # 20. Kirloskar 10 HP High-Discharge Farm Irrigation Pump
    ('scratch/equipment_candidates/irrigation_pump_india.jpg', 'assets/images/equipment/farm-irrigation-pump.jpg', 'center')
]

print("=== Processing 20 Catalog Items ===")
for src, dst, anchor in catalog_map:
    crop_and_save(src, dst, target_size=(800, 520), crop_anchor=anchor)

# 2. CATEGORY BANNERS (6 items)
categories_map = [
    # 1. Agricultural Tractors
    ('scratch/farmers/mahindra_in_india.jpg', 'assets/images/equipment/cat-tractors.jpg', 'center'),
    # 2. Tillage Equipment
    ('scratch/cropped_candidates/along_with_tractor.jpg', 'assets/images/equipment/cat-tillage.jpg', 'center'),
    # 3. Sowing Equipment
    ('scratch/downloaded_tests/national_agro_happy_seeder.jpg', 'assets/images/equipment/cat-sowing.jpg', 'center'),
    # 4. Spraying Equipment
    ('scratch/more_equipment/boom_sprayer_caseih.jpg', 'assets/images/equipment/cat-spraying.jpg', 'top'),
    # 5. Harvesting Equipment
    ('scratch/more_equipment/combine_john_deere.jpg', 'assets/images/equipment/cat-harvesting.jpg', 'center'),
    # 6. Transport Equipment
    ('scratch/equipment_candidates/tractor_trailer_hmt.jpg', 'assets/images/equipment/cat-transport.jpg', 'center')
]

print("\n=== Processing 6 Category Items ===")
for src, dst, anchor in categories_map:
    crop_and_save(src, dst, target_size=(800, 520), crop_anchor=anchor)

# 3. FARMING OPERATIONS & CROP CYCLE (5 items)
cycle_map = [
    # Phase 1: Primary Land Tillage & Deep Plowing
    ('scratch/tillage_downloads/field_ploughing_tractor.jpg', 'assets/images/equipment/cycle-phase-1-plough.jpg', 'center'),
    # Phase 2: Secondary Soil Pulverization & Tilth
    ('scratch/downloaded_tests/tractor_cultivating_farm.jpg', 'assets/images/equipment/cycle-phase-2-rotavator.jpg', 'center'),
    # Phase 3: Precision Sowing & Fertilizer Placement
    ('scratch/downloaded_tests/punjab_farmer_cultivating.jpg', 'assets/images/equipment/cycle-phase-3-seeder.jpg', 'center'),
    # Phase 4: Crop Protection & Boom Spraying
    ('scratch/more_equipment/vineyard_sprayer_holder.jpg', 'assets/images/equipment/cycle-phase-4-spraying.jpg', 'top'),
    # Phase 5: Harvesting, Threshing & Haulage
    ('scratch/equipment_candidates/combine_harvester_crop.jpg', 'assets/images/equipment/cycle-phase-5-harvesting.jpg', 'center')
]

print("\n=== Processing 5 Crop Cycle Items ===")
for src, dst, anchor in cycle_map:
    crop_and_save(src, dst, target_size=(600, 380), crop_anchor=anchor)

# 4. FINAL CTA BACKGROUND
print("\n=== Processing Final CTA Background ===")
crop_and_save('scratch/more_equipment/plowing_new_holland.jpg', 'assets/images/equipment/final-cta-tractor.jpg', target_size=(1920, 800), crop_anchor='center', quality=88)

print("\nAll images processed successfully!")
