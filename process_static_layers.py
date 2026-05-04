import os
from PIL import Image

layers = [
    "layer1_topbun.png",
    "layer2_lettuce.png",
    "layer3_tomatoes.png",
    "layer4_onions.png",
    "layer5_pickles.png",
    "layer6_cheese.png",
    "layer7_patty.png",
    "layer8_bottombun.png"
]

target_max_width = 400

# First, find the bounding box of the entire burger to find the true max width of the visual elements
combined_bbox = None

cropped_data = []

for layer in layers:
    img = Image.open(layer).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        cropped_data.append((layer, cropped))

# The actual width of the burger is the width of the widest layer (usually patty or bun)
max_original_width = max(c.width for _, c in cropped_data)

# Calculate scale factor
scale_factor = target_max_width / max_original_width

for layer_name, cropped in cropped_data:
    new_width = int(cropped.width * scale_factor)
    new_height = int(cropped.height * scale_factor)
    resized = cropped.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    new_name = "static_" + layer_name
    resized.save(new_name)
    print(f"Saved {new_name} ({new_width}x{new_height})")
