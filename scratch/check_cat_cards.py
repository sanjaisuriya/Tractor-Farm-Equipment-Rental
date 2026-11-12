with open('equipment.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
categories = re.findall(r'<div class="equipment-category-card">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
for c in categories:
    badge = re.findall(r'<span>([^<]+)</span>', c)
    h3 = re.findall(r'<h3>([^<]+)</h3>', c)
    print(h3, badge)
