from PIL import Image, ImageEnhance
import shutil

# 1. Process farm-irrigation-pump.jpg
im_pump = Image.open('scratch/pump_paddy.jpg')
# (1152, 864)
# Diesel pump is centered.
# Target 800x520 -> aspect ratio 1.538
# Height available = 864. Max width for 864 = 864 * 1.538 = 1329 (larger than 1152)
# Width available = 1152. Height needed = 1152 / 1.538 = 749.
# Y crop from (864 - 749) // 2 = 57 to 57 + 749
crop_pump = im_pump.crop((0, 50, 1152, 50 + 749)).resize((800, 520), Image.Resampling.LANCZOS)
# Enhance brightness and color slightly
enh_b = ImageEnhance.Brightness(crop_pump).enhance(1.05)
enh_c = ImageEnhance.Contrast(enh_b).enhance(1.08)
enh_s = ImageEnhance.Color(enh_c).enhance(1.12)
enh_s.save('scratch/processed_pump.jpg', quality=95)
shutil.copy('scratch/processed_pump.jpg', r'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\processed_pump.jpg')

# 2. Process water-tanker-trolley.jpg
im_tanker = Image.open('scratch/tractor_tanker.jpg')
# (2560, 1920)
# Tractor is in front right, tanker is in back left.
# Width = 2560, Height = 1920.
# Height for width 2560 = 2560 / 1.538 = 1664
# Y bounds: (1920 - 1664) // 2 = 128
crop_tanker = im_tanker.crop((0, 120, 2560, 120 + 1664)).resize((800, 520), Image.Resampling.LANCZOS)
enh_tb = ImageEnhance.Brightness(crop_tanker).enhance(1.04)
enh_tc = ImageEnhance.Contrast(enh_tb).enhance(1.06)
enh_ts = ImageEnhance.Color(enh_tc).enhance(1.15)
enh_ts.save('scratch/processed_tanker.jpg', quality=95)
shutil.copy('scratch/processed_tanker.jpg', r'C:\Users\Sanjai\.gemini\antigravity\brain\043b14ed-505b-4860-b100-d2e67549e96e\processed_tanker.jpg')

print('Processed pump and tanker images successfully.')
