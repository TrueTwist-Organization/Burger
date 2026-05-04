import re

with open("checkout.html", "r") as f:
    html = f.read()

script_tag = '<script src="checkout.js"></script>'
new_scripts = """    <!-- GSAP for Track Modal Animations -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/MotionPathPlugin.min.js"></script>
    <script>gsap.registerPlugin(MotionPathPlugin);</script>
    <script src="checkout.js"></script>"""

html = html.replace(script_tag, new_scripts)

with open("checkout.html", "w") as f:
    f.write(html)

print("Added GSAP to checkout.html")
