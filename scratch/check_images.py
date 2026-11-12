import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', c):
        tag = m.group(0)
        src = m.group(1)
        if any(w in src for w in ['preet', 'rotavator', 'fleet', 'depot', 'harvester', 'tractor', 'swaraj', 'mahindra']):
            alt = re.search(r'alt=["\']([^"\']+)["\']', tag)
            alt_text = alt.group(1) if alt else 'NO ALT'
            print(f'{f} -> {src} | alt: {alt_text}')
