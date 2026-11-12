import os
from PIL import Image

imgs = {
    'farmer_working_field_tractor_wide': 'scratch/farmer_working_field_tractor_wide.jpg',
    'farmer_cultivating_punjab': 'scratch/farmer_cultivating_punjab.jpg',
    'plowing_land_india': 'scratch/plowing_land_india.jpg',
    'two_tractors_field': 'scratch/two_tractors_field.jpg',
    'about_hero_banner': 'assets/images/about/about-hero-banner.jpg',
    'existing_booking_banner': 'assets/images/booking/booking-banner.jpg',
    'hero_tractor': 'assets/images/home-1/hero-tractor.jpg'
}

for name, path in imgs.items():
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{name}: {path} -> {im.size}, ratio={im.width/im.height:.2f}")
