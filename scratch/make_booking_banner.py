import os
from PIL import Image

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

# Let's create high-resolution booking-banner.jpg
crop_banner('scratch/farmer_working_field_tractor_wide.jpg', 'assets/images/booking/booking-banner.jpg', crop_anchor='center')
