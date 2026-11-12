from PIL import Image
import os

brain_dir = "C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e"

def process_and_save(src_path, filename):
    im = Image.open(src_path)
    # Target 1200x900 (4:3) or 1200x800 (3:2)
    target_w, target_h = 1200, 900
    target_ratio = target_w / target_h
    im_ratio = im.width / im.height
    
    if im_ratio > target_ratio:
        new_w = int(target_ratio * im.height)
        left = (im.width - new_w) // 2
        box = (left, 0, left + new_w, im.height)
    else:
        new_h = int(im.width / target_ratio)
        top = (im.height - new_h) // 2
        box = (0, top, im.width, top + new_h)
        
    cropped = im.crop(box).resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    dst_assets = os.path.join("assets/images/about", filename)
    dst_brain = os.path.join(brain_dir, filename)
    cropped.save(dst_assets, "JPEG", quality=92)
    cropped.save(dst_brain, "JPEG", quality=92)
    print(f"Processed & saved {filename}: {target_w}x{target_h}")

process_and_save("scratch/farmers/mahindra_in_india.jpg", "farmer-doorstep-support.jpg")
process_and_save("scratch/farmers/north_india_tractor.jpg", "farmer-service-guarantee.jpg")
process_and_save("scratch/downloaded_tests/cotton_farmer_haryana.jpg", "farmer-field-operator.jpg")
