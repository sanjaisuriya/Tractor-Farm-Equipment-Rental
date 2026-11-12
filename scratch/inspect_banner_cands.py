import os
from PIL import Image

candidates = [
    'scratch/farmer_working_field_tractor_wide.jpg',
    'scratch/farmer_tractor_tilling.jpg',
    'scratch/farm_machine_tilling.jpg',
    'assets/images/about/about-hero-banner.jpg',
    'assets/images/contact/contact-hero-banner.jpg',
    'assets/images/equipment/final-cta-tractor.jpg',
    'assets/images/home-1/hero-tractor.jpg',
    'assets/images/about/vision-fleet-action.jpg'
]

for c in candidates:
    if os.path.exists(c):
        im = Image.open(c)
        print(f"{c}: {im.size}, ratio={im.width/im.height:.2f}")
