with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sec10 = re.search(r'<section id="faq".*?</section>', text, re.DOTALL)
if sec10:
    spans = re.findall(r'<div class="faq-header">\s*<span>(.*?)</span>', sec10.group(0))
    for s in spans:
        print("  -", s)
