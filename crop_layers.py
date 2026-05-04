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

for i, layer in enumerate(layers):
    img = Image.open(layer).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        cropped.save(f"cropped_layer{i+1}.png")
        print(f"Saved cropped_layer{i+1}.png")
