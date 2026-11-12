from PIL import Image

files = [
    'assets/images/about/about-hero-banner.jpg',
    'assets/images/equipment/equipment-hero-banner.jpg',
    'scratch/farmer_working_field_tractor_wide.jpg',
    'scratch/harvester_wheat_field.jpg',
    'scratch/farmer_tractor_tilling.jpg',
    'scratch/two_tractors_field.jpg'
]

for f in files:
    im = Image.open(f)
    print(f, im.size)
