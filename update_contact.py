import os

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_end_str = '</main>'
idx_end = content.find(main_end_str)
post_main = content[idx_end + len(main_end_str):]

print("Post-main starts with:")
print(post_main[:300])
print("="*40)
print("Post-main ends with:")
print(post_main[-400:])
