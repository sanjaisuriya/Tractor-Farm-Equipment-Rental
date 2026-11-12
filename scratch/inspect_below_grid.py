with open('booking.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[455:530], start=456):
    print(f"Line {i}: {l.rstrip()}")
