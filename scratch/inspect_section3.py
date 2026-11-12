with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m3 = re.search(r'<section id="pricingPlans".*?</section>', text, re.DOTALL)
if m3:
    sec = m3.group(0)
    cards = re.findall(r'<div class="pricing-card.*?</div>\s*</div>\s*</div>', sec, re.DOTALL)
    print(f"Found {len(cards)} pricing cards in Section 3")
    # print card titles and prices
    titles = re.findall(r'<h3[^>]*>(.*?)</h3>', sec)
    prices = re.findall(r'<span class="dynamic-price-value[^"]*"[^>]*>(.*?)</span>', sec)
    labels = re.findall(r'<span class="dynamic-period-label"[^>]*>(.*?)</span>', sec)
    for t, p, l in zip(titles, prices, labels):
        print(f"  {t.strip()} | {p.strip()} {l.strip()}")
