import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace exploded_bg_new.png with exploded_bg_latest.png
html = html.replace('url(\'exploded_bg_new.png\')', 'url(\'exploded_bg_latest.png\')')
html = html.replace('url("exploded_bg_new.png")', 'url(\'exploded_bg_latest.png\')')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Set exploded_bg_latest.png as the background of the exploded ingredients section!")
