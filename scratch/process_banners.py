from PIL import Image
import os

def crop_banner(src, dest, target_size=(1920, 1080), quality=92, crop_anchor='center'):
    im = Image.open(src).convert('RGB')
    w, h = im.size
    tw, th = target_size
    target_ratio = tw / th
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        if crop_anchor == 'center':
            left = (w - new_w) // 2
        elif crop_anchor == 'left':
            left = 0
        else:
            left = w - new_w
        box = (left, 0, left + new_w, h)
    else:
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
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    resized.save(dest, 'JPEG', quality=quality)
    print(f"Saved {dest} from {src}: {resized.size}, {os.path.getsize(dest)} bytes")

crop_banner('scratch/farmer_cultivating_punjab.jpg', 'scratch/test_banner_punjab.jpg', crop_anchor='center')
crop_banner('scratch/plowing_land_india.jpg', 'scratch/test_banner_plow.jpg', crop_anchor='center')
crop_banner('scratch/farmer_working_field_tractor_wide.jpg', 'scratch/test_banner_working.jpg', crop_anchor='center')
