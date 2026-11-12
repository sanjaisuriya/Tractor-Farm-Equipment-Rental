with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec6_match = re.search(r'Seasonal Package Bundles.*?</section>', html, re.DOTALL)
cards = re.findall(r'<div class="bundle-card.*?</a>\s*</div>', sec6_match.group(0), re.DOTALL)
for i, c in enumerate(cards):
    print(f"--- Bundle {i+1} ---")
    h3 = re.search(r'<h3[^>]*>(.*?)</h3>', c, re.DOTALL)
    p = re.search(r'<p[^>]*>(.*?)</p>', c, re.DOTALL)
    print("H3:", h3.group(1).strip() if h3 else "")
    print("P:", p.group(1).strip() if p else "")
