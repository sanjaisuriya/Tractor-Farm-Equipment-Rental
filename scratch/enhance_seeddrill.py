from PIL import Image, ImageEnhance

# Crop seeddrill tightly around tractor + seeder
im_seed = Image.open('scratch/seeddrill4189.jpg')
# Machine bounds: x from ~900 to 4400, y from ~1300 to 3000
# Let's crop x: 950 to 4550 (width 3600), height = 3600 / (800/520) = 2340
# y from 1000 to 3340
crop = im_seed.crop((950, 950, 950 + 3600, 950 + 2340)).resize((800, 520), Image.Resampling.LANCZOS)

# Enhance brightness slightly by 1.08, contrast by 1.10, color saturation by 1.15 to make it look fresh and vibrant
enh_b = ImageEnhance.Brightness(crop).enhance(1.08)
enh_c = ImageEnhance.Contrast(enh_b).enhance(1.10)
enh_s = ImageEnhance.Color(enh_c).enhance(1.18)

enh_s.save('scratch/seeddrill_vibrant.jpg', quality=95)
print('Saved scratch/seeddrill_vibrant.jpg')
