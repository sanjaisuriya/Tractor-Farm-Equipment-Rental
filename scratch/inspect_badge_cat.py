with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.badge-cat[^{]*\{[^}]*\})', css)
print("badge-cat in style.css:", matches)

with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    pcss = f.read()
matches2 = re.findall(r'(\.badge-cat[^{]*\{[^}]*\})', pcss)
print("badge-cat in pricing.css:", matches2)
