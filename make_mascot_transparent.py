from PIL import Image
from collections import deque

def process(filename, out_filename):
    try:
        img = Image.open(filename).convert("RGBA")
        width, height = img.size
        
        target_color = img.getpixel((0,0))
        tolerance = 50
        
        def color_diff(c1, c2):
            return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]) + abs(c1[2]-c2[2])
            
        visited = set()
        queue = deque([(0,0), (width-1, 0), (0, height-1), (width-1, height-1)])
        
        pixels = img.load()
        
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if color_diff(pixels[x,y], target_color) < tolerance:
                pixels[x, y] = (255, 255, 255, 0)
                
                if x > 0: queue.append((x-1, y))
                if x < width - 1: queue.append((x+1, y))
                if y > 0: queue.append((x, y-1))
                if y < height - 1: queue.append((x, y+1))
                
        img.save(out_filename)
        print(f"Successfully processed {out_filename}")
    except Exception as e:
        print(f"Error on {filename}: {e}")

process("/Users/jinal/.gemini/antigravity/brain/4b18eaf6-047e-482a-85e5-762338da25ce/new_yummy_mascot_1777696665058.png", "yummy.png")
