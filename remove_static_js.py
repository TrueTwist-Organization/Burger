import re

with open("script.js", "r") as f:
    js = f.read()

pattern = r'// --- STATIC INGREDIENTS SECTION JS ---.*?// Timeline 2: Ambient background'
js = re.sub(pattern, '// Timeline 2: Ambient background', js, flags=re.DOTALL)

with open("script.js", "w") as f:
    f.write(js)

print("Removed static JS")
