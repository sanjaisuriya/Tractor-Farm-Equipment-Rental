with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec4 = re.search(r'Tractor Specifications & Price Matrix.*?</table>', html, re.DOTALL)
if sec4:
    print(sec4.group(0)[:2500])
