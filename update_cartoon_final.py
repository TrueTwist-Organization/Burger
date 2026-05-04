import re

file = 'bbq_bacon_burger.html'
with open(file, 'r') as f:
    html = f.read()

# Replace cartoon_monster with wow_yummy_transparent
html = html.replace('cartoon_monster.png', 'wow_yummy_transparent.png')

# Hide or remove the chef-speech because the image has the text
html = re.sub(r'<div id="chef-speech".*?</div>', '', html)

# We might need to adjust the GSAP animation to remove #chef-speech references
# Find and replace the GSAP lines
old_gsap_speech1 = r"""            // 4\. Chef speaks "Wow yummy"
            \.to\("#chef-speech", \{
                opacity: 1,
                y: -30,
                duration: 0\.5,
                ease: "back\.out\(2\)"
            \}\)"""
new_gsap_speech1 = ""

old_gsap_speech2 = r"""            // 5\. Chef stays for a bit, then leaves
            \.to\(\["#naughty-chef", "#chef-speech"\], \{
                opacity: 0,
                x: 400,
                duration: 1,
                ease: "power2\.in"
            \}, "\+=2"\)"""
new_gsap_speech2 = r"""            // 5. Chef stays for a bit, then leaves
            .to("#naughty-chef", {
                opacity: 0,
                x: 400,
                duration: 1.5,
                ease: "power2.in"
            }, "+=2")"""

html = re.sub(old_gsap_speech1, new_gsap_speech1, html)
html = re.sub(old_gsap_speech2, new_gsap_speech2, html)

# Adjust the cartoon width to be bigger so it fits perfectly
html = html.replace('width: 350px;', 'width: 500px;')
# Adjust the initial x position so it slides in properly
html = html.replace('x: -250,', 'x: -350,')

with open(file, 'w') as f:
    f.write(html)

print("Updated bbq_bacon_burger.html")
