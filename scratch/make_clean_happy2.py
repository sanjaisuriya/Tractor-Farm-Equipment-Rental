from PIL import Image, ImageEnhance
import shutil

im = Image.open('scratch/punjab_happy_seeder.jpg')
# (1280, 848)
w_crop = 660
h_crop = int(w_crop * 520 / 800) # 429
left = 390
top = 315
crop = im.crop((left, top, left + w_crop, top + h_crop)).resize((800, 520), Image.Resampling.LANCZOS)

# Enhance brightness and color slightly
b = ImageEnhance.Brightness(crop).enhance(1.05)
c = ImageEnhance.Contrast(b).enhance(1.08)
s = ImageEnhance.Color(c).enhance(1.15)

out = 'scratch/happy_seeder_clean2.jpg'
s.save(out, quality=95)
shutil.copy(out, r'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\happy_seeder_clean2.jpg')
print('Saved clean happy seeder 2')
