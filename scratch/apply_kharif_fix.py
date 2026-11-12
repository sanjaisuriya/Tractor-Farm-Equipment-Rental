import shutil
import os
import hashlib

src = 'scratch/test_kharif_1.jpg'
dest = 'assets/images/home-1/season-kharif.jpg'

shutil.copy(src, dest)
print(f"Updated {dest}: {os.path.getsize(dest)} bytes")

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

h = get_hash(dest)
print(f"New season-kharif.jpg hash: {h}")

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
print("PASSED! New Kharif Cultivation image is 100% unique across the entire site!")
