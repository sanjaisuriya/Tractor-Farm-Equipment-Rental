from PIL import Image, ImageEnhance
import shutil

im = Image.open('scratch/seeddrill4189.jpg')
# Original size: 4896 x 3672
# Tractor is located: right tire ~3500, front weight ~3650, top of cab ~1750, bottom of tires ~2650
# Seeder is located: left marker ~1200, left edge of drill ~1250, hopper top ~1700
# Machine bounds: X = 1200 to 3650 (width = 2450)
# Height for 800:520 ratio = 2450 / (800/520) = 1592
# Machine Y bounds: 1700 to 2700 (height = 1000). Center Y is around 2200.
# Y_top = 2200 - 1592/2 = 1404
# Y_bottom = 1404 + 1592 = 2996

crop = im.crop((1150, 1380, 1150 + 2500, 1380 + int(2500 * 520 / 800)))
resized = crop.resize((800, 520), Image.Resampling.LANCZOS)

# Enhance color and contrast to make it vibrant and bright
enh_b = ImageEnhance.Brightness(resized).enhance(1.06)
enh_c = ImageEnhance.Contrast(enh_b).enhance(1.08)
enh_s = ImageEnhance.Color(enh_c).enhance(1.15)

out_path = 'scratch/seeddrill_close_crop.jpg'
enh_s.save(out_path, quality=95)
shutil.copy(out_path, r'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\seeddrill_close_crop.jpg')
print('Done close crop')
