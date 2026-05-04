from PIL import Image

img_path = '/Users/jinal/Downloads/Food/burger_transparent.png'
original_img = Image.open(img_path).convert("RGBA")
width, height = original_img.size
pixels = original_img.load()

# Step 2: Find horizontal sections with content
has_content = [False] * height
for y in range(height):
    solid_pixels = 0
    for x in range(width):
        if pixels[x, y][3] > 0:  # If pixel is not fully transparent
            solid_pixels += 1
    
    # If there are at least some visible pixels, mark row as having content
    if solid_pixels > width * 0.01:
        has_content[y] = True

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

for i, (top, bottom) in enumerate(layers):
    print(f"Layer {i+1}: {top} to {bottom} (height {bottom - top})")
