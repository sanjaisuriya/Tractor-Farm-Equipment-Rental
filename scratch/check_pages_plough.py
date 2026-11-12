import re

for f in ['index.html', 'home-2.html', 'about.html', 'equipment.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
        for img in imgs:
            if any(k in img for k in ['plough', 'tillage', 'phase', 'chinawal']):
                print(f, "->", img)
