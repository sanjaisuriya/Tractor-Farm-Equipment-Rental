import os
import re
import glob

used_imgs = {}
for html in glob.glob('*.html'):
    with open(html, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'(assets/images/[^\s"\'\)]+)', content)
    for m in matches:
        clean_m = m.strip("',;\"")
        used_imgs.setdefault(clean_m, set()).add(html)

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js_content = f.read()
for m in re.findall(r'(assets/images/[^\s"\'\)]+)', js_content):
    clean_m = m.strip("',;\"")
    used_imgs.setdefault(clean_m, set()).add('js/equipment.js')

print(f"Total unique referenced image paths: {len(used_imgs)}")
for p, files in sorted(used_imgs.items()):
    if 'equipment' in p or 'about' in p:
        print(f"{p:55} -> {list(files)}")
