import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js = f.read()

items = re.findall(r'id:\s*["\']([^"\']+)["\']\s*,\s*name:\s*["\']([^"\']+)["\']\s*,\s*category:\s*["\']([^"\']+)["\']\s*,\s*subCategory:\s*["\']([^"\']+)["\']', js)
for eq_id, name, cat, sub in items:
    print(f"[{cat:22s}] | [{sub:32s}] | {name}")
