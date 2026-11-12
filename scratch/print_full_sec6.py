with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec6_match = re.search(r'Seasonal Package Bundles.*?id="transit"', html, re.DOTALL)
if not sec6_match:
    sec6_match = re.search(r'Seasonal Package Bundles.*?</section>', html, re.DOTALL)

print(sec6_match.group(0))
