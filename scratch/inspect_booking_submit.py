with open('js/booking.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if 'addEventListener(\'submit\'' in l or 'addEventListener("submit"' in l:
        print(f"Submit at line {i}")
        for j in range(i, min(i+40, len(lines))):
            print(f"Line {j}: {lines[j-1].rstrip()}")
        break
