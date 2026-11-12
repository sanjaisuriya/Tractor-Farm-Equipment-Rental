with open('booking.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[140:410], start=141):
    if '<section' in l or '</section>' in l or 'grid' in l or 'col-' in l or '<form' in l or '</form>' in l or 'id=' in l or 'sidebar' in l or 'summary' in l.lower():
        print(f"Line {i}: {l.strip()}")
