with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
right_col_end = re.search(r'<!-- Verified Farmer Testimonial Card -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>', html, re.DOTALL)
if right_col_end:
    print("Found right_col_end:")
    print(right_col_end.group(0))
else:
    print("Not found with this exact regex, let's find the closing of lg:col-span-5")
    pos = html.find('Verified Farmer Testimonial Card')
    print(html[pos:pos+1500])
