with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[560:625], start=561):
    print(f"Line {i}: {l.rstrip()}")
