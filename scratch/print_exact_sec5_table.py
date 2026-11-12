with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec5_match = re.search(r'Standalone Farm Implement.*?</table>', html, re.DOTALL)
print(sec5_match.group(0))
