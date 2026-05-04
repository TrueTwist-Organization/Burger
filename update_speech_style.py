import os
import glob

html_files = glob.glob('*_burger.html')

old_speech_prefix = '<div id="chef-speech" style="position: absolute; right: -80px; top: -100px; background: white; padding: 15px 25px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-weight: 900; font-size: 1.8rem; color: #D32F2F; opacity: 0; z-index: 4; pointer-events: none; border: 3px solid #FFC107;">WOW YUMMY!! 😋</div>'

new_speech = '<div id="chef-speech" style="position: absolute; right: -100px; top: -120px; font-family: \'Bangers\', cursive; font-size: 4.5rem; color: #FFEB3B; text-shadow: 3px 3px 0 #000, -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000, 6px 6px 0px #D32F2F; transform: rotate(-10deg); opacity: 0; z-index: 4; pointer-events: none; line-height: 1;">WOW<br>YUMMY!!</div>'

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()
        
    if old_speech_prefix in html:
        html = html.replace(old_speech_prefix, new_speech)
        with open(file, 'w') as f:
            f.write(html)
            
print("Updated speech bubble to comic cartoon style!")
