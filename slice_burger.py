from PIL import Image

# Load the image
img = Image.open('/Users/jinal/Downloads/Food/burger.png')
img = img.convert("RGBA")
width, height = img.size

# Define slice percentages (approximate heights for burger parts)
# Top bun: 0 to 30%
# Veggies: 30% to 50%
# Patty & Cheese: 50% to 75%
# Bottom Bun: 75% to 100%

slices = [
    ("layer1_topbun.png", 0, int(height * 0.35)),
    ("layer2_veggies.png", int(height * 0.35), int(height * 0.52)),
    ("layer3_patty.png", int(height * 0.52), int(height * 0.75)),
    ("layer4_bottombun.png", int(height * 0.75), height)
]

for name, top, bottom in slices:
    # crop(left, top, right, bottom)
    cropped_img = img.crop((0, top, width, bottom))
    cropped_img.save('/Users/jinal/Downloads/Food/' + name)

print("Sliced successfully!")
