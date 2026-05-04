import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the inline style from sec-landing that contains the promo_banner.png
pattern = r'<section class="sec-landing" id="home"\s*style="background-image: url\(\'promo_banner\.png\'\);[^"]*">'
replacement = '<section class="sec-landing" id="home">'

html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed the promo banner background from the hero section!")
