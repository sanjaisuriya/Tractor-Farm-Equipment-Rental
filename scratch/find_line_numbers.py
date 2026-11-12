with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if 'id="pricingPlans"' in l or 'id="transit"' in l:
        print(f"Line {i}: {l.strip()}")
