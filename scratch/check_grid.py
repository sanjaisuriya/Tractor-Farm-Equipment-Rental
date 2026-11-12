import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    content = f.read()

items = re.findall(r"id:\s*['\"]([^'\"]+)['\"]\s*,\s*name:\s*['\"]([^'\"]+)['\"]\s*,\s*category:\s*['\"]([^'\"]+)['\"]", content)
print('Total equipment items:', len(items))
for idx, (id, name, cat) in enumerate(items, 1):
    print(f'{idx:2d}. [{cat:12s}] ({id:15s}) {name}')
