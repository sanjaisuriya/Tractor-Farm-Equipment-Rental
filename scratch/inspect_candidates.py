import os
from PIL import Image

candidates = {
    'Hourly Rates - Indian tractor in field': [
        'assets/images/home-1/real_farmer_tractor_1.jpg',
        'assets/images/home-1/real_farmer_tractor_2.jpg',
        'assets/images/home-1/real_farmer_tractor_3.jpg',
        'assets/images/about/company-tractor.jpg',
        'assets/images/about/vision_tractor_field_cultivating.jpg',
        'assets/images/equipment/tractor-mahindra-415-real.jpg',
        'assets/images/equipment/swaraj-855-fe.jpg'
    ],
    'Daily Rates - Tractor with attached rotavator': [
        'assets/images/equipment/rotavator-tilling-real.jpg',
        'assets/images/equipment/rotavator-fleet-fresh.jpg',
        'assets/images/equipment/rotavator-tilling.jpg',
        'assets/images/equipment/cycle-phase-2-rotavator.jpg',
        'scratch/cand_rotavator_tilling_2.jpg'
    ],
    'Weekly Rental - Combine harvester working in paddy field': [
        'assets/images/equipment/preet-987-harvester.jpg',
        'assets/images/equipment/harvester-fleet-fresh.jpg',
        'assets/images/equipment/harvester.jpg',
        'assets/images/equipment/cycle-phase-5-harvesting.jpg',
        'scratch/muthuvara_paddy.jpg'
    ],
    'Monthly Season Pass - Multiple tractors and agricultural machinery': [
        'assets/images/home-1/machinery-depot.jpg',
        'assets/images/about/vision-fleet.jpg',
        'assets/images/about/vision-fleet-action.jpg',
        'assets/images/home-1/featured-machinery.jpg',
        'scratch/two_tractors_field.jpg'
    ]
}

for cat, files in candidates.items():
    print(f'=== {cat} ===')
    for f in files:
        if os.path.exists(f):
            im = Image.open(f)
            print(f'  {f}: size={im.size}, aspect={im.width/im.height:.2f}')
        else:
            print(f'  {f}: NOT FOUND')
