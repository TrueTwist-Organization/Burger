import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove new_cartoon.css link
html = html.replace('    <link rel="stylesheet" href="new_cartoon.css">\n', '')

# Remove new_cartoon.js script
html = html.replace('    <script src="new_cartoon.js"></script>\n', '')

# Remove the NC modal HTML block
if '<!-- NEW CARTOON MODAL -->' in html:
    html = re.sub(r'\s*<!-- NEW CARTOON MODAL -->.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
