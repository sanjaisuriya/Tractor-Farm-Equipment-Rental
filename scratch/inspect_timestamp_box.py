import numpy as np
from PIL import Image

im = Image.open('assets/images/equipment/paddy-transplanter.jpg')
arr = np.array(im)

# Let's find the exact bounding box of the timestamp "27/05/2011 15:10"
# In the previous run, Y was 293 to 484, X was 481 to 744. Let's see what is inside that crop:
crop = Image.open('scratch/timestamp_exact_crop.jpg')
print("Crop size:", crop.size)

# Let's find where the dense cluster of timestamp pixels is
for y in range(400, 520):
    row_oranges = []
    for x in range(400, 800):
        r, g, b = arr[y, x]
        if r > 160 and 80 < g < 160 and b < 50:
            row_oranges.append(x)
    if len(row_oranges) > 5:
        print(f"Row y={y}: orange xs from {min(row_oranges)} to {max(row_oranges)} (count={len(row_oranges)})")
