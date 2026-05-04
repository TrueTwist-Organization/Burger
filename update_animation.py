import re

with open('generate_pages.py', 'r') as f:
    code = f.read()

# Replace the image tag in Product Detail
new_img_html = """
        <div style="flex: 1; min-width: 300px; position: relative;" id="burger-img-container">
            <img src="burgers/{title.lower().replace(' ', '_')}.png" alt="{title}" class="main-burger-img" style="width: 100%; max-width: 500px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.1); position: relative; z-index: 2;">
            <img src="yummy.png" id="naughty-chef" alt="Chef" style="position: absolute; width: 200px; right: -50px; bottom: 0; z-index: 3; opacity: 0; pointer-events: none;">
            <div id="chef-speech" style="position: absolute; right: -100px; top: -50px; background: white; padding: 10px 15px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-weight: bold; color: #D32F2F; opacity: 0; z-index: 4; pointer-events: none;">Oops! I ate it! 😋<br>Making a fresh one...</div>
        </div>
"""

code = re.sub(
    r'<div style="flex: 1; min-width: 300px;">\s*<img src="burgers/\{title\.lower\(\)\.replace\(\' \', \'_\'\)\}\.png" alt="\{title\}" style="width: 100%; max-width: 500px; border-radius: 20px; box-shadow: 0 20px 50px rgba\(0,0,0,0\.1\);">\s*</div>',
    new_img_html.strip(),
    code
)

# Add GSAP script at the end
script_html = """
    <script src="cart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof gsap === 'undefined') return;
            const tl = gsap.timeline();
            
            // 1. Burger bounces in from top-left
            tl.from(".main-burger-img", {
                x: -800,
                y: -400,
                rotation: -360,
                duration: 2,
                ease: "bounce.out"
            })
            // 2. Naughty chef slides in
            .to("#naughty-chef", {
                opacity: 1,
                x: -120,
                rotation: -10,
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
                scale: 1.2,
                duration: 0.3,
                yoyo: true,
                repeat: 1
            })
            // 4. Chef speaks
            .to("#chef-speech", {
                opacity: 1,
                y: -20,
                duration: 0.5,
                ease: "back.out(2)"
            })
            // 5. Chef runs away after 2 seconds
            .to(["#naughty-chef", "#chef-speech"], {
                opacity: 0,
                x: 300,
                duration: 1,
                ease: "power2.in"
            }, "+=2")
            // 6. Fresh burger drops down!
            .set(".main-burger-img", {
                scale: 1,
                opacity: 1,
                y: -800,
                rotation: 0
            })
            .to(".main-burger-img", {
                y: 0,
                duration: 1.5,
                ease: "bounce.out"
            });
        });
    </script>
</body>
"""

code = code.replace('    <script src="cart.js"></script>\n</body>', script_html)

with open('generate_pages.py', 'w') as f:
    f.write(code)
print("Updated generate_pages.py with hilarious animation!")
