import re

for filename in ['equipment.html', 'equipment-details.html']:
    print(f"=== {filename} ===")
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', text):
        print(m.group(1))
