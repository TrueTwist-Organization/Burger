with open("script.js", "r") as f:
    js = f.read()

old_code = "imgWrapper.style.top = percentage + '%';"
new_code = "imgWrapper.style.top = percentage + '%';\n            imgWrapper.style.zIndex = 100 - index; // Ensure top layers are above bottom layers"

js = js.replace(old_code, new_code)

with open("script.js", "w") as f:
    f.write(js)
print("z-index fixed!")
