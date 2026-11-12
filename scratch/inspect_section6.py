import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find Section 6 content
match = re.search(r'SEASONAL MULTI-OPERATION PACKAGE BUNDLES.*?</section>', text, re.DOTALL)
if match:
    sec = match.group(0)
    print("Length of Section 6:", len(sec))
    # print first 50 lines
    for line in sec.split('\n')[:50]:
        print(line)
