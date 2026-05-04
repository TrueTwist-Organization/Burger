from PIL import Image

img_path = '/Users/jinal/Downloads/Food/burger.png'
original_img = Image.open(img_path).convert("RGBA")
width, height = original_img.size
pixels = original_img.load()

# Find rows that have at least some non-transparent pixels
has_content = [False] * height
for y in range(height):
    solid_pixels = 0
    for x in range(width):
        if pixels[x, y][3] > 50:  # Alpha > 50
            solid_pixels += 1
    
    if solid_pixels > width * 0.05:  # If more than 5% of the row has solid pixels
        has_content[y] = True

# Smooth the array to remove 1-pixel noise gaps
smoothed_content = list(has_content)
for y in range(1, height - 1):
    if not has_content[y] and has_content[y-1] and has_content[y+1]:
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

for i, (top, bottom) in enumerate(layers):
    if i < len(layer_names):
        name = layer_names[i]
        layer_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        slice_img = original_img.crop((0, top, width, bottom))
        layer_img.paste(slice_img, (0, top))
        layer_img.save('/Users/jinal/Downloads/Food/' + name)
        print(f"Saved {name} from {top} to {bottom}")
    else:
        print(f"Extra layer found from {top} to {bottom}")

print(f"Total layers detected: {len(layers)}")
