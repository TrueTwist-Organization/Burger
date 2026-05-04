from PIL import Image
import os

img_path = '/Users/jinal/.gemini/antigravity/brain/4b18eaf6-047e-482a-85e5-762338da25ce/long_tongue_cartoon_1777724096810.png'
img = Image.open(img_path).convert("RGBA")
data = img.getdata()

new_data = []
for item in data:
    # change all white (also shades of whites)
    # to transparent
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save("cartoon_monster.png", "PNG")
print("Saved cartoon_monster.png")
