from PIL import Image

# Load the new separated image
img_path = '/Users/jinal/Downloads/Food/burger_transparent.png'
original_img = Image.open(img_path).convert("RGBA")
width, height = original_img.size

# Make black background transparent
pixels = original_img.load()
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # Using a slightly higher threshold in case of compression artifacts
        if r < 15 and g < 15 and b < 15:
            pixels[x, y] = (0, 0, 0, 0)

# Define slices (Top Y, Bottom Y) approx based on standard exploding burgers
slices = [
    ("layer1_topbun.png", 0, int(height * 0.18)),
    ("layer2_lettuce.png", int(height * 0.18), int(height * 0.30)),
    ("layer3_tomatoes.png", int(height * 0.30), int(height * 0.42)),
    ("layer4_onions.png", int(height * 0.42), int(height * 0.50)),
    ("layer5_pickles.png", int(height * 0.50), int(height * 0.58)),
    ("layer6_cheese.png", int(height * 0.58), int(height * 0.66)),
    ("layer7_patty.png", int(height * 0.66), int(height * 0.83)),
    ("layer8_bottombun.png", int(height * 0.83), height)
]

for name, top, bottom in slices:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    slice_img = original_img.crop((0, top, width, bottom))
    layer.paste(slice_img, (0, top))
    layer.save('/Users/jinal/Downloads/Food/' + name)

print("Sliced separated image perfectly with original dimensions!")
