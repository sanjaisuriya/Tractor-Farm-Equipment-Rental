from PIL import Image
import os

images = ['tortella', 'jd450', 'vaderstad', 'seeddrill4189']

for name in images:
    path = f'scratch/{name}.jpg'
    im = Image.open(path)
    w, h = im.size
    print(f'{name}: {w}x{h}, mode={im.mode}')
    
    # Let us compute smart crop for 800x520 (1.538)
    target_ratio = 800 / 520
    cur_ratio = w / h
    
    if cur_ratio > target_ratio:
        # Wider than target -> crop sides
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        crop_box = (left, 0, left + new_w, h)
    else:
        # Taller than target -> crop top/bottom
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        crop_box = (0, top, w, top + new_h)
        
    cropped = im.crop(crop_box).resize((800, 520), Image.Resampling.LANCZOS)
    cropped.save(f'scratch/preview_{name}.jpg', quality=92)
    print(f'  Saved scratch/preview_{name}.jpg')
