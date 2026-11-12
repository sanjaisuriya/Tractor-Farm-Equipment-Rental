with open('js/booking.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:50], start=1):
    print(f"Line {i}: {l.rstrip()}")
