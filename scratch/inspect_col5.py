with open('booking.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[385:460], start=386):
    print(f"Line {i}: {l.rstrip()}")
