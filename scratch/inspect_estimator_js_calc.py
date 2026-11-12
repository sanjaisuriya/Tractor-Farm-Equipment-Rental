with open('js/pricing.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'// 2. Interactive Farmland Rental Cost.*', text, re.DOTALL)
if match:
    lines = match.group(0).split('\n')
    for line in lines[40:110]:
        print(line)
