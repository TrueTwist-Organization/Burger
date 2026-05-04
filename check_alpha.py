from PIL import Image

img = Image.open('hero_main_boy.png')
img = img.convert('RGBA')

w, h = img.size
corners = [
    img.getpixel((0, 0)),
    img.getpixel((w-1, 0)),
    img.getpixel((0, h-1)),
    img.getpixel((w-1, h-1))
]

print("Corners RGBA:", corners)
