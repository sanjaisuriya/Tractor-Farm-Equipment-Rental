# Find where it was downloaded from by checking files in scratch
import os

with open('scratch/farmers/mahindra_farmers_of_india.jpg', 'rb') as f:
    data = f.read()

# Check EXIF
from PIL import Image, ExifTags
im = Image.open('scratch/farmers/mahindra_farmers_of_india.jpg')
exif = im.getexif()
for k, v in exif.items():
    tag = ExifTags.TAGS.get(k, k)
    print(tag, ':', v)

print('--- punjab_farmer_cultivating ---')
im2 = Image.open('scratch/downloaded_tests/punjab_farmer_cultivating.jpg')
for k, v in im2.getexif().items():
    tag = ExifTags.TAGS.get(k, k)
    print(tag, ':', v)
