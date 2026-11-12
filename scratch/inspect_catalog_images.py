import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'id:\s*"([^"]+)",\s*name:\s*"([^"]+)",[\s\S]*?image:\s*"([^"]+)",\s*gallery:\s*\[([\s\S]*?)\]'
for idx, (eq_id, name, img, gal) in enumerate(re.findall(pattern, text), 1):
    gal_imgs = [g.strip(' "\t\r\n,') for g in gal.split('\n') if g.strip(' "\t\r\n,')]
    print(f"{idx:2}. [{eq_id:15}] {name[:40]:40} | img: {img}")
    print(f"    gallery: {gal_imgs}")
