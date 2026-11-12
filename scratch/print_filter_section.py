with open('equipment.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(440, 505):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
