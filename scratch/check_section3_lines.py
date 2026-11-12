with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[120:250], start=121):
    if 'pricing-card' in l or 'pricing-price' in l or 'dynamic-price-value' in l or 'pricing-features' in l:
        print(f"Line {i}: {l.strip()}")
