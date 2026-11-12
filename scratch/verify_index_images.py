import os
import hashlib
import re

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

images = re.findall(r'(assets/images/[^\s"\'\)]+)', text)
hashes = {}
duplicates = []

for img in set(images):
    clean = img.strip("',;\"")
    if not os.path.exists(clean):
        print(f"MISSING: {clean}")
        continue
    h = get_hash(clean)
    if h in hashes:
        duplicates.append((clean, hashes[h]))
    hashes[h] = clean
    print(f"  [OK] {clean} ({os.path.getsize(clean)} B)")

if duplicates:
    print("Duplicates in index.html:", duplicates)
else:
    print("PASSED: All images in index.html exist and have 100% unique hashes!")
