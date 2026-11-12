with open('js/equipment.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(830, 885):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
