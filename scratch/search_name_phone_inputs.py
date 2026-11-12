import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(r'<input[^>]*(?:name|phone|mobile|tel)[^>]*>', content, re.IGNORECASE)
                if matches:
                    print(f"File {filepath}:")
                    for m in matches:
                        print("  ", m)
