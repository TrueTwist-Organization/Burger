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

cropped_images = []
for layer in layers:
    img = Image.open(layer).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        cropped_images.append(cropped)

# Calculate dimensions
max_width = max(img.width for img in cropped_images)

# We want the centers of the images to be evenly spaced.
# Let's define the spacing between centers.
# The tallest image is likely the top bun or patty.
max_height = max(img.height for img in cropped_images)

center_spacing = max_height + 20  # gap

total_height = center_spacing * (len(cropped_images) - 1) + cropped_images[0].height//2 + cropped_images[-1].height//2

combined = Image.new("RGBA", (max_width, total_height), (0, 0, 0, 0))

current_y_center = cropped_images[0].height // 2

for img in cropped_images:
    # paste img centered horizontally
    x = (max_width - img.width) // 2
    y = current_y_center - (img.height // 2)
    combined.paste(img, (x, y), img)
    current_y_center += center_spacing

combined.save("exploded_burger_static.png")
print("Saved exploded_burger_static.png")
