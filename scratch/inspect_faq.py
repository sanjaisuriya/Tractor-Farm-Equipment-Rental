with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sec10 = re.search(r'<section id="faq".*?</section>', text, re.DOTALL)
if sec10:
    for line in sec10.group(0).split('\n'):
        if 'class="faq' in line or '<h' in line or '<span' in line and '?' in line:
            print(line.strip())
