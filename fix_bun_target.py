with open("script.js", "r") as f:
    js = f.read()

# Replace the y: -300 with x: 260, y: 60
js = js.replace('x: 0,\n        y: -300, // Approximate visual center', 'x: 260,\n        y: 60, // Approximate visual center')

with open("script.js", "w") as f:
    f.write(js)
