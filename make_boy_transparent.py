from PIL import Image
import os

img_path = '/Users/jinal/.gemini/antigravity/brain/4b18eaf6-047e-482a-85e5-762338da25ce/wow_yummy_boy_1777724495844.png'
img = Image.open(img_path).convert("RGBA")
data = img.getdata()

new_data = []
for item in data:
    # Remove the orange background. The orange is roughly R>200, G>100, B<100 
    # Actually it's safer to just keep the image as is and let the user enjoy the comic panel look!
    new_data.append(item)

img.putdata(new_data)
img.save("wow_yummy_boy.png", "PNG")
print("Saved wow_yummy_boy.png")
