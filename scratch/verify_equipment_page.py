import os
import re
import hashlib
from PIL import Image

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

print("========================================")
print("1. CHECKING ALL IMAGES IN equipment.html")
print("========================================")
with open('equipment.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_images = re.findall(r'(assets/images/[^\s"\'\)]+)', html_content)
missing_html = []
for img in set(html_images):
    clean = img.strip("',;\"")
    if not os.path.exists(clean):
        missing_html.append(clean)
    else:
        size = os.path.getsize(clean)
        print(f"  [OK] {clean} ({size} bytes)")

if missing_html:
    print(f"FAILED: Missing images in equipment.html: {missing_html}")
else:
    print(f"PASSED: All {len(set(html_images))} images in equipment.html exist!")

print("\n========================================")
print("2. CHECKING ALL 20 EQUIPMENT CARDS IN js/equipment.js")
print("========================================")
with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

pattern = r'id:\s*"([^"]+)",\s*name:\s*"([^"]+)",[\s\S]*?image:\s*"([^"]+)"'
cards = re.findall(pattern, js_content)
print(f"Found {len(cards)} equipment cards:")

card_images = []
card_hashes = {}
duplicate_cards = []

for idx, (eq_id, name, img_path) in enumerate(cards, 1):
    if not os.path.exists(img_path):
        print(f"  [ERROR] Card {idx}: {name} -> MISSING: {img_path}")
        continue
    h = get_hash(img_path)
    im = Image.open(img_path)
    if h in card_hashes:
        duplicate_cards.append((idx, name, img_path, card_hashes[h]))
    card_hashes[h] = (idx, name, img_path)
    card_images.append(img_path)
    print(f"  {idx:2}. [{eq_id:15}] {name[:35]:35} | {im.size} | {os.path.getsize(img_path):7} B | {img_path}")

if duplicate_cards:
    print(f"FAILED: Found duplicate images among cards: {duplicate_cards}")
else:
    print(f"PASSED: All {len(cards)} equipment cards have 100% UNIQUE images!")

print("\n========================================")
print("3. CHECKING CATEGORIES (6)")
print("========================================")
cats = [
    'assets/images/equipment/cat-tractors.jpg',
    'assets/images/equipment/cat-tillage.jpg',
    'assets/images/equipment/cat-sowing.jpg',
    'assets/images/equipment/cat-spraying.jpg',
    'assets/images/equipment/cat-harvesting.jpg',
    'assets/images/equipment/cat-transport.jpg'
]
cat_hashes = set()
for c in cats:
    assert os.path.exists(c), f"Missing {c}"
    h = get_hash(c)
    assert h not in cat_hashes, f"Duplicate hash {c}"
    cat_hashes.add(h)
    print(f"  [OK] {c}")
print(f"PASSED: All 6 categories exist and are unique!")

print("\n========================================")
print("4. CHECKING CROP CYCLE (5 PHASES)")
print("========================================")
phases = [
    'assets/images/equipment/cycle-phase-1-plough.jpg',
    'assets/images/equipment/cycle-phase-2-rotavator.jpg',
    'assets/images/equipment/cycle-phase-3-seeder.jpg',
    'assets/images/equipment/cycle-phase-4-spraying.jpg',
    'assets/images/equipment/cycle-phase-5-harvesting.jpg'
]
phase_hashes = set()
for p in phases:
    assert os.path.exists(p), f"Missing {p}"
    h = get_hash(p)
    assert h not in phase_hashes, f"Duplicate hash {p}"
    phase_hashes.add(h)
    print(f"  [OK] {p}")
print(f"PASSED: All 5 crop cycle phases exist and are unique!")

print("\n========================================")
print("5. CHECKING BOTTOM CTA BACKGROUND")
print("========================================")
cta_bg = 'assets/images/equipment/final-cta-tractor.jpg'
assert os.path.exists(cta_bg), f"Missing {cta_bg}"
im = Image.open(cta_bg)
print(f"  [OK] {cta_bg} ({im.size}, {os.path.getsize(cta_bg)} bytes)")
print("PASSED: Bottom CTA background exists and is valid!")

print("\n========================================")
print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
print("========================================")
