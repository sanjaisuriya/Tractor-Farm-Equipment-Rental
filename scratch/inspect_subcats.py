import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'id:\s*["\']([^"\']+)["\'].*?name:\s*["\']([^"\']+)["\'].*?category:\s*["\']([^"\']+)["\'].*?subCategory:\s*["\']([^"\']+)["\']'
matches = re.findall(pattern, text, re.DOTALL)

print(f"Total matched items: {len(matches)}")
for eq_id, name, cat, sub in matches:
    print(f"{eq_id:15} | Cat: {cat:20} | Sub: {sub}")
