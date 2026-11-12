with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', html)
print("Scripts in contact.html:", scripts)
inline_scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Inline scripts in contact.html: {len(inline_scripts)}")
