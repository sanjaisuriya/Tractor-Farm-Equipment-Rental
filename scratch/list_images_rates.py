import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', html)
for src, alt in imgs:
    print(f"SRC: {src:40} | ALT: {alt}")
