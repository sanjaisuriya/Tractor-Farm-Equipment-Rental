with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
imgs = re.findall(r'src="(assets/images/[^"]+)"', text)
for i in sorted(set(imgs)):
    print(f'about.html uses: {i}')
