import re

with open('mushroom_swiss_burger.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the exploded container
pattern_exploded = r'<div id="ms-exploded-container".*?</div>\s*</div>\s*</div>' # wait, the regex needs to be precise.
# Let's just use string replace for the huge div block. We can find it using regex.
html = re.sub(r'<div id="ms-exploded-container".*?Bottom Bun 👈</div>\s*</div>', 
              '<img src="mushroom_swiss_burger.png" alt="MUSHROOM SWISS BURGER" class="main-burger-img"\n                style="width: 100%; max-width: 500px; filter: drop-shadow(0px 20px 30px rgba(0,0,0,0.3)); mix-blend-mode: multiply; position: relative; z-index: 2;">', 
              html, flags=re.DOTALL)

# Remove GSAP script at the end
html = re.sub(r'<script>\s*// Automatic explosion animation on load.*?</script>', '', html, flags=re.DOTALL)

# Optionally remove the gsap head imports if it breaks anything, but it's fine to leave them or remove them.
html = re.sub(r'<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\s*<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>', '', html, flags=re.DOTALL)

with open('mushroom_swiss_burger.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Reverted Mushroom Swiss HTML.")
