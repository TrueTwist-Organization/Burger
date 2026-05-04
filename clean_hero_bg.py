import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Set the background image on sec-landing
pattern_landing = r'<section class="sec-landing" id="home">'
replacement_landing = '<section class="sec-landing" id="home" style="background-image: url(\'promo_banner.png\'); background-size: cover; background-position: center; background-repeat: no-repeat;">'
html = html.replace(pattern_landing, replacement_landing)

# 2. Remove hero-bg-burgers div
pattern_bg_burgers = r'<!-- Side Burgers for Hero Section -->.*?</div>'
html = re.sub(pattern_bg_burgers, '', html, flags=re.DOTALL)

# 3. Remove hero-middle-image
pattern_middle_image = r'<!-- New Middle Hero Image -->.*?<img src="hero_main_boy\.png"[^>]*>'
html = re.sub(pattern_middle_image, '', html, flags=re.DOTALL)

# 4. Remove chef_1.png
pattern_chef = r'<!-- Chef 1 -->.*?<img src="chef_1\.png"[^>]*>'
html = re.sub(pattern_chef, '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated the hero section with the new banner background and removed clashing images!")
