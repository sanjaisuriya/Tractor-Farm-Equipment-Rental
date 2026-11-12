with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
pos = css.find('.form-textarea')
print(css[pos-100:pos+250])
