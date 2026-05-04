import glob
import re

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We want to change the style of #chef-speech
    old_style = 'style="position: absolute; right: -120px; top: -150px; z-index: 4; pointer-events: none; opacity: 0; display: flex; flex-direction: column; align-items: center; gap: 10px;"'
    new_style = 'style="position: absolute; right: -40px; top: -20px; z-index: 4; pointer-events: none; opacity: 0; display: flex; flex-direction: column; align-items: center; gap: 10px;"'
    
    html = html.replace(old_style, new_style)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Moved WOW YUMMY text closer to the image!")
