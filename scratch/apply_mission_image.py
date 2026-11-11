import os
from PIL import Image

src = 'scratch/downloaded_tests/punjab_farmer_cultivating.jpg'
dst = 'assets/images/about/mission-rotavator.jpg'

im = Image.open(src)
print('Source size:', im.size)

# Target: 1000 x 750 (4:3 aspect ratio matching h-[380px] to h-[430px])
target_w, target_h = 1000, 750
w, h = im.size
target_aspect = target_w / target_h
curr_aspect = w / h

if curr_aspect > target_aspect:
    new_w = int(h * target_aspect)
    left = (w - new_w) // 2
    crop = im.crop((left, 0, left + new_w, h))
else:
    new_h = int(w / target_aspect)
    top = (h - new_h) // 2
    crop = im.crop((0, top, w, top + new_h))

result = crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
result.save(dst, quality=90, optimize=True)
print(f'Successfully updated {dst}: {os.path.getsize(dst)/1024:.1f} KB')
