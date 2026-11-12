with open('contact.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if 'id="contactName"' in l or 'id="contactPhone"' in l:
        print(f"Line {i}: {l.rstrip()}")
