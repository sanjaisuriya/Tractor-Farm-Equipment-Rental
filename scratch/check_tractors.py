import os
from PIL import Image

imgs = [
    'assets/images/home-1/real_farmer_tractor_1.jpg',
    'assets/images/home-1/real_farmer_tractor_2.jpg',
    'assets/images/home-1/real_farmer_tractor_3.jpg',
    'assets/images/about/company-tractor.jpg',
    'assets/images/about/vision_tractor_field_cultivating.jpg'
]

for img in imgs:
    im = Image.open(img)
    print(img, im.size, im.format)
