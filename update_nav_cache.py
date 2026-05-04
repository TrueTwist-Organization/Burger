import glob
import re

# 1. Update CSS to 1024px
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The block we appended:
# /* MOBILE NAVBAR TOGGLE */
# @media (max-width: 768px) {
css = css.replace('/* MOBILE NAVBAR TOGGLE */\n@media (max-width: 768px)', '/* MOBILE NAVBAR TOGGLE */\n@media (max-width: 1024px)')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update cache buster in all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Force cache reload by changing style.css to style.css?v=3 or similar
    html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=' + str(hash("new_nav") % 10000) + '"', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated breakpoint to 1024px and forced CSS cache refresh!")
