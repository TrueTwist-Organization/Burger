import re

with open("index.html", "r") as f:
    html = f.read()

# Remove the static ingredients section
pattern = r'<!-- STATIC INGREDIENTS SECTION \(RESPONSIVE\) -->.*?<!-- Section 3: Menu -->'
html = re.sub(pattern, '<!-- Section 3: Menu -->', html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(html)

print("Removed static ingredients section from index.html")
