with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if 'tractorContactForm' in l:
        print(f"Line {i}:")
        for j in range(i-2, min(i+35, len(lines))):
            print(f"Line {j}: {lines[j-1].rstrip()}")
        break
