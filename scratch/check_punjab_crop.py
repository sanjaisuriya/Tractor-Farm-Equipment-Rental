from PIL import Image

im = Image.open('scratch/farmer_cultivating_punjab.jpg')
w, h = im.size
print("Original size:", w, h)
# Try different anchor or crop positions if needed
