import glob
import re

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove Step 3 (Chef eats burger)
    pattern3 = r'\s*// 3\. Chef "eats" the burger\s*\.to\("\.main-burger-img", \{.*?\ease: "back\.in\(2\)"\s*\}\)'
    html = re.sub(pattern3, '', html, flags=re.DOTALL)
    
    # Remove Step 6 (Fresh burger drops down)
    pattern6 = r'\s*// 6\. Fresh burger drops down!\s*\.set\("\.main-burger-img", \{.*?\ease: "bounce\.out"\s*\}\);?'
    html = re.sub(pattern6, ';', html, flags=re.DOTALL)

    # In case there's a trailing empty .to or something, let's make sure the semi-colon is correct
    # Actually, replacing the end with a semicolon is safe if it's the end of the chain.
    # The chain currently ends with:
    #             .to(".main-burger-img", {
    #                 y: 0,
    #                 duration: 1.5,
    #                 ease: "bounce.out"
    #             });
    # If we remove step 6, the chain ends at step 5:
    #             // 5. Chef stays for a bit, then leaves
    #             .to(["#naughty-chef", "#chef-speech"], {
    #                 opacity: 0,
    #                 x: 400,
    #                 duration: 1.5,
    #                 ease: "power2.in"
    #             })
    # We need to ensure there is a semicolon at the end of the timeline chain.
    
    # A robust way: find the end of the GSAP chain and ensure it has a semicolon
    # Replace any `})` right before `});` with just `});` or fix the end
    html = re.sub(r'\}\)\s*;\s*\}\);', '});', html)
    html = re.sub(r'\}\)\s*\}\);', '});\n        });', html)

    # Simple fix for the missing semicolon if we just removed step 6:
    html = re.sub(r'ease: "power2\.in"\s*\}\)\s*;', 'ease: "power2.in"\n            });', html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Kept the original burger on screen!")
