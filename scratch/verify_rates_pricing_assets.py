import os
import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all src="images/..."
srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
print(f"Total src images found: {len(srcs)}")
missing = []
for src in set(srcs):
    # Clean query parameters or anchors if any
    clean_src = src.split('?')[0].split('#')[0]
    if not os.path.exists(clean_src):
        missing.append(src)

if missing:
    print("MISSING IMAGES:", missing)
else:
    print("All image files exist!")

# Find all href links
hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
print(f"Total hrefs found: {len(hrefs)}")
missing_hrefs = []
for h in set(hrefs):
    if h.startswith('#') or h.startswith('tel:') or h.startswith('mailto:') or h.startswith('http'):
        continue
    clean_h = h.split('?')[0].split('#')[0]
    if not os.path.exists(clean_h):
        missing_hrefs.append(h)

if missing_hrefs:
    print("MISSING HREFS:", missing_hrefs)
else:
    print("All internal links exist!")
