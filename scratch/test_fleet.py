import os
from PIL import Image

f1 = 'assets/images/home-1/machinery-depot.jpg'
f2 = 'assets/images/about/vision-fleet.jpg'
f3 = 'assets/images/about/vision-fleet-action.jpg'

print(f1, Image.open(f1).size)
print(f2, Image.open(f2).size)
print(f3, Image.open(f3).size)
