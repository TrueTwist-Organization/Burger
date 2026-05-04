import re

with open("script.js", "r") as f:
    js = f.read()

# Remove the animateTopBunEntrance function and its call
pattern = r'function animateTopBunEntrance\(\) \{.*?\n\}\n\nanimateTopBunEntrance\(\);\n\n'
js = re.sub(pattern, '', js, flags=re.DOTALL)

with open("script.js", "w") as f:
    f.write(js)

print("Reverted bun animation")
