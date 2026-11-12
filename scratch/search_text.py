import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'cultivator attachment ready' in content or 'instant deposit refund' in content or 'Machinery Booking' in content:
                        print(f"Found match in: {filepath}")
            except Exception as e:
                pass
