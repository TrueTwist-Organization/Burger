from PIL import Image, ImageDraw, ImageFilter

for filename in ['truffle_mayo_burger.png', 'hawaiian_pineapple_burger.png']:
    try:
        img = Image.open(filename).convert('RGBA')
        w, h = img.size

        mask = Image.new('L', (w, h), 255)
        draw = ImageDraw.Draw(mask)

        plate_y = int(h * 0.8)
        draw.rectangle([0, plate_y, w, h], fill=0)

        bun_width = int(w * 0.7)
        bun_x = (w - bun_width) // 2
        bun_y_top = plate_y - 100
        bun_y_bottom = plate_y + 40

        draw.ellipse([bun_x, bun_y_top, bun_x + bun_width, bun_y_bottom], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(10))

        data = img.getdata()
        mask_data = mask.getdata()

        new_data = []
        for i, item in enumerate(data):
            m = mask_data[i]
            if m < 255:
                ratio = m / 255.0
                r = int(item[0] * ratio + 255 * (1 - ratio))
                g = int(item[1] * ratio + 255 * (1 - ratio))
                b = int(item[2] * ratio + 255 * (1 - ratio))
                new_data.append((r, g, b, 255))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(filename)
        print(f"Plate removed from {filename} with soft edge!")
    except Exception as e:
        print(f"Failed on {filename}: {e}")
