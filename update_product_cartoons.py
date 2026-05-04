import glob
import re

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()

    # Update Chef Image
    old_chef = r'<img src="yummy.png" id="naughty-chef" alt="Chef" style="position: absolute; width: 200px; right: -50px; bottom: 0; z-index: 3; opacity: 0; pointer-events: none;">'
    new_chef = r'<img src="chef_2.png" id="naughty-chef" alt="Chef" style="position: absolute; width: 350px; right: -150px; bottom: -50px; z-index: 3; opacity: 0; pointer-events: none; filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.3));">'
    
    # Update Speech Bubble
    old_speech = r'<div id="chef-speech" style="position: absolute; right: -100px; top: -50px; background: white; padding: 10px 15px; border-radius: 15px; box-shadow: 0 5px 15px rgba\(0,0,0,0.2\); font-weight: bold; color: #D32F2F; opacity: 0; z-index: 4; pointer-events: none;">Oops! I ate it! 😋<br>Making a fresh one...</div>'
    new_speech = r'<div id="chef-speech" style="position: absolute; right: -80px; top: -100px; background: white; padding: 15px 25px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-weight: 900; font-size: 1.8rem; color: #D32F2F; opacity: 0; z-index: 4; pointer-events: none; border: 3px solid #FFC107;">WOW YUMMY!! 😋</div>'

    html = re.sub(old_chef, new_chef, html)
    html = re.sub(old_speech, new_speech, html)

    # Update GSAP Animation
    old_gsap = r"""            // 2\. Naughty chef slides in
            \.to\("#naughty-chef", \{
                opacity: 1,
                x: -120,
                rotation: -10,
                duration: 0\.8,
                ease: "power2\.out"
            \}, "\+=0\.5"\)
            // 3\. Chef "eats" the burger
            \.to\("\.main-burger-img", \{
                scale: 0,
                opacity: 0,
                rotation: 180,
                duration: 0\.5,
                ease: "back\.in\(2\)"
            \}\)
            \.to\("#naughty-chef", \{
                scale: 1\.2,
                duration: 0\.3,
                yoyo: true,
                repeat: 1
            \}\)
            // 4\. Chef speaks
            \.to\("#chef-speech", \{
                opacity: 1,
                y: -20,
                duration: 0\.5,
                ease: "back\.out\(2\)"
            \}\)
            // 5\. Chef runs away after 2 seconds
            \.to\(\["#naughty-chef", "#chef-speech"\], \{
                opacity: 0,
                x: 300,
                duration: 1,
                ease: "power2\.in"
            \}, "\+=2"\)"""

    new_gsap = """            // 2. Naughty chef slides in
            .to("#naughty-chef", {
                opacity: 1,
                x: -250,
                rotation: -5,
                duration: 0.8,
                ease: "power2.out"
            }, "+=0.5")
            // 3. Chef "eats" the burger
            .to(".main-burger-img", {
                scale: 0,
                opacity: 0,
                rotation: 180,
                duration: 0.5,
                ease: "back.in(2)"
            })
            .to("#naughty-chef", {
                scale: 1.1,
                duration: 0.3,
                yoyo: true,
                repeat: 1
            })
            // 4. Chef speaks "Wow yummy"
            .to("#chef-speech", {
                opacity: 1,
                y: -30,
                duration: 0.5,
                ease: "back.out(2)"
            })
            // 5. Chef stays for a bit, then leaves
            .to(["#naughty-chef", "#chef-speech"], {
                opacity: 0,
                x: 400,
                duration: 1,
                ease: "power2.in"
            }, "+=2")"""

    html = re.sub(old_gsap, new_gsap, html)

    with open(file, 'w') as f:
        f.write(html)

print("Product cartoons updated!")
