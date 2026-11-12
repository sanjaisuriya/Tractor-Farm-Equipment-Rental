import re

for filename in ['about.html', 'home-2.html', 'index.html']:
    print(f'=== {filename} ===')
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', content)
    for src, alt in matches:
        if any(w in src.lower() for w in ['tractor', 'farmer', 'land']):
            print(f'{src} | {alt}')
