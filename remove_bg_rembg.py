# Use a simple flood fill from the top-left corner to remove the background
from PIL import Image

def remove_bg(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    
    # We will just do a simple color replacement for the background
    # The background is mostly orange.
    data = img.getdata()
    new_data = []
    
    # Let's get the color of the top-left pixel
    bg_color = data[0]
    
    for item in data:
        # Calculate distance from bg_color
        dist = abs(item[0] - bg_color[0]) + abs(item[1] - bg_color[1]) + abs(item[2] - bg_color[2])
        if dist < 60: # Threshold
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")

remove_bg("wow_yummy_boy.png", "wow_yummy_transparent.png")
print("Saved wow_yummy_transparent.png")
