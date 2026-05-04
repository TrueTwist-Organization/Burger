import glob
import re

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()

    # Replace chef_2.png with cartoon_monster.png
    html = html.replace('chef_2.png', 'cartoon_monster.png')
    
    with open(file, 'w') as f:
        f.write(html)

print("Monster updated in all files!")
