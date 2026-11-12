import os
import re
import hashlib
from PIL import Image

def verify_all():
    print("=" * 40)
    print("1. CHECKING ALL IMAGES IN equipment.html")
    print("=" * 40)
    
    with open('equipment.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    img_srcs = set(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html))
    css_urls = set(re.findall(r'url\(["\']?([^"\')]+)["\']?\)', html))
    
    all_refs = img_srcs.union(css_urls)
    for ref in sorted(all_refs):
        if ref.startswith(('http', 'data:', '#')):
            continue
        clean_ref = ref.split('?')[0].split('#')[0]
        if os.path.exists(clean_ref):
            sz = os.path.getsize(clean_ref)
            print(f"  [OK] {clean_ref} ({sz} bytes)")
        else:
            print(f"  [FAIL] {clean_ref} does not exist!")
            return False
            
    print(f"PASSED: All images in equipment.html exist!\n")

    print("=" * 40)
    print("2. CHECKING ALL EQUIPMENT CARDS IN js/equipment.js")
    print("=" * 40)
    
    with open('js/equipment.js', 'r', encoding='utf-8') as f:
        js = f.read()
        
    items = re.findall(r'\{[^{]*?id:\s*["\']([^"\']+)["\'].*?name:\s*["\']([^"\']+)["\'].*?image:\s*["\']([^"\']+)["\']', js, re.DOTALL)
    print(f"Found {len(items)} equipment cards:")
    
    hashes = {}
    for idx, (eq_id, name, img_path) in enumerate(items, 1):
        if not os.path.exists(img_path):
            print(f"  [FAIL] #{idx} {name} -> Image {img_path} NOT FOUND!")
            return False
            
        with open(img_path, 'rb') as fp:
            h = hashlib.md5(fp.read()).hexdigest()
            
        im = Image.open(img_path)
        sz_bytes = os.path.getsize(img_path)
        
        if h in hashes:
            print(f"  [FAIL] DUPLICATE IMAGE DETECTED! Card #{idx} ({name}) has same image hash as Card #{hashes[h][0]} ({hashes[h][1]})")
            return False
            
        hashes[h] = (idx, name, img_path)
        print(f"  {idx:2d}. [{eq_id:15s}] {name[:35]:35s} | {im.size} | {sz_bytes:7d} B | {img_path}")
        
    print(f"PASSED: All {len(items)} equipment cards have 100% UNIQUE images!\n")
    return True

if __name__ == '__main__':
    verify_all()
