import os
from PIL import Image

# Let's inspect the existing files in assets/images/
files = [
    ('Hourly', 'assets/images/home-1/real_farmer_tractor_1.jpg'),
    ('Rotavator', 'assets/images/equipment/rotavator-tilling-real.jpg'),
    ('Preet Harvester', 'assets/images/equipment/preet-987-harvester.jpg'),
    ('Paddy Harvester Kerala', 'scratch/mechanized_harvesting_kerala.jpg'),
    ('Paddy Harvester Crop Tiger', 'scratch/crop_tiger_paddy_india.jpg'),
    ('Machinery Depot', 'assets/images/home-1/machinery-depot.jpg'),
    ('Vision Fleet', 'assets/images/about/vision-fleet.jpg')
]

for name, path in files:
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{name}: {path} -> {im.size}, ratio={im.width/im.height:.2f}")
