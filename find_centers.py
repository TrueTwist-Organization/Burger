from PIL import Image
import glob

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

for layer in layers:
    img = Image.open(layer).convert("RGBA")
    bbox = img.getbbox() # (left, upper, right, lower)
    if bbox:
        center_y = (bbox[1] + bbox[3]) / 2
        print(f"{layer}: {center_y / img.height * 100:.2f}%")
