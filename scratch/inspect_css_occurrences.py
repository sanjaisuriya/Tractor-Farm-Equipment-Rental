with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's inspect where .pricing-card appears
import re
blocks = [m.start() for m in re.finditer(r'\.pricing-card\b', css)]
print(f"Total occurrences: {len(blocks)}")
