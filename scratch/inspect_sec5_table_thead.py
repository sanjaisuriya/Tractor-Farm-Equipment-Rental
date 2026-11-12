with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
sec5_table = re.search(r'Standalone Farm Implement.*?</table>', html, re.DOTALL)
if sec5_table:
    # Print the thead
    thead = re.search(r'<thead>.*?</thead>', sec5_table.group(0), re.DOTALL)
    if thead:
        print("THEAD:")
        print(thead.group(0))
