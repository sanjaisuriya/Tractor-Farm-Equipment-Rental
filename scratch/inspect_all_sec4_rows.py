with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec4_match = re.search(r'Tractor Specifications & Price Matrix.*?</table>', html, re.DOTALL)
rows = re.findall(r'<tr[^>]*>.*?</tr>', sec4_match.group(0), re.DOTALL)
print(f"Total rows in Section 4: {len(rows)}")
for i, r in enumerate(rows):
    cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.DOTALL)
    cleaned = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
    print(f"Row {i}: {cleaned}")
