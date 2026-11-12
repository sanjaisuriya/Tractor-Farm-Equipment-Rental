import shutil
import os

brain_dir = "C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e"

files = [
    ("scratch/farmers/mahindra_farmers_of_india.jpg", "real_farmer_tractor_1.jpg"),
    ("scratch/farmers/along_with_tractor.jpg", "real_farmer_tractor_2.jpg"),
    ("scratch/downloaded_tests/punjab_farmer_cultivating.jpg", "real_farmer_tractor_3.jpg"),
    ("scratch/farmers/goa_tractor_driver.jpg", "real_farmer_tractor_4.jpg"),
    ("scratch/farmers/north_india_tractor.jpg", "real_farmer_tractor_5.jpg")
]

for src, name in files:
    if os.path.exists(src):
        dst_brain = os.path.join(brain_dir, name)
        dst_assets = os.path.join("assets/images/home-1", name)
        shutil.copy(src, dst_brain)
        shutil.copy(src, dst_assets)
        print(f"Copied {src} -> {name}")
