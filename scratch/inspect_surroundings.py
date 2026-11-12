from PIL import Image

im = Image.open('assets/images/equipment/paddy-transplanter.jpg')
# Let's crop a window around the timestamp: y from 420 to 510, x from 520 to 770
crop_region = im.crop((520, 420, 770, 510))
crop_region.save('scratch/timestamp_surroundings.jpg')
print("Saved scratch/timestamp_surroundings.jpg")
