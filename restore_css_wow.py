import os
import glob
import re

html_files = glob.glob('*_burger.html')

new_speech_container = '''<div id="chef-speech" style="position: absolute; right: -120px; top: -150px; z-index: 4; pointer-events: none; opacity: 0; display: flex; flex-direction: column; align-items: center; gap: 10px;">
    <div style="font-family: 'Bangers', cursive; font-size: 6rem; color: #FFEB3B; line-height: 1; transform: rotate(-10deg); text-shadow: 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 3px 0 #000, 0 -3px 0 #000, 8px 8px 0px #0288D1, 10px 10px 0px #000;">WOW!</div>
    <div style="font-family: 'Bangers', cursive; font-size: 4.5rem; color: #FFFFFF; line-height: 1; transform: rotate(5deg) translateX(40px); text-shadow: 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 3px 0 #000, 0 -3px 0 #000, 6px 6px 0px #000;">YUMMY!</div>
</div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # The current HTML has <div id="chef-speech" ...> <img src="wow_bubble.png"...> ... </div>
    pattern = r'<div id="chef-speech"[^>]*>.*?</div>'
    new_html = re.sub(pattern, new_speech_container, html, flags=re.DOTALL)
    
    if html != new_html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Updated HTML files to clean CSS WOW/YUMMY.")
