with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sec8 = re.search(r'TRANSPARENT INCLUSIONS VS EXCLUSIONS.*?</section>', text, re.DOTALL)
if sec8:
    print("=== Section 8 ===")
    for line in sec8.group(0).split('\n')[:35]:
        print(line)

sec9 = re.search(r'KISAN CREDIT CARD.*?</section>', text, re.DOTALL)
if sec9:
    print("\n=== Section 9 ===")
    for line in sec9.group(0).split('\n')[:35]:
        print(line)

sec10 = re.search(r'<section id="faq".*?</section>', text, re.DOTALL)
if sec10:
    print("\n=== Section 10 FAQ ===")
    questions = re.findall(r'<button[^>]*class="faq-header[^"]*"[^>]*>(.*?)</button>', sec10.group(0), re.DOTALL)
    for q in questions:
        print("  Q:", re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', q)).strip())

sec11 = re.search(r'<section class="py-16 bg-forest.*?</section>', text, re.DOTALL)
if sec11:
    print("\n=== Section 11 CTA ===")
    print(sec11.group(0))
