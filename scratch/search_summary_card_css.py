import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.css') or file.endswith('.html') or file.endswith('.js'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'booking-summary-card' in content:
                        print(f"Match in: {filepath}")
                        # find css rules if css
                        if file.endswith('.css'):
                            matches = re.findall(r'(\.booking-summary-card[^{]*\{[^}]*\})', content)
                            for m in matches:
                                print("   CSS:", m)
            except Exception as e:
                pass
