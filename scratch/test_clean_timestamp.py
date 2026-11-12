import numpy as np
from PIL import Image, ImageFilter

im = Image.open('assets/images/equipment/paddy-transplanter.jpg')
arr = np.array(im, dtype=np.float32)

# The timestamp is at y=465..486, x=550..748
# Let's see what rows are above it: y=435..456, x=550..748 is clean flooded paddy field!
# And below it: y=490..510, x=550..748 is also clean flooded paddy field!

# Let's create an inpaint mask for the timestamp text
# The timestamp text has characters with orange fill and dark gray outline
# Let's inspect the exact box [464:487, 554:748]
target_box = arr[464:487, 554:748]

# A mask of text pixels: orange pixels OR very dark edge pixels that outline the digits
r = target_box[:, :, 0]
g = target_box[:, :, 1]
b = target_box[:, :, 2]

# Orange fill condition
orange = (r > 150) & (g > 75) & (b < 60)
# Dark outline condition in this region
dark_outline = (r < 70) & (g < 70) & (b < 70)

text_mask = orange | dark_outline
print("Text mask pixels:", np.sum(text_mask))

# Let's test a clean patch replacement:
# The patch right above (y=438..461, x=554..748) has exact same lighting, water angle, and muddy texture!
patch_above = arr[438:461, 554:748].copy()

# If we blend patch_above into [464:487, 554:748] with smooth edge feathering:
cleaned = arr.copy()

# Let's create a smooth alpha mask for [462:489, 552:750]
y1, y2 = 462, 489
x1, x2 = 552, 750

# Source patch from y=434..461, x=552..750 (same height: 27px, width: 198px)
src_patch = arr[434:461, x1:x2].copy()

# Add a slight subtle gradient or noise match so it blends imperceptibly
# Feather top and bottom 3 pixels, left and right 4 pixels
mask = np.ones((y2 - y1, x2 - x1, 1), dtype=np.float32)
for i in range(4):
    alpha = (i + 1) / 5.0
    mask[i, :, :] *= alpha
    mask[-(i + 1), :, :] *= alpha
for j in range(5):
    alpha = (j + 1) / 6.0
    mask[:, j, :] *= alpha
    mask[:, -(j + 1), :] *= alpha

blended = (1.0 - mask) * arr[y1:y2, x1:x2] + mask * src_patch
cleaned[y1:y2, x1:x2] = blended

res_im = Image.fromarray(np.clip(cleaned, 0, 255).astype(np.uint8))
res_im.save('scratch/test_cleaned_paddy.jpg', quality=95)

# Save close-up crop
crop = res_im.crop((520, 420, 770, 510))
crop.save('scratch/test_cleaned_crop.jpg')
print("Saved test_cleaned_paddy.jpg and test_cleaned_crop.jpg")
