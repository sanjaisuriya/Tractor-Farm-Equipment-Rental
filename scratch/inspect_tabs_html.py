import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

tabs = re.findall(r'<button[^>]*class="[^"]*rate-period-tab[^"]*"[^>]*>.*?</button>', html, re.DOTALL)
print(f"Found {len(tabs)} tabs:")
for t in tabs:
    print(t)
