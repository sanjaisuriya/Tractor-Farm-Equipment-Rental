with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
# Find item 20
matches = re.findall(r'(\{[^\{]*id:\s*[\'\"]pump-10hp[\'\"].*?\n  \})', js, re.DOTALL)
if matches:
    print(matches[0])
