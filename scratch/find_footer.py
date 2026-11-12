with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<footer', text, re.IGNORECASE)]
print("Footer positions:", matches)
if matches:
    print(text[matches[0]:matches[0]+300])
