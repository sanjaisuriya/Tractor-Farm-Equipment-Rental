from PIL import Image

im = Image.open('assets/images/equipment/paddy-transplanter.jpg')
print("Image size:", im.size)

# Crop the bottom right area where timestamps usually appear (e.g. bottom 15% of the image)
w, h = im.size
bottom_right = im.crop((w - 250, h - 80, w, h))
bottom_right.save('scratch/transplanter_bottom_right.jpg')

# Also check bottom left, top right, etc.
bottom_left = im.crop((0, h - 80, 250, h))
bottom_left.save('scratch/transplanter_bottom_left.jpg')

print("Saved crops.")
