with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[415:475], start=416):
    print(f"Line {i}: {l.rstrip()}")
