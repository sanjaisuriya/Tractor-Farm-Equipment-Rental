with open('equipment.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'bg-forest' in line:
        for j in range(idx, min(len(lines), idx + 25)):
            if '<h' in lines[j]:
                print(f"Line {j+1}: {lines[j].strip()}")
