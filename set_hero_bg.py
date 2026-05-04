import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find sec-landing and add the background image style
pattern = r'<section class="sec-landing" id="home".*?>'
# We'll replace any existing style with the new background image style, or append it
def replacer(match):
    tag = match.group(0)
    new_style = "background-image: url('promo_banner.png'); background-size: cover; background-position: center; background-repeat: no-repeat;"
    if 'style="' in tag:
        # replace existing style contents with the new one for simplicity since we know it's just background
        return re.sub(r'style="[^"]*"', f'style="{new_style}"', tag)
    else:
        return tag.replace('id="home"', f'id="home" style="{new_style}"')

html = re.sub(pattern, replacer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Set promo_banner.png as the background of the hero section!")
