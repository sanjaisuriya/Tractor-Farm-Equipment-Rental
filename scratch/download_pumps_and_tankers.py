import urllib.request
from PIL import Image
import shutil

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}

urls = {
    'pump_vrindavan_1': 'https://upload.wikimedia.org/wikipedia/commons/9/94/Agricultural_irrigation_pump_set_with_borewell%2C_Vrindavan%2C_Uttar_Pradesh%2C_India.jpg',
    'pump_vrindavan_2': 'https://upload.wikimedia.org/wikipedia/commons/9/92/Agricultural_irrigation_pump_set_with_borewell%2C_Vrindavan%2C_Uttar_Pradesh%2C_India_02.jpg',
    'pump_paddy': 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Diesel_Pump_Using_in_the_Paddy_Fields.jpg',
    'tractor_tanker': 'https://upload.wikimedia.org/wikipedia/commons/f/f2/A_Tractor_fitted_with_Water_tanker.jpg'
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
