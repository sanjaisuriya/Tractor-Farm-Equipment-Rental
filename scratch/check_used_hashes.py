import hashlib, os, glob

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

used_hashes = {}
for html in glob.glob('*.html'):
    with open(html, 'r', encoding='utf-8') as f:
        content = f.read()
    for root, dirs, files in os.walk('assets/images'):
        for file in files:
            p = os.path.join(root, file).replace('\\', '/')
            if p in content:
                h = get_hash(p)
                used_hashes[h] = p

print(f"Total uniquely hashed images used in site: {len(used_hashes)}")

candidates = [
    ('north_india_tractor', 'scratch/farmers/north_india_tractor.jpg'),
    ('goa_driver', 'scratch/farmers/goa_tractor_driver.jpg'),
    ('mahindra_in_india', 'scratch/farmers/mahindra_in_india.jpg'),
    ('cotton_farmer_haryana', 'scratch/downloaded_tests/cotton_farmer_haryana.jpg'),
    ('sugar_cane_farmers', 'scratch/real_field/sugar_cane_farmers.jpg'),
    ('mahindra_india', 'mahindra_india.jpg'),
    ('mahindra_415', 'mahindra_415.jpg'),
    ('new_holland_plowing', 'new_holland_plowing.jpg')
]

for name, path in candidates:
    if os.path.exists(path):
        h = get_hash(path)
        if h in used_hashes:
            print(f"[ALREADY USED] {name} matches {used_hashes[h]}")
        else:
            print(f"[FRESH / UNUSED] {name} (Size: {os.path.getsize(path)})")
