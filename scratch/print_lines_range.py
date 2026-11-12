with open('js/pricing.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(20, 40):
    print(f"{i+1}: {repr(lines[i])}")
