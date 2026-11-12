with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec6_match = re.search(r'Seasonal Package Bundles.*?</section>', html, re.DOTALL)
if sec6_match:
    print(sec6_match.group(0)[:1500])
