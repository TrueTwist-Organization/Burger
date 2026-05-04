from PIL import Image

img_path = '/Users/jinal/Downloads/Food/mushroom_swiss_burger.png'
try:
    original_img = Image.open(img_path).convert("RGBA")
    width, height = original_img.size

    # Mushroom Swiss typically has 5 or 6 main visual layers
    # Slicing roughly based on typical proportions
    slices = [
        ("ms_layer1_topbun.png", 0, int(height * 0.30)),
        ("ms_layer2_mushrooms.png", int(height * 0.30), int(height * 0.45)),
        ("ms_layer3_cheese.png", int(height * 0.45), int(height * 0.60)),
        ("ms_layer4_patty.png", int(height * 0.60), int(height * 0.75)),
        ("ms_layer5_bottombun.png", int(height * 0.75), height)
    ]

    for name, top, bottom in slices:
        layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        slice_img = original_img.crop((0, top, width, bottom))
        layer.paste(slice_img, (0, top))
        layer.save('/Users/jinal/Downloads/Food/' + name)

    print("Successfully sliced the Mushroom Swiss Burger into 5 layers!")
except Exception as e:
    print(f"Error slicing: {e}")
