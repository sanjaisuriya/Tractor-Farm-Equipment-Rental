with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# In Section 6:
# 1. replace `<h3 class="text-lg font-bold text-slate-900 dark:text-white mb-1.5 leading-snug">` with `<h3 class="bundle-title text-lg font-bold text-slate-900 dark:text-white mb-1.5 leading-snug">`
# 2. replace `<p class="text-xs text-muted mb-3 font-medium">` with `<p class="bundle-included text-xs text-muted mb-3 font-medium">`
# 3. replace `<div class="mb-4 pb-3 border-b border-gray-100 dark:border-gray-800">` in bundle cards with `<div class="bundle-price-block mb-4 pb-3 border-b border-gray-100 dark:border-gray-800">`
# 4. replace `<ul class="space-y-2 text-xs text-slate-600 dark:text-slate-300 mb-6">` in bundle cards with `<ul class="bundle-features space-y-2 text-xs text-slate-600 dark:text-slate-300 mb-6">`

sec6_match = re.search(r'(Seasonal Package Bundles.*?)(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 items-stretch">)(.*?)(</div>\s*</div>\s*</section>)', html, re.DOTALL)

if sec6_match:
    bundles_html = sec6_match.group(3)
    bundles_html = bundles_html.replace('<h3 class="text-lg font-bold text-slate-900 dark:text-white mb-1.5 leading-snug">', '<h3 class="bundle-title text-lg font-bold text-slate-900 dark:text-white mb-1.5 leading-snug">')
    bundles_html = bundles_html.replace('<p class="text-xs text-muted mb-3 font-medium">', '<p class="bundle-included text-xs text-muted mb-3 font-medium">')
    bundles_html = bundles_html.replace('<div class="mb-4 pb-3 border-b border-gray-100 dark:border-gray-800">', '<div class="bundle-price-block mb-4 pb-3 border-b border-gray-100 dark:border-gray-800">')
    bundles_html = bundles_html.replace('<ul class="space-y-2 text-xs text-slate-600 dark:text-slate-300 mb-6">', '<ul class="bundle-features space-y-2 text-xs text-slate-600 dark:text-slate-300 mb-6">')
    
    new_html = html[:sec6_match.start(3)] + bundles_html + html[sec6_match.end(3):]
    with open('rates-pricing.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated Section 6 bundle classes in rates-pricing.html successfully!")
else:
    print("Could not match Section 6!")
