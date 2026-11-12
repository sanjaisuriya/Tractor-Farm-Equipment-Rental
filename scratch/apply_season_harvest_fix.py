import os
import hashlib
from PIL import Image

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def crop_and_save(src_path, dest_path, target_size=(800, 520), crop_anchor='center', quality=90):
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

dest = 'assets/images/home-1/season-harvesting.jpg'
crop_and_save('scratch/claas_lexion_584_wheat.jpg', dest, crop_anchor='center')

h = get_hash(dest)
print(f"New season-harvesting.jpg hash: {h}")

collisions = []
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f).replace('\\', '/')
            if p == dest:
                continue
            if get_hash(p) == h:
                collisions.append(p)

print("Collisions found:", collisions)
assert len(collisions) == 0, "Duplicate hash found!"
print("PASSED! New Harvest & Threshing image is 100% unique across the entire site!")
