import shutil

# Overwrite trailer.jpg with the genuine agricultural tractor-trailer image
shutil.copy("assets/images/equipment/tractor-trailer-real.jpg", "assets/images/equipment/trailer.jpg")

# Overwrite sprayer.jpg with the real tractor-mounted boom sprayer image
shutil.copy("assets/images/equipment/agricultural-sprayer-real.jpg", "assets/images/equipment/sprayer.jpg")

print("Updated trailer.jpg and sprayer.jpg in assets/images/equipment/")
