import glob
import re

html_files = glob.glob('*_burger.html')

correct_speech = '''<div id="chef-speech" style="position: absolute; right: -120px; top: -150px; z-index: 4; pointer-events: none; opacity: 0; display: flex; flex-direction: column; align-items: center; gap: 10px;">
    <div style="font-family: 'Bangers', cursive; font-size: 6rem; color: #FFEB3B; line-height: 1; transform: rotate(-10deg); text-shadow: 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 3px 0 #000, 0 -3px 0 #000, 8px 8px 0px #0288D1, 10px 10px 0px #000;">WOW!</div>
    <div style="font-family: 'Bangers', cursive; font-size: 4.5rem; color: #FFFFFF; line-height: 1; transform: rotate(5deg) translateX(40px); text-shadow: 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 3px 0 #000, 0 -3px 0 #000, 6px 6px 0px #000;">YUMMY!</div>
</div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # We will use regex to find everything from <div id="chef-speech" ... to </div></div>
    # But it's safer to find <div id="chef-speech" and replace up to <div class="product-text-col"
    
    # Let's find exactly the corrupted block and replace it
    # We know the corrupted block starts with <div id="chef-speech" and ends right before <div class="product-text-col"
    pattern = r'<div id="chef-speech".*?(?=<div class="product-text-col")'
    replacement = correct_speech + '\n            \n        </div>\n        '
    
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed HTML layouts!")
