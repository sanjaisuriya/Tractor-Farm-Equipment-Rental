with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<input[^>]*id="booking(?:FarmerName|Mobile)"[^>]*>', html)
for m in matches:
    print(m)
