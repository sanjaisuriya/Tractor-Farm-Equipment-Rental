with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's remove the first basic definition of .pricing-card if it's overridden below
import re
# Check occurrences
print("pricing-card occurrences:", len(re.findall(r'\.pricing-card\s*\{', css)))
