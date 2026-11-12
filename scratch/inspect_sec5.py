with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec5 = re.search(r'Standalone Farm Implement.*?</table>', html, re.DOTALL)
if sec5:
    print(sec5.group(0)[:2500])
