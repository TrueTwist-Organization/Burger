import re

# Fix index.html id
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('id="universe-menu"', 'id="menu"')
with open('index.html', 'w') as f:
    f.write(html)

# Fix universe.js
with open('universe.js', 'r') as f:
    ujs = f.read()

ujs = ujs.replace("getElementById('universe-menu')", "getElementById('menu')")
with open('universe.js', 'w') as f:
    f.write(ujs)

# Fix script.js
with open('script.js', 'r') as f:
    sjs = f.read()

sjs = sjs.replace('trigger: ".sec-menu",', 'trigger: ".sec-menu-universe",')
with open('script.js', 'w') as f:
    f.write(sjs)

print("Navbar issues fixed.")
