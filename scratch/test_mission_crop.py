from PIL import Image

im = Image.open('scratch/farmer_cultivating_punjab.jpg')
print('punjab cultivation size:', im.size)

# Crop to 1200x800 for mission section
w, h = im.size
target_aspect = 1200 / 800
target_w = int(h * target_aspect)
left = (w - target_w) // 2
crop = im.crop((left, 0, left + target_w, h)).resize((1200, 800), Image.Resampling.LANCZOS)
crop.save('scratch/punjab_mission_preview.jpg', quality=90)
print('Saved scratch/punjab_mission_preview.jpg')
