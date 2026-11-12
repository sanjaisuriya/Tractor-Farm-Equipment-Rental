import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

for el_id in ['calcInclusionExplain', 'calcCostLabel', 'calcInclusionBadge']:
    m = re.search(r'id="' + el_id + r'[^>]*>(.*?)</(?:p|span|div)>', html, re.DOTALL)
    if m:
        print(f"--- {el_id} ---")
        print(m.group(0))
