from PIL import Image

# Load the original image
img_path = '/Users/jinal/Downloads/Food/burger.png'
original_img = Image.open(img_path).convert("RGBA")
width, height = original_img.size

# Define slices (Top Y, Bottom Y)
slices = [
    ("layer1_topbun.png", 0, int(height * 0.35)),
    ("layer2_veggies.png", int(height * 0.35), int(height * 0.52)),
    ("layer3_patty.png", int(height * 0.52), int(height * 0.75)),
    ("layer4_bottombun.png", int(height * 0.75), height)
]

for name, top, bottom in slices:
    # Create a completely transparent image of the same size
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    # Crop the slice from original
    slice_img = original_img.crop((0, top, width, bottom))
    # Paste the slice into the transparent image at the exact same position
    layer.paste(slice_img, (0, top))
    # Save the layer
    layer.save('/Users/jinal/Downloads/Food/' + name)

print("Sliced perfectly with original dimensions!")
