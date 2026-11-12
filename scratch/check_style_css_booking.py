with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.booking-summary-card[^{]*\{[^}]*\})', css)
print("booking-summary-card in style.css:", matches)
