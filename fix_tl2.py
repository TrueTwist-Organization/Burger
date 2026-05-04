with open('script.js', 'r') as f:
    js = f.read()

# Change top 80% to top 20%
js = js.replace('start: "top 80%", // Start earlier', 'start: "top 20%", // Start much later to avoid early fadeout')

with open('script.js', 'w') as f:
    f.write(js)
