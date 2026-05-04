import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Fix the footer link (About Us)
    html = html.replace('href="index.html#about" style="color: #bbb; text-decoration: none; margin: 0 10px;">About Us</a>', 'href="index.html#story" style="color: #bbb; text-decoration: none; margin: 0 10px;">About Us</a>')
    
    # Fix the header nav links (About)
    html = html.replace('href="index.html#about" class="nav-link">About</a>', 'href="index.html#story" class="nav-link">About</a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed About links to point to #story!")
