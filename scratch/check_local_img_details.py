import glob, os

files = [
    'assets/images/home-1/real_farmer_tractor_1.jpg',
    'assets/images/home-1/real_farmer_tractor_2.jpg',
    'assets/images/home-1/real_farmer_tractor_3.jpg',
    'assets/images/about/company-tractor.jpg',
    'assets/images/about/mission-rotavator.jpg',
    'assets/images/equipment/rotavator-tilling-real.jpg',
    'assets/images/equipment/rotavator-fleet-fresh.jpg',
    'assets/images/equipment/rotavator-tilling.jpg',
    'assets/images/equipment/preet-987-harvester.jpg',
    'assets/images/equipment/harvester-fleet-fresh.jpg',
    'assets/images/equipment/harvester.jpg',
    'assets/images/home-1/machinery-depot.jpg',
    'assets/images/about/vision-fleet.jpg',
    'assets/images/about/vision-fleet-action.jpg'
]

for f in files:
    if os.path.exists(f):
        size = os.path.getsize(f)
        print(f"{f}: size={size} bytes")
