from PIL import Image

im = Image.open('scratch/punjab_happy_seeder.jpg')
w, h = im.size
print('Original:', w, h)

# Tractor and seeder bounds:
# x from ~350 to 900
# y from ~350 to 650
# Let's crop:
crop_box = (320, 320, 950, 320 + int(630 * 520 / 800))
cropped = im.crop(crop_box).resize((800, 520), Image.Resampling.LANCZOS)
cropped.save('scratch/punjab_happy_tight.jpg', quality=95)
print('Saved scratch/punjab_happy_tight.jpg')
