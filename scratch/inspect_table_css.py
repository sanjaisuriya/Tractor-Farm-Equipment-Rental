with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.pricing-table[^{]*\{[^}]*\})', css)
print("pricing-table rules in pricing.css:")
for m in matches:
    print(m)
