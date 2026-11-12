with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
form_match = re.search(r'<div class="lg:col-span-7[^"]*">.*?</div>\s*<!-- Live Price', html, re.DOTALL)
if form_match:
    print(form_match.group(0)[:1500])
    print("\n... End of form ...\n")
    print(form_match.group(0)[-500:])
