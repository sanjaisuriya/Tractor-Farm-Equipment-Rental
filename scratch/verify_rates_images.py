import re, os

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total images found in rates-pricing.html: {len(images)}")
missing = []
for img in images:
    if not os.path.exists(img):
        missing.append(img)
    else:
        print(f"OK: {img}")

if missing:
    print("MISSING IMAGES:", missing)
else:
    print("ALL IMAGES EXIST PERFECTLY!")
