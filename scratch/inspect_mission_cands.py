from PIL import Image

files = [
    'scratch/downloaded_tests/punjab_farmer_cultivating.jpg',
    'scratch/farmers/mahindra_farmers_of_india.jpg',
    'scratch/farmers/mahindra_in_india.jpg',
    'scratch/real_field/sugar_cane_farmers.jpg',
    'scratch/real_field/chinawal_ploughing_1.jpg'
]

for f in files:
    try:
        im = Image.open(f)
        print(f, im.size, im.mode)
    except Exception as e:
        print(f, 'Error:', e)
