from PIL import Image
import glob

files = glob.glob('*_burger.png')
for f in files:
    try:
        img = Image.open(f).convert('RGBA')
        data = img.getdata()
        
        new_data = []
        for item in data:
            # If the pixel is very light (almost white), make it pure white so multiply blend works perfectly
            if item[0] > 235 and item[1] > 235 and item[2] > 235:
                # Force it to pure white
                new_data.append((255, 255, 255, 255))
            else:
                new_data.append(item)
                
        img.putdata(new_data)
        img.save(f, "PNG")
        print(f"Cleaned {f}")
    except Exception as e:
        print(f"Failed to clean {f}: {e}")
