with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.rate-period-tab[^{]*\{[^}]*\})', css)
print("CSS rules for .rate-period-tab:")
for m in matches:
    print(m)
