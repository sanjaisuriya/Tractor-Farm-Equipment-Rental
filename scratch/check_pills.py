with open('equipment.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
pills = re.findall(r'<button[^>]*category-pill[^>]*>.*?</button>', html, re.DOTALL)
for p in pills:
    print(p.strip())
