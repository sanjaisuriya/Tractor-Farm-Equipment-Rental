import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Check all shortDesc to see if any exceed 3 lines (~160 chars)
pattern = r'id:\s*["\']([^"\']+)["\'],\s*name:\s*["\']([^"\']+)["\'],.*?shortDesc:\s*["\']([^"\']+)["\']'
items = re.findall(pattern, text, re.DOTALL)

for eq_id, name, desc in items:
    print(f"[{eq_id:15}] ({len(desc):3d} chars): {desc}")
