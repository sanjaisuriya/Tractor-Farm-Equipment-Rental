with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Lines 205-220:")
for i in range(204, 220):
    print(f"{i+1}: {repr(lines[i])}")

print("\nLines 1255-1275:")
for i in range(1254, min(1275, len(lines))):
    print(f"{i+1}: {repr(lines[i])}")
