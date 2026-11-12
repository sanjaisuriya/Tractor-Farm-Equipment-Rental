with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

header_part = text[:text.find('<section class="site-hero-banner')]
footer_part = text[text.find('</section>\n\n    <!-- SITE FOOTER -->'):]

print("Header part length:", len(header_part))
print("Footer part length:", len(footer_part))
print("Footer part starts with:", repr(footer_part[:100]))
