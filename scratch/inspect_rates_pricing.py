import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all sections and their comments or headings
sections = re.findall(r'(<!--.*?SECTION.*?-->|<section.*?>)', text, re.IGNORECASE)
for s in sections[:25]:
    print(s[:100].strip())

print("\n--- ALL H1, H2, H3 ---")
headings = re.findall(r'<(h[1-3])[^>]*>(.*?)</\1>', text, re.DOTALL)
for tag, h in headings:
    clean = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h)).strip()
    print(f"[{tag.upper()}] {clean}")
