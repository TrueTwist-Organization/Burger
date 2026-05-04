import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find sec-exploded and replace its style to use exploded_bg_new.png
pattern = r'<section class="sec-exploded" id="ingredients-story" style="[^"]*">'
replacement = '<section class="sec-exploded" id="ingredients-story" style="min-height: 100vh; position: relative; background-image: url(\'exploded_bg_new.png\'); background-size: cover; background-position: center; background-attachment: fixed; background-repeat: no-repeat;">'

html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Set exploded_bg_new.png as the background of the exploded ingredients section!")
