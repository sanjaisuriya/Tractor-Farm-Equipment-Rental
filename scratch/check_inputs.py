import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        if 'type="tel"' in line or ('name' in line.lower() and '<input' in line.lower()):
            print(f"{f}:{i+1} -> {line.strip()[:100]}")
