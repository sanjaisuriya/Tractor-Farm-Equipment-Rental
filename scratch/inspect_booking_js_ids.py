with open('js/booking.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
ids = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', js)
print("IDs used in js/booking.js:")
print(set(ids))
