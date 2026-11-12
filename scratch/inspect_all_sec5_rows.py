with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec5_match = re.search(r'Standalone Farm Implement.*?</table>', html, re.DOTALL)
rows = re.findall(r'<tr[^>]*>.*?</tr>', sec5_match.group(0), re.DOTALL)
print(f"Total rows in Section 5: {len(rows)}")
for i, r in enumerate(rows):
    cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.DOTALL)
    cleaned = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
    print(f"Row {i}: {cleaned}")
