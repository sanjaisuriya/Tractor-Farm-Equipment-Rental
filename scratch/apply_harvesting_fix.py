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

# Save as cat-harvesting.jpg
crop_and_save('scratch/harvester_wheat_field.jpg', 'assets/images/equipment/cat-harvesting.jpg', target_size=(800, 520), crop_anchor='center')

# Check hash uniqueness
target = 'assets/images/equipment/cat-harvesting.jpg'
target_hash = get_hash(target)
print(f"New cat-harvesting hash: {target_hash}")

collisions = []
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f).replace('\\', '/')
            if p == target:
                continue
            if get_hash(p) == target_hash:
                collisions.append(p)

print("Collisions found:", collisions)
assert len(collisions) == 0, "Duplicate hash found!"
print("PASSED! New Harvesting Equipment image is 100% unique across the entire site!")
