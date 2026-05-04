from PIL import Image

img = Image.open('wow_yummy_transparent.png')

# Crop WOW (Approx top right quarter)
# Left, Upper, Right, Lower
wow_box = (550, 50, 1000, 400)
wow_img = img.crop(wow_box)
wow_img.save('wow_bubble.png')

# Crop YUMMY (Approx middle right)
yummy_box = (650, 450, 1024, 750)
yummy_img = img.crop(yummy_box)
yummy_img.save('yummy_bubble.png')

print("Extracted wow_bubble.png and yummy_bubble.png")
