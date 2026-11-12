import shutil
from PIL import Image

# Copy cleaned image to assets/images/equipment/paddy-transplanter.jpg
shutil.copy('scratch/test_cleaned_paddy.jpg', 'assets/images/equipment/paddy-transplanter.jpg')
print("Updated assets/images/equipment/paddy-transplanter.jpg")

# Also copy to artifact directory
artifact_dir = 'C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e'
shutil.copy('scratch/test_cleaned_paddy.jpg', f'{artifact_dir}/cleaned_paddy_transplanter.jpg')
shutil.copy('scratch/test_cleaned_crop.jpg', f'{artifact_dir}/cleaned_transplanter_crop.jpg')
print("Copied to artifact directory.")
