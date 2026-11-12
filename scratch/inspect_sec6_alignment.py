with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec6 = re.search(r'Seasonal Package Bundles.*?id="transit"', html, re.DOTALL)
if sec6:
    print(sec6.group(0)[:2000])
