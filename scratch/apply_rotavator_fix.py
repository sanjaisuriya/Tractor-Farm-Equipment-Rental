import os
import shutil
import hashlib
from PIL import Image

src = 'scratch/cand_rotavator_tilling_2.jpg'
dest = 'assets/images/equipment/rotavator-tilling.jpg'

shutil.copy(src, dest)
print(f"Copied {src} -> {dest}")

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

target_hash = get_hash(dest)
print(f"New rotavator-tilling.jpg hash: {target_hash}")

collisions = []
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f).replace('\\', '/')
            if p == dest:
                continue
            if get_hash(p) == target_hash:
                collisions.append(p)

print("Collisions found:", collisions)
assert len(collisions) == 0, "Duplicate hash found!"
print("PASSED! New Shaktiman Rotavator image is 100% unique across the entire site!")
