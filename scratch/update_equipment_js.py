import re

with open('js/equipment.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Exact replacements for image and gallery for the 20 items:

replacements = {
    # 4. Swaraj 855 FE
    'tr-swaraj855': {
        'image': 'assets/images/equipment/swaraj-855-fe.jpg',
        'gallery': [
            'assets/images/equipment/swaraj-855-fe.jpg',
            'assets/images/equipment/tractor.jpg'
        ]
    },
    # 5. Rotavator
    'rot-48': {
        'image': 'assets/images/equipment/rotavator-tilling.jpg',
        'gallery': [
            'assets/images/equipment/rotavator-tilling.jpg',
            'assets/images/equipment/rotavator.jpg'
        ]
    },
    # 8. Disc Harrow
    'harrow-disc': {
        'image': 'assets/images/equipment/disc-harrow.jpg',
        'gallery': [
            'assets/images/equipment/disc-harrow.jpg',
            'assets/images/equipment/cultivator.jpg'
        ]
    },
    # 9. Dasmesh Happy Seeder
    'seed-super': {
        'image': 'assets/images/equipment/dasmesh-happy-seeder.jpg',
        'gallery': [
            'assets/images/equipment/dasmesh-happy-seeder.jpg',
            'assets/images/equipment/seed-drill.jpg'
        ]
    },
    # 10. Precision Planter
    'seed-planter': {
        'image': 'assets/images/equipment/precision-seed-planter.jpg',
        'gallery': [
            'assets/images/equipment/precision-seed-planter.jpg',
            'assets/images/equipment/dasmesh-happy-seeder.jpg'
        ]
    },
    # 11. Paddy Transplanter
    'paddy-transplant': {
        'image': 'assets/images/equipment/paddy-transplanter.jpg',
        'gallery': [
            'assets/images/equipment/paddy-transplanter.jpg',
            'assets/images/equipment/precision-seed-planter.jpg'
        ]
    },
    # 12. Mitra Sprayer
    'spray-500': {
        'image': 'assets/images/equipment/mitra-sprayer.jpg',
        'gallery': [
            'assets/images/equipment/mitra-sprayer.jpg',
            'assets/images/equipment/sprayer.jpg'
        ]
    },
    # 13. Boom Sprayer
    'spray-boom': {
        'image': 'assets/images/equipment/hydraulic-boom-sprayer.jpg',
        'gallery': [
            'assets/images/equipment/hydraulic-boom-sprayer.jpg',
            'assets/images/equipment/mitra-sprayer.jpg'
        ]
    },
    # 14. HTP Power Sprayer
    'spray-power': {
        'image': 'assets/images/equipment/htp-power-sprayer.jpg',
        'gallery': [
            'assets/images/equipment/htp-power-sprayer.jpg',
            'assets/images/equipment/mitra-sprayer.jpg'
        ]
    },
    # 15. Preet Harvester
    'harv-9000': {
        'image': 'assets/images/equipment/preet-987-harvester.jpg',
        'gallery': [
            'assets/images/equipment/preet-987-harvester.jpg',
            'assets/images/equipment/harvester.jpg'
        ]
    },
    # 16. Reaper Binder
    'reaper-bind': {
        'image': 'assets/images/equipment/reaper-binder.jpg',
        'gallery': [
            'assets/images/equipment/reaper-binder.jpg',
            'assets/images/equipment/preet-987-harvester.jpg'
        ]
    },
    # 17. Straw Baler
    'baler-straw': {
        'image': 'assets/images/equipment/round-hay-baler.jpg',
        'gallery': [
            'assets/images/equipment/round-hay-baler.jpg',
            'assets/images/equipment/preet-987-harvester.jpg'
        ]
    },
    # 18. Tipping Trailer
    'trail-8t': {
        'image': 'assets/images/equipment/hydraulic-tipping-trailer.jpg',
        'gallery': [
            'assets/images/equipment/hydraulic-tipping-trailer.jpg',
            'assets/images/equipment/trailer.jpg'
        ]
    },
    # 19. Mandi Trolley
    'trail-mandi': {
        'image': 'assets/images/equipment/mandi-grain-trolley.jpg',
        'gallery': [
            'assets/images/equipment/mandi-grain-trolley.jpg',
            'assets/images/equipment/hydraulic-tipping-trailer.jpg'
        ]
    },
    # 20. Water Pump
    'pump-10hp': {
        'image': 'assets/images/equipment/farm-irrigation-pump.jpg',
        'gallery': [
            'assets/images/equipment/farm-irrigation-pump.jpg',
            'assets/images/equipment/water-pump.jpg'
        ]
    }
}

new_content = content
for eq_id, data in replacements.items():
    # Regex to match this specific item block
    # from id: "eq_id" until features or specs
    pattern = rf'(id:\s*"{re.escape(eq_id)}",[\s\S]*?image:\s*")[^"]+("[\s\S]*?gallery:\s*\[)[\s\S]*?(\])'
    def repl(m):
        new_gal_str = ',\n      '.join([f'"{g}"' for g in data['gallery']])
        return f"{m.group(1)}{data['image']}{m.group(2)}\n      {new_gal_str}\n    {m.group(3)}"
    
    new_content, n = re.subn(pattern, repl, new_content, count=1)
    print(f"Updated {eq_id}: {n} replacement")

with open('js/equipment.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Saved js/equipment.js successfully!")
