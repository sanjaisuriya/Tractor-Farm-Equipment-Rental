with open('js/equipment-details.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'renderCard' in line:
        for i in range(max(0, idx - 5), min(len(lines), idx + 35)):
            print(f"{i+1}: {lines[i]}", end='')
