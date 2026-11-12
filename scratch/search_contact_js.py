import os

for root, dirs, files in os.walk('js'):
    for file in files:
        if 'contact' in file:
            print(os.path.join(root, file))
