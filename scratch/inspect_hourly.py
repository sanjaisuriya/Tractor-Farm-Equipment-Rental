import os
from PIL import Image

imgs = {
    'tractor_punjab_1': 'assets/images/home-1/real_farmer_tractor_1.jpg',
    'tractor_punjab_3': 'assets/images/home-1/real_farmer_tractor_3.jpg',
    'swaraj_855': 'assets/images/equipment/swaraj-855-fe.jpg',
    'mahindra_415': 'assets/images/equipment/tractor-mahindra-415-real.jpg',
    'company_tractor': 'assets/images/about/company-tractor.jpg'
}

for k, v in imgs.items():
    if os.path.exists(v):
        im = Image.open(v)
        print(f"{k} ({v}): {im.size}, {im.format}")
