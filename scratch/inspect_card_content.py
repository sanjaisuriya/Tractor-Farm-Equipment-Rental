import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'id:\s*["\']([^"\']+)["\'],\s*name:\s*["\']([^"\']+)["\'],.*?hp:\s*["\']([^"\']+)["\'],.*?shortDesc:\s*["\']([^"\']+)["\']'
items = re.findall(pattern, text, re.DOTALL)

for eq_id, name, hp, desc in items:
    print(f"{eq_id:15} | Name ({len(name):2}c): {name[:32]:32} | HP ({len(hp):2}c): {hp:25} | Desc: {len(desc)}c")
