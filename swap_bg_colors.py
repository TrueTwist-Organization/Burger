import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace linear-gradient with #FFF5E4 for .sec-landing
css = css.replace(
    'background: linear-gradient(135deg, #FFF9F2 0%, #FFF3E0 100%);',
    'background: #FFF5E4;'
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace background color for sec-exploded
pattern = r'<section class="sec-exploded" id="ingredients-story" style="min-height: 100vh; position: relative; background[^>]*>'
replacement = '<section class="sec-exploded" id="ingredients-story" style="min-height: 100vh; position: relative; background: linear-gradient(135deg, #FFF9F2 0%, #FFF3E0 100%);">'
html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Swapped the backgrounds of the hero section and the exploded ingredients section!")
