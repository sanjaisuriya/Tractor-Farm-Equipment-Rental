import re

with open("js/equipment.js", "r", encoding="utf-8") as f:
    text = f.read()

items = re.findall(r'id:\s*"([^"]+)",\s*name:\s*"([^"]+)",(?:.|\n)*?image:\s*"([^"]+)"', text)
for idx, (item_id, name, img) in enumerate(items, 1):
    print(f"{idx}. [{item_id}] {name} --> {img}")
