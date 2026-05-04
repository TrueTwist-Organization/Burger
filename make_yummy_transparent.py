from PIL import Image

def remove_background(img_path, out_path, bg_color, tolerance=40):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    
    for item in data:
        r, g, b, a = item
        # Calculate color distance
        dist = ((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)**0.5
        if dist < tolerance:
            new_data.append((255, 255, 255, 0)) # fully transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")

remove_background("/Users/jinal/.gemini/antigravity/brain/e43f8f8b-503c-43cf-a12e-89e32f7612ad/yummy_chef_1777633613837.png", "/Users/jinal/Downloads/Food/yummy.png", (255, 152, 0), tolerance=60)
