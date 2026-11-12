with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'[^\n]*scale[^\n]*', css)
print("Matches with scale in pricing.css:")
for m in matches:
    print(" -", m)

matches_featured = re.findall(r'(\.pricing-card\.featured[^{]*\{[^}]*\})', css)
print("\nMatches with .pricing-card.featured:")
for m in matches_featured:
    print(" -", m)
