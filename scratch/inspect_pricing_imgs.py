import re, os

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|webp|svg))["\']', text)
print(f"Total img tags in rates-pricing.html: {len(imgs)}")
for i in set(imgs):
    exists = os.path.exists(i)
    sz = os.path.getsize(i) if exists else 0
    print(f"  {'[OK]' if exists else '[MISSING]'} {i} ({sz} bytes)")
