with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec3 = re.search(r'id="pricingPlans".*?</section>', html, re.DOTALL)
if sec3:
    print(sec3.group(0))
