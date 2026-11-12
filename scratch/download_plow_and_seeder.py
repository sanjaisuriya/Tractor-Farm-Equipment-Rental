import urllib.request
from PIL import Image
import shutil

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}

urls = {
    'new_holland_plow': 'https://upload.wikimedia.org/wikipedia/commons/1/12/Tractor_New_Holland_T6.165_plowing_%28Zadobrova%2C_Ljubljana%29.jpg',
    'schaupflug_1232': 'https://upload.wikimedia.org/wikipedia/commons/a/a2/04-09-12-Schaupfl%C3%BCgen-Fahrenwalde-RalfR-IMG_1232.jpg',
    'jd_kuhn_plow': 'https://upload.wikimedia.org/wikipedia/commons/f/f7/John_Deere_tractor_with_Kuhn_plough%2C_Werktuigendagen_2005.jpg',
    'punjab_happy_seeder': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Agriculture_in_India_tractor_farming_Punjab_preparing_field_for_a_wheat_crop_without_burning_previous_crop_stalk.jpg'
}

for name, url in urls.items():
    dest = f'scratch/{name}.jpg'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        with open(dest, 'wb') as f:
            f.write(resp.read())
            
    im = Image.open(dest)
    w, h = im.size
    target_ratio = 800 / 520
    cur_ratio = w / h
    if cur_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        crop_box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        crop_box = (0, top, w, top + new_h)
    cropped = im.crop(crop_box).resize((800, 520), Image.Resampling.LANCZOS)
    cropped.save(f'scratch/preview_{name}.jpg', quality=95)
    shutil.copy(f'scratch/preview_{name}.jpg', rf'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\preview_{name}.jpg')
    print(f'Done {name}')
