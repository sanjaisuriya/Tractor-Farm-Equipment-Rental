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

# 1. Tractors Category: tractor_fendt828.jpg or tractor_mf8740.jpg
crop_and_save('scratch/tractor_fendt828.jpg', 'assets/images/equipment/cat-tractors.jpg', target_size=(800, 520), crop_anchor='center')

# 2. Sowing Equipment Category: sowing_field_seeder.jpg
crop_and_save('scratch/sowing_field_seeder.jpg', 'assets/images/equipment/cat-sowing.jpg', target_size=(800, 520), crop_anchor='center')

print("Checking hash uniqueness across all site images...")
# Verify against all images in assets/images/
target_files = [
    'assets/images/equipment/cat-tractors.jpg',
    'assets/images/equipment/cat-sowing.jpg'
]

hashes = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f).replace('\\', '/')
            h = get_hash(p)
            hashes.setdefault(h, []).append(p)

for tf in target_files:
    tf_norm = tf.replace('\\', '/')
    tf_hash = get_hash(tf_norm)
    print(f"{tf_norm} (MD5: {tf_hash[:8]}...) is used at: {hashes.get(tf_hash)}")
    assert len(hashes.get(tf_hash, [])) == 1, f"Hash collision for {tf_norm}!"

print("PASSED! Both new images are 100% unique across the entire project with ZERO collisions!")
