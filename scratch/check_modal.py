with open('equipment.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<div id="equipmentDetailsModal".*?</div>\s*</div>\s*</div>\s*</div>', html, re.DOTALL)
if matches:
    print(matches[0][:800])
