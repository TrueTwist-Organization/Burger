import re

with open('mushroom_swiss_burger.html', 'r', encoding='utf-8') as f:
    html = f.read()

exploded_html = """
            <div id="ms-exploded-container" style="position: relative; width: 100%; max-width: 500px; height: 600px; margin: 0 auto;">
                <div class="ms-layer" id="ms-l1" style="position: absolute; top: 0; left: 0; width: 100%; z-index: 5;"><img src="ms_layer1_topbun.png" style="width:100%; drop-shadow(0 10px 10px rgba(0,0,0,0.3))"></div>
                <div class="ms-label" id="ms-label1" style="position: absolute; top: 10%; right: -20%; opacity: 0; font-family: 'Bangers'; font-size: 1.5rem; color: #FF5722; white-space: nowrap;">Top Bun 👈</div>

                <div class="ms-layer" id="ms-l2" style="position: absolute; top: 0; left: 0; width: 100%; z-index: 4;"><img src="ms_layer2_mushrooms.png" style="width:100%; drop-shadow(0 10px 10px rgba(0,0,0,0.3))"></div>
                <div class="ms-label" id="ms-label2" style="position: absolute; top: 30%; right: -25%; opacity: 0; font-family: 'Bangers'; font-size: 1.5rem; color: #FF5722; white-space: nowrap;">Sautéed Mushrooms 👈</div>

                <div class="ms-layer" id="ms-l3" style="position: absolute; top: 0; left: 0; width: 100%; z-index: 3;"><img src="ms_layer3_cheese.png" style="width:100%; drop-shadow(0 10px 10px rgba(0,0,0,0.3))"></div>
                <div class="ms-label" id="ms-label3" style="position: absolute; top: 50%; right: -25%; opacity: 0; font-family: 'Bangers'; font-size: 1.5rem; color: #FF5722; white-space: nowrap;">Melted Swiss Cheese 👈</div>

                <div class="ms-layer" id="ms-l4" style="position: absolute; top: 0; left: 0; width: 100%; z-index: 2;"><img src="ms_layer4_patty.png" style="width:100%; drop-shadow(0 10px 10px rgba(0,0,0,0.3))"></div>
                <div class="ms-label" id="ms-label4" style="position: absolute; top: 70%; right: -20%; opacity: 0; font-family: 'Bangers'; font-size: 1.5rem; color: #FF5722; white-space: nowrap;">Beef Patty 👈</div>

                <div class="ms-layer" id="ms-l5" style="position: absolute; top: 0; left: 0; width: 100%; z-index: 1;"><img src="ms_layer5_bottombun.png" style="width:100%; drop-shadow(0 10px 10px rgba(0,0,0,0.3))"></div>
                <div class="ms-label" id="ms-label5" style="position: absolute; top: 90%; right: -20%; opacity: 0; font-family: 'Bangers'; font-size: 1.5rem; color: #FF5722; white-space: nowrap;">Bottom Bun 👈</div>
            </div>
"""

# Replace the original flat image with the exploded container
pattern = r'<img src="mushroom_swiss_burger\.png".*?z-index: 2;">'
html = re.sub(pattern, exploded_html, html, flags=re.DOTALL)

# Add GSAP scripts to the head if not present
if "gsap" not in html:
    gsap_scripts = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
"""
    html = html.replace('</head>', gsap_scripts + '</head>')

# Add the GSAP animation script at the end of the body
animation_script = """
    <script>
        // Automatic explosion animation on load
        window.addEventListener("load", () => {
            const tl = gsap.timeline({delay: 0.5});
            
            // Initial assembled state is Y=0 for all.
            // Explode by modifying Y
            tl.to("#ms-l1", {y: -80, duration: 1}, 0)
              .to("#ms-label1", {opacity: 1, x: -20, duration: 1}, 0)
              
              .to("#ms-l2", {y: -40, duration: 1}, 0.2)
              .to("#ms-label2", {opacity: 1, x: -20, duration: 1}, 0.2)
              
              .to("#ms-l3", {y: 0, duration: 1}, 0.4)
              .to("#ms-label3", {opacity: 1, x: -20, duration: 1}, 0.4)
              
              .to("#ms-l4", {y: 40, duration: 1}, 0.6)
              .to("#ms-label4", {opacity: 1, x: -20, duration: 1}, 0.6)
              
              .to("#ms-l5", {y: 80, duration: 1}, 0.8)
              .to("#ms-label5", {opacity: 1, x: -20, duration: 1}, 0.8);
        });
    </script>
</body>
"""

html = html.replace('</body>', animation_script)

with open('mushroom_swiss_burger.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added mushroom swiss exploded animation!")
