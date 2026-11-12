with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
left_col = re.search(r'<div class="lg:col-span-7 space-y-6">.*?</div>\s*<!-- Live Price', html, re.DOTALL)
right_col = re.search(r'<div class="lg:col-span-5 space-y-6">.*?(?=</div>\s*</div>\s*</section>)', html, re.DOTALL)

print("LEFT COLUMN:")
cards_left = re.findall(r'<div class="bg-white dark:bg-slate-800 rounded-2xl[^"]*"', left_col.group(0))
print(f"Total cards in left column: {len(cards_left)}")

print("\nRIGHT COLUMN:")
cards_right = re.findall(r'<div class="[^"]*(?:summary-card|rounded-2xl)[^"]*"', right_col.group(0))
print(f"Total cards in right column: {len(cards_right)}")
for c in re.findall(r'<h[34][^>]*>(.*?)</h[34]>', right_col.group(0), re.DOTALL):
    print("  Header:", re.sub(r'<[^>]+>', '', c).strip())
