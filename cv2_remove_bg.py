import cv2
import numpy as np
import glob

def remove_background(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        return
    
    if img.shape[2] == 4:
        bgr = img[:, :, :3].copy()
        alpha = img[:, :, 3].copy()
    else:
        bgr = img.copy()
        alpha = np.ones(bgr.shape[:2], dtype=np.uint8) * 255
    
    h, w = bgr.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    
    # Floodfill from corners
    corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
    # Use a relatively generous tolerance for off-white backgrounds
    # Assuming the corners are part of the background
    for pt in corners:
        # Check if the pixel is bright enough to be considered background
        # If it's already dark, it might be the burger itself, so don't floodfill!
        px = bgr[pt[1], pt[0]]
        if px[0] > 200 and px[1] > 200 and px[2] > 200:
            cv2.floodFill(bgr, mask, pt, (0, 255, 0), (30, 30, 30), (30, 30, 30), cv2.FLOODFILL_FIXED_RANGE)
    
    # The mask has 1 where filled
    filled_mask = mask[1:-1, 1:-1]
    
    # Foreground mask
    fg_mask = (1 - filled_mask).astype(np.float32) * 255
    
    # Smooth edges
    soft_mask = cv2.GaussianBlur(fg_mask, (5, 5), 0)
    
    # Multiply existing alpha by our new mask
    final_alpha = (alpha.astype(np.float32) * (soft_mask / 255.0)).astype(np.uint8)
    
    orig = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if orig.shape[2] == 3:
        orig = cv2.cvtColor(orig, cv2.COLOR_BGR2BGRA)
        
    orig[:, :, 3] = final_alpha
    cv2.imwrite(image_path, orig)
    print(f"Removed background for {image_path}")

for f in glob.glob('*_burger.png'):
    remove_background(f)
