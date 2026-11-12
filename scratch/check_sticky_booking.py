with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<div class="[^"]*sticky[^"]*"', html)
print("Sticky divs in booking.html:", matches)
