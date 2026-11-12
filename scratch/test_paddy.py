import os
from PIL import Image

for p in ['scratch/mechanized_harvesting_kerala.jpg', 'scratch/agri_machinery_harvester_wb.jpg', 'scratch/crop_tiger_paddy_india.jpg']:
    im = Image.open(p)
    print(p, im.size)
