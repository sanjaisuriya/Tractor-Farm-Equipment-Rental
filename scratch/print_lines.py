with open('equipment.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(270, 390):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
