import os
import glob
import re

html_files = glob.glob('*_burger.html')

new_speech_container = '''<div id="chef-speech" style="position: absolute; right: -150px; top: -200px; z-index: 4; pointer-events: none; opacity: 0; width: 300px; height: 300px;">
    <img src="wow_bubble.png" style="width: 250px; position: absolute; right: 10px; top: 0px; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.3)); transform: rotate(-5deg);">
    <img src="yummy_bubble.png" style="width: 220px; position: absolute; right: -20px; top: 160px; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.3)); transform: rotate(5deg);">
</div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace the existing #chef-speech
    pattern = r'<div id="chef-speech"[^>]*>.*?</div>'
    new_html = re.sub(pattern, new_speech_container, html, flags=re.DOTALL)
    
    if html != new_html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Updated speech bubble to use image bubbles!")
