with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec4_match = re.search(r'Tractor Specifications & Price Matrix.*?(<div class="[^"]*">.*?<table.*?</table>\s*</div>)', html, re.DOTALL)
if sec4_match:
    print("Found sec4 container:", sec4_match.group(1)[:200])
else:
    print("Not found!")
