with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'INTERACTIVE FARMLAND RENTAL COST & ACREAGE ESTIMATOR.*?</section>', text, re.DOTALL)
if match:
    sec = match.group(0)
    for line in sec.split('\n'):
        if 'id=' in line or '<input' in line or '<select' in line or '<button' in line or '<span id=' in line:
            print(line.strip())
