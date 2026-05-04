from PIL import Image

def process(filename):
    try:
        img = Image.open(filename).convert("RGBA")
        width, height = img.size
        
        # We will flood fill from (0,0)
        target_color = img.getpixel((0,0))
        
        # Simple BFS for flood fill with tolerance
        tolerance = 50
        
        def color_diff(c1, c2):
            return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]) + abs(c1[2]-c2[2])
            
        visited = set()
        queue = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1)]
        
        pixels = img.load()
        
        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if color_diff(pixels[x,y], target_color) < tolerance:
                pixels[x, y] = (255, 255, 255, 0)
                
                if x > 0: queue.append((x-1, y))
                if x < width - 1: queue.append((x+1, y))
                if y > 0: queue.append((x, y-1))
                if y < height - 1: queue.append((x, y+1))
                
        img.save(filename)
        print(f"Successfully processed {filename}")
    except Exception as e:
        print(f"Error on {filename}: {e}")

process("classic_cheese_burger.png")
process("grilled_chicken_burger.png")
process("spicy_chicken_burger.png")
process("bbq_bacon_burger.png")
process("veggie_burger.png")
process("mushroom_swiss_burger.png")
process("double_beef_burger.png")
