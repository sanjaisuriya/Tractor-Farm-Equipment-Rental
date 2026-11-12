from PIL import Image
import os

brain_dir = "C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e"

def crop_and_save(src, name):
    im = Image.open(src)
    # calculate target aspect ratio 16:10 or 3:2 (1200x800)
    target_w, target_h = 1200, 800
    target_ratio = target_w / target_h
    im_ratio = im.width / im.height
    
    if im_ratio > target_ratio:
        # image is wider
        new_w = int(target_ratio * im.height)
        left = (im.width - new_w) // 2
        box = (left, 0, left + new_w, im.height)
    else:
        # image is taller
        new_h = int(im.width / target_ratio)
        top = (im.height - new_h) // 2
        box = (0, top, im.width, top + new_h)
        
    cropped = im.crop(box).resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    dst_brain = os.path.join(brain_dir, name)
    dst_assets = os.path.join("assets/images/about", name)
    cropped.save(dst_brain, "JPEG", quality=90)
    cropped.save(dst_assets, "JPEG", quality=90)
    print(f"Saved {name}: {target_w}x{target_h}")

crop_and_save("mahindra_india.jpg", "vision_mahindra_india.jpg")
crop_and_save("tractor_cultivating.jpg", "vision_tractor_field_cultivating.jpg")
crop_and_save("new_holland_plowing.jpg", "vision_modern_plowing.jpg")
crop_and_save("mahindra_415.jpg", "vision_mahindra_red.jpg")
