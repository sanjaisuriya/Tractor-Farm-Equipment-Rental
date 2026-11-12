with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<div class="bundle-card.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
print(f"Found {len(matches)} bundle cards")
for i, m in enumerate(matches):
    print(f"--- Bundle {i+1} ---")
    print(m[:400])
