with open('booking.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[396:465], start=397):
    print(f"Line {i}: {l.rstrip()}")
