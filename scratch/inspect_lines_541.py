with open('booking.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[540:600], start=541):
    print(f"Line {i}: {l.rstrip()}")
