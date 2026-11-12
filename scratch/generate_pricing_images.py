import os
from PIL import Image

def process_image(src, dest, target_size=(800, 500), quality=92, crop_box=None):
    im = Image.open(src).convert('RGB')
    w, h = im.size
    tw, th = target_size
    target_ratio = tw / th
    
    if crop_box:
        cropped = im.crop(crop_box)
    else:
        current_ratio = w / h
        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            cropped = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            cropped = im.crop((0, top, w, top + new_h))
            
    final_img = cropped.resize(target_size, Image.LANCZOS)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    final_img.save(dest, 'JPEG', quality=quality)
    print(f"Created {dest}: size={final_img.size}, bytes={os.path.getsize(dest)}")

# 1. Hourly Rates: Indian tractor operating in an agricultural field
process_image(
    'assets/images/home-1/real_farmer_tractor_1.jpg',
    'assets/images/pricing/plan-hourly-tractor.jpg',
    target_size=(800, 500)
)

# 2. Daily Rates: Tractor with an attached rotavator
process_image(
    'assets/images/equipment/rotavator-tilling-real.jpg',
    'assets/images/pricing/plan-daily-rotavator.jpg',
    target_size=(800, 500)
)

# 3. Weekly Rental: Combine harvester working in a paddy field
process_image(
    'scratch/mechanized_harvesting_kerala.jpg',
    'assets/images/pricing/plan-weekly-harvester.jpg',
    target_size=(800, 500)
)

# 4. Monthly Season Pass: Multiple tractors and agricultural machinery
process_image(
    'assets/images/home-1/machinery-depot.jpg',
    'assets/images/pricing/plan-monthly-fleet.jpg',
    target_size=(800, 500)
)

print("All 4 pricing plan images successfully generated!")
