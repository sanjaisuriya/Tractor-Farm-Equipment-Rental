with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec6_match = re.search(r'Seasonal Package Bundles.*?id="transit"', html, re.DOTALL)
if not sec6_match:
    sec6_match = re.search(r'Seasonal Package Bundles.*?</section>', html, re.DOTALL)

cards = re.findall(r'<div class="bundle-card.*?</a>\s*</div>', sec6_match.group(0), re.DOTALL)
print(f"Found {len(cards)} bundle cards")
for i, c in enumerate(cards):
    print(f"\n=== Bundle Card {i+1} ===")
    title = re.search(r'<h3[^>]*>(.*?)</h3>', c, re.DOTALL)
    price = re.search(r'₹[\d,]+', c)
    savings = re.search(r'Save ₹[\d,]+', c)
    print("Title:", title.group(1).strip() if title else "N/A")
    print("Price:", price.group(0) if price else "N/A")
    print("Savings:", savings.group(0) if savings else "N/A")
