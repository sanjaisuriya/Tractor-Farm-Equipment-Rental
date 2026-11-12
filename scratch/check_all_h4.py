import glob
import re

for f in glob.glob('**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines):
        if '<h4' in line and 'text-white' not in line:
            # check if inside a dark container
            context = ''.join(lines[max(0, idx - 10):idx])
            if 'bg-forest' in context or 'bg-emerald-900' in context or 'bg-slate-900' in context:
                print(f"{f}:{idx+1}: {line.strip()}")
