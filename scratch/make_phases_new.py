from PIL import Image, ImageEnhance
import shutil

# 1. Phase 1: Reversible MB Plough (jd_kuhn_plow.jpg, 3008x2000)
im_plow = Image.open('scratch/jd_kuhn_plow.jpg')
# Machine bounds:
# Tractor is at x=800..1500, plow is at x=1300..2500
# Machine spans x from ~800 to 2500 (width = 1700), Y is around 600..1300
# For 800:520 (1.538):
# Let's crop width 2100 -> height = 2100 / 1.538 = 1365
# Left = 650, Top = 450
crop_plow = im_plow.crop((650, 450, 650 + 2100, 450 + 1365)).resize((800, 520), Image.Resampling.LANCZOS)
b1 = ImageEnhance.Brightness(crop_plow).enhance(1.04)
c1 = ImageEnhance.Contrast(b1).enhance(1.06)
s1 = ImageEnhance.Color(c1).enhance(1.10)
s1.save('scratch/phase1_plough_new.jpg', quality=95)
shutil.copy('scratch/phase1_plough_new.jpg', r'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\phase1_plough_new.jpg')

# 2. Phase 3: Seed Drill (tortella.jpg, 3008x2000)
# We already have scratch/tortella_focus_seeder.jpg which focuses directly on the seed drill and tractor
im_seeder = Image.open('scratch/tortella_focus_seeder.jpg')
im_seeder.save('scratch/phase3_seeder_new.jpg', quality=95)
shutil.copy('scratch/phase3_seeder_new.jpg', r'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\phase3_seeder_new.jpg')

print('Generated phase1_plough_new.jpg and phase3_seeder_new.jpg')
