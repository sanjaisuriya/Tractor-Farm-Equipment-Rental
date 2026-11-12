with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m3 = re.search(r'<section id="pricingPlans".*?</section>', text, re.DOTALL)
if m3:
    lines = m3.group(0).split('\n')
    print(f"Total lines in Section 3: {len(lines)}")
    for line in lines:
        if '<h3' in line or 'dynamic-price-value' in line or 'pricing-card' in line or 'data-card-period' in line:
            print(line.strip())
