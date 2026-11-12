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
        left = (w - new_w) // 2
        box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        box = (0, top, w, top + new_h)
        
    cropped = im.crop(box)
    resized = cropped.resize(target_size, Image.LANCZOS)
    resized.save(dest, 'JPEG', quality=quality)
    print(f"Saved {dest} from {src}: {resized.size}")

crop_banner('scratch/plowing_land_india.jpg', 'scratch/booking_banner_plow.jpg')
