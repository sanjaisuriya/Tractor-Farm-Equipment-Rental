import shutil

shutil.copy('scratch/tillage_downloads/field_ploughing_tractor.jpg', 'C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/vision_ploughing_1.jpg')
shutil.copy('scratch/tillage_downloads/tractor_ploughing_field_2.jpg', 'C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/vision_ploughing_2.jpg')
shutil.copy('scratch/downloaded_tests/national_agro_happy_seeder.jpg', 'C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/vision_seeder.jpg')
shutil.copy('scratch/candidates/punjab_wheat_prep.jpg', 'C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/vision_wheat_prep.jpg')

# Also copy the top candidate to assets/images/about/
shutil.copy('scratch/tillage_downloads/field_ploughing_tractor.jpg', 'assets/images/about/vision-sustainable-farming.jpg')
shutil.copy('scratch/tillage_downloads/tractor_ploughing_field_2.jpg', 'assets/images/about/vision-fleet-action.jpg')
shutil.copy('scratch/downloaded_tests/national_agro_happy_seeder.jpg', 'assets/images/about/vision-zero-till-seeder.jpg')
print("Copied all candidates successfully")
