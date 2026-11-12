import os
import glob
from PIL import Image

image_files = glob.glob('assets/images/**/*.jpg', recursive=True) + glob.glob('assets/images/**/*.png', recursive=True)
print(f"Total images found: {len(image_files)}")

# Let's inspect the target thumbnail first
target = Image.open('C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/.user_uploaded/media_1794473669623_dbb83481.png')
print(f"Target size: {target.size}, mode: {target.mode}")

# We know it has paddy field seedlings / rice transplanter or similar!
# Let's check images related to paddy, transplanter, seeder, kharif, etc.
keywords = ['paddy', 'transplant', 'seed', 'kharif', 'pump', 'plough', 'irrigation']
candidates = [f for f in image_files if any(k in f.lower() for k in keywords)]
print(f"Candidate images with keywords: {candidates}")

for c in candidates:
    im = Image.open(c)
    print(f"  {c}: size={im.size}")
