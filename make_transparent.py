from PIL import Image
import os
import glob

def process(filename):
    if not os.path.exists(filename): return
    img = Image.open(filename).convert("RGBA")
    datas = img.getdata()
    
    new_data = []
    # Identify the background color from the top-left pixel
    bg_color = datas[0]
    
    # We use a color distance tolerance
    tolerance = 30
    
    for item in datas:
        # Distance squared
        dist = (item[0] - bg_color[0])**2 + (item[1] - bg_color[1])**2 + (item[2] - bg_color[2])**2
        if dist < tolerance**2:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(filename, "PNG")
    print(f"Processed {filename}")

for f in glob.glob("*_burger.png"):
    process(f)
