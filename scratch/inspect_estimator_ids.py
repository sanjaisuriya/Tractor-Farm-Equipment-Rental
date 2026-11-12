import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find estimator section
sec2_match = re.search(r'id="estimator".*?</section>', html, re.DOTALL)
if sec2_match:
    sec2 = sec2_match.group(0)
    ids = re.findall(r'id="([^"]+)"', sec2)
    print("Estimator IDs found:", ids)
else:
    print("No section with id='estimator' found. Looking for calc IDs...")
    calc_ids = re.findall(r'id="(calc[^"]+)"', html)
    print("calc IDs found:", calc_ids)
