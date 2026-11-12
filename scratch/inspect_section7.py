with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m7 = re.search(r'Certified Operator & Transit Charges.*?</section>', text, re.DOTALL)
if m7:
    sec = m7.group(0)
    for line in sec.split('\n')[:50]:
        print(line)
