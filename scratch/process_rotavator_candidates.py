import os
from PIL import Image

def crop_and_save(src_path, dest_path, target_size=(800, 520), crop_anchor='center', quality=90):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with Image.open(src_path) as im:
        im = im.convert('RGB')
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
        resized.save(dest_path, 'JPEG', quality=quality)
        print(f"Saved {dest_path}: {resized.size}, {os.path.getsize(dest_path)} bytes")

crop_and_save('scratch/farmer_tractor_tilling.jpg', 'scratch/cand_rotavator_tilling_1.jpg')
crop_and_save('scratch/tractor_mounted_rototiller.jpg', 'scratch/cand_rotavator_tilling_2.jpg')
crop_and_save('scratch/rotary_tiller_korea.jpg', 'scratch/cand_rotavator_tilling_3.jpg')
crop_and_save('scratch/tractor_tilling_west_mains.jpg', 'scratch/cand_rotavator_tilling_4.jpg')
