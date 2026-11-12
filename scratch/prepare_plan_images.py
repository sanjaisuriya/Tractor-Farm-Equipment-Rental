import shutil
from PIL import Image

def get_crop(src, dest, target_size=(800, 500)):
    im = Image.open(src)
    im = im.convert('RGB')
    w, h = im.size
    tw, th = target_size
    target_ratio = tw / th
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        box = (0, top, w, top + new_h)
        
    cropped = im.crop(box)
    resized = cropped.resize(target_size, Image.LANCZOS)
    resized.save(dest, 'JPEG', quality=92)
    print(f"Saved {dest} from {src}: {resized.size}")

get_crop('assets/images/home-1/real_farmer_tractor_1.jpg', 'scratch/plan_hourly_test.jpg')
get_crop('assets/images/equipment/rotavator-tilling-real.jpg', 'scratch/plan_daily_test.jpg')
get_crop('scratch/mechanized_harvesting_kerala.jpg', 'scratch/plan_weekly_test.jpg')
get_crop('assets/images/home-1/machinery-depot.jpg', 'scratch/plan_monthly_test.jpg')
