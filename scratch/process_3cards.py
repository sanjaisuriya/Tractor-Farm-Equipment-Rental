from PIL import Image
import os, hashlib

brain_dir = "C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e"

def crop_and_save(src_path, filename):
    im = Image.open(src_path)
    target_w, target_h = 800, 520
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
    
    dst_assets = os.path.join("assets/images/equipment", filename)
    dst_brain = os.path.join(brain_dir, filename)
    cropped.save(dst_assets, "JPEG", quality=90)
    cropped.save(dst_brain, "JPEG", quality=90)
    print(f"Processed & saved {filename} ({target_w}x{target_h})")

crop_and_save("mahindra_415.jpg", "tractor-mahindra-415-real.jpg")
crop_and_save("vst_mini_tractor.jpg", "mini-tractor-vst-real.jpg")
crop_and_save("scratch/downloaded_tests/punjab_farmer_cultivating.jpg", "rotavator-tilling-real.jpg")
