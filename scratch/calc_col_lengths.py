# Let's check the current content in left column vs right column in booking.html
with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
left_col = re.search(r'<div class="lg:col-span-7[^"]*">.*?</div>\s*<!-- Live Price', html, re.DOTALL)
right_col = re.search(r'<div class="lg:col-span-5[^"]*">.*?(?=</div>\s*</div>\s*</section>)', html, re.DOTALL)

print("Left column length (chars):", len(left_col.group(0)) if left_col else 0)
print("Right column length (chars):", len(right_col.group(0)) if right_col else 0)
