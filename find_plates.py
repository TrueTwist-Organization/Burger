from PIL import Image
import glob

files = glob.glob('*_burger.png')
for f in files:
    try:
        img = Image.open(f).convert('RGB')
        w, h = img.size
        # Check a pixel near the bottom center (e.g. at x=w/2, y=h-50)
        pixel = img.getpixel((w//2, h - 50))
        
        # If it's dark (R<100, G<100, B<100), it's likely a plate
        if pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
            print(f"Possible plate found in: {f} - Pixel color: {pixel}")
    except Exception as e:
        pass
