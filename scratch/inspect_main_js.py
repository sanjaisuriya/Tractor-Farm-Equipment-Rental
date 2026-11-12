with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'[^\n]*(?:tel|phone|mobile|name)[^\n]*', js, re.IGNORECASE)
print(f"Matches in main.js: {len(matches)}")
for m in matches[:10]:
    print("  ", m)
