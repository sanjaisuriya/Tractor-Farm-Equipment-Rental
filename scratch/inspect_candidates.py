from PIL import Image

for name, path in [
    ('mahindra_in_india', 'scratch/farmers/mahindra_in_india.jpg'),
    ('north_india_tractor', 'scratch/farmers/north_india_tractor.jpg'),
    ('goa_driver', 'scratch/farmers/goa_tractor_driver.jpg'),
    ('cotton_farmer', 'scratch/downloaded_tests/cotton_farmer_haryana.jpg')
]:
    im = Image.open(path)
    print(name, im.size)
