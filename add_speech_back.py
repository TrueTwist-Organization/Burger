import os
import re
import glob

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()
        
    # Check if #chef-speech already exists
    if 'id="chef-speech"' not in html:
        # Insert speech bubble right after naughty-chef
        chef_tag = r'<img src="[^"]*" id="naughty-chef".*?>'
        new_speech = r'\g<0>\n            <div id="chef-speech" style="position: absolute; right: -80px; top: -100px; background: white; padding: 15px 25px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-weight: 900; font-size: 1.8rem; color: #D32F2F; opacity: 0; z-index: 4; pointer-events: none; border: 3px solid #FFC107;">WOW YUMMY!! 😋</div>'
        html = re.sub(chef_tag, new_speech, html, count=1)
        
    # Check if GSAP animation has the speech bubble logic
    # Find:
    #             // 5. Chef stays for a bit, then leaves
    #             .to("#naughty-chef", {
    # Replace with logic that animates speech bubble first
    
    old_leave = r'            // 5\. Chef stays for a bit, then leaves\n            \.to\("#naughty-chef", \{'
    new_leave = r'''            // 4. Chef speaks "Wow yummy"
            .to("#chef-speech", {
                opacity: 1,
                y: -20,
                duration: 0.4,
                ease: "back.out(2)"
            })
            // 5. Chef stays for a bit, then leaves
            .to(["#naughty-chef", "#chef-speech"], {'''
            
    if 'Chef speaks "Wow yummy"' not in html:
        html = re.sub(old_leave, new_leave, html)
        
    with open(file, 'w') as f:
        f.write(html)
        
print("Added WOW YUMMY speech bubble to all product pages!")
