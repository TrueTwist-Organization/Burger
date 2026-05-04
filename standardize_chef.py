import glob
import re

html_files = glob.glob('*_burger.html')

standard_chef = '<img src="avocado_chef_transparent.png" id="naughty-chef" alt="Chef" style="position: absolute; width: 500px; right: -150px; bottom: -50px; z-index: 3; opacity: 0; pointer-events: none; filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.3));">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Use regex to find any img tag with id="naughty-chef" and replace it
    pattern = r'<img src="[^"]*" id="naughty-chef"[^>]*>'
    html = re.sub(pattern, standard_chef, html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Standardized the chef image on all pages!")
