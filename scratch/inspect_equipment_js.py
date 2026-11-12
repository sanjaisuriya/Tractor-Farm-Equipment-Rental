with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\([^\)]*\)', js)
print("Functions in js/equipment.js:", funcs)

# Check categories list
cats = re.findall(r'categories\s*=\s*\[[^\]]+\]', js)
print("Categories:", cats)
