import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the replacements
cards = [
    ("classic_cheese_burger.png", "classic_cheese_burger.html"),
    ("spicy_chicken_burger.png", "spicy_chicken_burger.html"),
    ("bbq_bacon_burger.png", "bbq_bacon_burger.html"),
    ("mushroom_swiss_burger.png", "mushroom_swiss_burger.html"),
    ("ultimate_monster_burger.png", "ultimate_monster_burger.html")
]

for img, link in cards:
    old_img_tag = f'<img src="{img}" class="u-burger-img" alt="Burger">'
    new_img_tag = f'<a href="{link}" style="display:block; z-index:10; position:relative;"><img src="{img}" class="u-burger-img" alt="Burger"></a>'
    html = html.replace(old_img_tag, new_img_tag)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added image links to the old tilted cards.")
