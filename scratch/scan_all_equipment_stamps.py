import glob
import numpy as np
from PIL import Image

imgs = glob.glob('assets/images/equipment/*.jpg')
print(f"Scanning {len(imgs)} equipment images for digital date stamps...")

for p in imgs:
    im = Image.open(p)
    arr = np.array(im)
    h, w, _ = arr.shape
    # Check bottom 10%
    bottom = arr[int(h * 0.85):, :]
    # Check for bright orange/yellow text
    orange = (bottom[:, :, 0] > 180) & (bottom[:, :, 1] > 100) & (bottom[:, :, 2] < 50)
    # Check for bright green or white digital stamps
    green_stamp = (bottom[:, :, 1] > 200) & (bottom[:, :, 0] < 50) & (bottom[:, :, 2] < 50)
    
    cnt_orange = np.sum(orange)
    cnt_green = np.sum(green_stamp)
    
    if cnt_orange > 50 or cnt_green > 50:
        print(f"  FLAG: {p} (orange={cnt_orange}, green={cnt_green})")
print("Scan complete.")
