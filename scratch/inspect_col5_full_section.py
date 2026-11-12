with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
col5_match = re.search(r'<!-- Live Price Calculation Summary \(Col 5\) -->.*?</section>', html, re.DOTALL)
if col5_match:
    print(col5_match.group(0)[:1500])
