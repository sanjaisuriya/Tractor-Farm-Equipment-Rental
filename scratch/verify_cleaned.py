import numpy as np
from PIL import Image

im = Image.open('scratch/test_cleaned_paddy.jpg')
arr = np.array(im)

orange_pts = []
for y in range(450, 500):
    for x in range(540, 760):
        r, g, b = arr[y, x]
        if r > 160 and 80 < g < 160 and b < 50:
            orange_pts.append((y, x))

print(f"Remaining orange pixels in target region: {len(orange_pts)}")
