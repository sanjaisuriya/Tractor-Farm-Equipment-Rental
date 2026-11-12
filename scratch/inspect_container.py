with open('equipment.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("IDs:", re.findall(r'id=["\'][^"\']*equipment[^"\']*["\']', html))

# Also let's check js/equipment.js for how cards are rendered into DOM
with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js = f.read()

for line in js.splitlines():
    if 'innerHTML' in line or 'append' in line or 'getElementById' in line or 'querySelector' in line:
        print("JS:", line)
