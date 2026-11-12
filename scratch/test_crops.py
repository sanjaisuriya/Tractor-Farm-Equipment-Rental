from PIL import Image

# For tortella.jpg (3008x2000)
# Tractor and seeder are horizontally from ~300 to 2900, vertically from ~150 to 1100
im_tort = Image.open('scratch/tortella.jpg')
# Let's crop x from 250 to 2950 (width = 2700), height for 800:520 ratio = 2700 * 520 / 800 = 1755
# or height from 100 to 1250 (height = 1150), width = 1150 * 800 / 520 = 1769
# Let's crop tight around the machine:
# Machine bounding box approx: left=300, top=120, right=2920, bottom=1150
# Width=2620, Height=1030
# To get 800:520 (1.538):
# If width=2620, height needed = 2620 / 1.538 = 1703
# Center Y between 120 and 1150 is ~635.
# Top = 635 - 1703//2 = 635 - 851 = -216 -> too tall for the image!
# So width is constrained by height:
# Height available around machine: from y=50 to y=1350 (height=1300)
# Width for height 1300 = 1300 * 1.538 = 2000
# Center around seeder and tractor rear:
# Let's do a crop focusing on the seed drill and tractor rear-to-mid:
crop1 = im_tort.crop((200, 100, 200 + int(1200 * 800/520), 100 + 1200)).resize((800, 520), Image.Resampling.LANCZOS)
crop1.save('scratch/tortella_focus_seeder.jpg', quality=95)

# Also let's test full machine crop:
# If height is from 100 to 1900 (height 1800):
# width = 1800 * 800 / 520 = 2769
# X from 120 to 2889
crop2 = im_tort.crop((120, 100, 120 + 2769, 100 + 1800)).resize((800, 520), Image.Resampling.LANCZOS)
crop2.save('scratch/tortella_full_machine.jpg', quality=95)

# For seeddrill4189 (4896x3672)
im_seed = Image.open('scratch/seeddrill4189.jpg')
# The tractor and HORSCH seeder are centered vertically around y=1800 to 2600, x=1200 to 3600
# Let's do a tight crop on the machine:
# Width around 2600 -> height = 2600 / 1.538 = 1690
crop3 = im_seed.crop((1100, 1400, 1100 + 2600, 1400 + 1690)).resize((800, 520), Image.Resampling.LANCZOS)
crop3.save('scratch/seeddrill_tight.jpg', quality=95)

print('Crops generated successfully.')
