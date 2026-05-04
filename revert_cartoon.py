import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove cartoon.css link
content = content.replace('<link rel="stylesheet" href="story.css">\n    <link rel="stylesheet" href="cartoon.css">', '<link rel="stylesheet" href="story.css">')
content = content.replace('    <link rel="stylesheet" href="cartoon.css">\n', '')

# Remove cartoon.js script
content = content.replace('<script src="story.js"></script>\n    <script src="cartoon.js"></script>', '<script src="story.js"></script>')
content = content.replace('    <script src="cartoon.js"></script>\n', '')

# Revert Spicy Chicken Burger links
content = re.sub(r'<a href="#" onclick="openCartoonModal\(\'Spicy Chicken Burger\', \'240\'\); return false;" style="display:block; z-index:10; position:relative;">', r'<a href="spicy_chicken_burger.html" style="display:block; z-index:10; position:relative;">', content)
content = re.sub(r'<a href="#" onclick="openCartoonModal\(\'Spicy Chicken Burger\', \'240\'\); return false;" class="u-card-title">Spicy Chicken Burger</a>', r'<a href="spicy_chicken_burger.html" class="u-card-title">Spicy Chicken Burger</a>', content)

# Revert Mushroom Swiss Burger links
content = re.sub(r'<a href="#" onclick="openCartoonModal\(\'Mushroom Swiss Burger\', \'280\'\); return false;" style="display:block; z-index:10; position:relative;">', r'<a href="mushroom_swiss_burger.html" style="display:block; z-index:10; position:relative;">', content)
content = re.sub(r'<a href="#" onclick="openCartoonModal\(\'Mushroom Swiss Burger\', \'280\'\); return false;" class="u-card-title">Mushroom Swiss Burger</a>', r'<a href="mushroom_swiss_burger.html" class="u-card-title">Mushroom Swiss Burger</a>', content)

# Revert Classic Cheese Burger link
content = re.sub(r'<a href="#" onclick="openCartoonModal\(\'Classic Cheese Burger\', \'200\'\); return false;" style="display:block; z-index:10; position:relative;"><img src="burger.png" class="u-burger-img" alt="Burger"></a>', r'<img src="burger.png" class="u-burger-img" alt="Burger">', content)

# Remove the cartoon modal HTML
cartoon_modal_start = '<!-- Full Screen Cartoon Animation Modal -->'
cartoon_modal_end = '    </div>\n</body>'

if cartoon_modal_start in content:
    content = re.sub(r'<!-- Full Screen Cartoon Animation Modal -->.*?</div>\n</body>', '</body>', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
print("Reverted index.html successfully.")
