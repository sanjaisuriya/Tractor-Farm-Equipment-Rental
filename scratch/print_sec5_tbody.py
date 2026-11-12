with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec5_table = re.search(r'Standalone Farm Implement.*?</table>', html, re.DOTALL)
if sec5_table:
    tbody = re.search(r'<tbody[^>]*>(.*?)</tbody>', sec5_table.group(0), re.DOTALL)
    if tbody:
        print(tbody.group(0)[:2000])
