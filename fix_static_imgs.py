with open("script.js", "r") as f:
    js = f.read()

# Replace static_layer*.png with layer*.png
for i in range(1, 9):
    old_img = f'static_layer{i}_'
    new_img = f'layer{i}_'
    js = js.replace(old_img, new_img)

with open("script.js", "w") as f:
    f.write(js)
    
print("Updated script.js to use full size layer images.")
