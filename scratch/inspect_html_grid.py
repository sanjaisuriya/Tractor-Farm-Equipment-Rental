with open('equipment.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'equipmentGrid' in line:
        for i in range(max(0, idx - 5), min(len(lines), idx + 10)):
            print(f"{i+1}: {lines[i]}", end='')
