import glob
import numpy as np
from PIL import Image

# The timestamp text color in the uploaded image is orange/yellow with a dark outline.
target = Image.open('C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/.user_uploaded/media_1794473669623_dbb83481.png').convert('RGB')
t_arr = np.array(target)

# Let's sample the orange pixels: R > 180, G > 100, B < 50
orange_mask = (t_arr[:, :, 0] > 180) & (t_arr[:, :, 1] > 100) & (t_arr[:, :, 2] < 50)
print(f"Target has {np.sum(orange_mask)} orange pixels")

all_imgs = glob.glob('assets/images/**/*.jpg', recursive=True)
for path in all_imgs:
    try:
        im = Image.open(path).convert('RGB')
        arr = np.array(im)
        # Check bottom 20%
        h, w, _ = arr.shape
        bottom_region = arr[int(h * 0.75):, :]
        mask = (bottom_region[:, :, 0] > 180) & (bottom_region[:, :, 1] > 100) & (bottom_region[:, :, 2] < 50)
        count = np.sum(mask)
        if count > 50:
            print(f"MATCH: {path} has {count} orange timestamp-like pixels in bottom region!")
    except Exception as e:
        pass
