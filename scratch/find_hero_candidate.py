import glob
import re
import os
import hashlib
from PIL import Image

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

used_paths = set()
used_hashes = set()

for ext in ['*.html', 'js/*.js']:
    for f in glob.glob(ext):
        with open(f, 'r', encoding='utf-8') as fh:
            text = fh.read()
        for m in re.findall(r'(assets/images/[^\s"\'\)]+)', text):
            clean = m.strip("',;\"")
            if os.path.exists(clean):
                used_paths.add(clean)
                used_hashes.add(get_hash(clean))

print(f"Total currently used image files: {len(used_paths)}")
print(f"Total currently used hashes: {len(used_hashes)}")

# Check candidates in scratch
candidates = []
for root, dirs, files in os.walk('scratch'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f)
            h = get_hash(p)
            if h not in used_hashes and p not in used_paths:
                try:
                    im = Image.open(p)
                    if im.width >= 1200:
                        candidates.append((f, p, im.size, os.path.getsize(p)))
                except:
                    pass

print(f"\nFresh large candidates (>1200px wide): {len(candidates)}")
for f, p, sz, bytes_sz in sorted(candidates, key=lambda x: x[3], reverse=True)[:15]:
    print(f"  {f:35} | {sz} | {bytes_sz:8} B | {p}")
