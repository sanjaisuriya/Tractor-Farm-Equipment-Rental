import re

with open('equipment.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Occurrences of '20' in equipment.html:")
for line in html.splitlines():
    if '20' in line and ('machine' in line.lower() or 'equipment' in line.lower() or 'catalog' in line.lower() or 'fleet' in line.lower() or 'model' in line.lower()):
        print("  HTML:", line.strip())

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("Occurrences of '20' in js/equipment.js:")
for line in js.splitlines():
    if '20' in line:
        print("  JS:", line.strip())
