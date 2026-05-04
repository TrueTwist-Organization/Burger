from PIL import Image
import os

img_path = '/Users/jinal/Downloads/Food/burger.png'
original_img = Image.open(img_path).convert("RGBA")
width, height = original_img.size
pixels = original_img.load()

# Step 1: Make black background transparent
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # If the pixel is very dark, make it transparent
        if r < 15 and g < 15 and b < 15:
            pixels[x, y] = (0, 0, 0, 0)

# Step 2: Find horizontal sections with content
has_content = [False] * height
for y in range(height):
    solid_pixels = 0
    for x in range(width):
        if pixels[x, y][3] > 0:  # If pixel is not fully transparent
            solid_pixels += 1
    
    # If there are at least some visible pixels, mark row as having content
    if solid_pixels > width * 0.02:
        has_content[y] = True

# Smooth the array to avoid splitting a single layer because of a small gap
smoothed_content = list(has_content)
for y in range(2, height - 2):
    if not has_content[y]:
        # If it's a small gap of 1-3 pixels between content, fill it
        if has_content[y-2] and has_content[y+2]:
            smoothed_content[y] = True

has_content = smoothed_content

layers = []
in_layer = False
start_y = 0

for y in range(height):
    if has_content[y] and not in_layer:
        in_layer = True
        start_y = y
    elif not has_content[y] and in_layer:
        in_layer = False
        layers.append((start_y, y))

if in_layer:
    layers.append((start_y, height))

layer_names = [
    "layer1_topbun.png",
    "layer2_lettuce.png",
    "layer3_tomatoes.png",
    "layer4_onions.png",
    "layer5_pickles.png",
    "layer6_cheese.png",
    "layer7_patty.png",
    "layer8_bottombun.png"
]

print(f"Total layers detected: {len(layers)}")

for i, (top, bottom) in enumerate(layers):
    if i < len(layer_names):
        name = layer_names[i]
        # Keep original image size but only the content of this layer
        layer_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        slice_img = original_img.crop((0, top, width, bottom))
        layer_img.paste(slice_img, (0, top))
        layer_img.save('/Users/jinal/Downloads/Food/' + name)
        print(f"Saved {name} from {top} to {bottom}")
    else:
        print(f"Extra layer found from {top} to {bottom}")

original_img.save('/Users/jinal/Downloads/Food/burger_transparent.png')
print("Saved full transparent burger as burger_transparent.png")
