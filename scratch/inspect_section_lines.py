with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in rates-pricing.html: {len(lines)}")
for idx, line in enumerate(lines, 1):
    if '<section' in line or '</section>' in line:
        print(f"Line {idx:4d}: {line.strip()[:90]}")
