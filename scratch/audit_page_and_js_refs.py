import re

print("=== Checking equipment.html ===")
with open('equipment.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'(assets/images/[^\s"\'\)]+)', text):
    print(m.group(1))

print("\n=== Checking js/equipment.js ===")
with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

for m in re.finditer(r'"(assets/images/[^"]+)"', js_text):
    print(m.group(1))
