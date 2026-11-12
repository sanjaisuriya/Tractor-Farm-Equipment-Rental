import numpy as np
from PIL import Image

im = Image.open('assets/images/equipment/paddy-transplanter.jpg')
arr = np.array(im)
h, w, _ = arr.shape

# Let's search where the orange pixels are located in paddy-transplanter.jpg
# Target orange color:
target = Image.open('C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/.user_uploaded/media_1794473669623_dbb83481.png').convert('RGB')
t_arr = np.array(target)

# Find coordinates of orange pixels in paddy-transplanter.jpg
orange_pts = []
for y in range(h):
    for x in range(w):
        r, g, b = arr[y, x]
        if r > 180 and 90 < g < 160 and b < 50:
            orange_pts.append((y, x))

if orange_pts:
    min_y = min(p[0] for p in orange_pts)
    max_y = max(p[0] for p in orange_pts)
    min_x = min(p[1] for p in orange_pts)
    max_x = max(p[1] for p in orange_pts)
    print(f"FOUND orange timestamp in paddy-transplanter.jpg!")
    print(f"Y range: {min_y} to {max_y} (height {h})")
    print(f"X range: {min_x} to {max_x} (width {w})")
    
    # Save a crop around it
    crop = im.crop((max(0, min_x - 30), max(0, min_y - 30), min(w, max_x + 30), min(h, max_y + 30)))
    crop.save('scratch/timestamp_exact_crop.jpg')
    print("Saved scratch/timestamp_exact_crop.jpg")
else:
    print("No orange points matched the strict condition in paddy-transplanter.jpg")
