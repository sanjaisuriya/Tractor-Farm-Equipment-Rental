with open('js/equipment.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(880, 955):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
