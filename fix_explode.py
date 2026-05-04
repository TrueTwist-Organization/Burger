import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Insert attractive-text into burger-container
old_layer1 = '<img src="layer1_topbun.png" class="burger-layer" id="layer-1" alt="Top Bun" style="z-index: 8;">\n    </div>'
new_layer1 = """<img src="layer1_topbun.png" class="burger-layer" id="layer-1" alt="Top Bun" style="z-index: 8;">
        
        <div class="attractive-text" id="attractive-text" style="position: absolute; left: 65%; top: 50%; transform: translateY(-50%); width: 400px; color: white; opacity: 0;">
            <h2 style="font-family: 'Bebas Neue', sans-serif; font-size: 5rem; margin-bottom: 20px; line-height: 0.9; letter-spacing: 2px;">THE PERFECT<br><span style="color: #FFD54F;">BUILD</span></h2>
            <p style="font-size: 1.2rem; line-height: 1.6; font-weight: 300;">Every layer is crafted with precision. From our freshly baked artisanal buns to the crispest greens and juiciest flame-grilled patty, experience perfection in every single bite.</p>
        </div>
    </div>"""
if 'attractive-text' not in html:
    html = html.replace(old_layer1, new_layer1)

# 2. Insert sec-exploded after sec-landing
old_landing = r"""        <img src="chef_1.png" class="chef-img chef-1" alt="Cartoon Chef Thumbs Up">
    </section>"""
new_landing = """        <img src="chef_1.png" class="chef-img chef-1" alt="Cartoon Chef Thumbs Up">
    </section>

    <!-- Section 2: Exploded Ingredients -->
    <section class="sec-exploded" style="min-height: 100vh; display: flex; align-items: center; position: relative;">
    </section>"""
if 'sec-exploded' not in html:
    html = html.replace(old_landing, new_landing)

with open("index.html", "w") as f:
    f.write(html)

print("index.html fixed!")
