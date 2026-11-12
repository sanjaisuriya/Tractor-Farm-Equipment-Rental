with open('booking.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if 'cultivator attachment ready' in l or 'instant deposit refund' in l or 'Machinery Booking' in l:
        print(f"Line {i}: {l.strip()}")
