with open('script.js', 'r') as f:
    js = f.read()

# Add gsap.set for #burger-container
old_setup = """if(l1) {
    gsap.set([l1, l2, l3, l4, l5, l6, l7, l8], { opacity: 1 });"""
new_setup = """if(l1) {
    gsap.set("#burger-container", { xPercent: -50 });
    gsap.set([l1, l2, l3, l4, l5, l6, l7, l8], { opacity: 1 });"""

js = js.replace(old_setup, new_setup)

with open('script.js', 'w') as f:
    f.write(js)
print("Added xPercent: -50 to script.js")
