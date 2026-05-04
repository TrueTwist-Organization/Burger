with open('script.js', 'r') as f:
    js = f.read()

old_setup = """gsap.set([l1, l2, l3, l4, l5, l6, l7, l8], { opacity: 1 });"""
new_setup = """if(l1) {
    gsap.set([l1, l2, l3, l4, l5, l6, l7, l8], { opacity: 1 });"""

old_end = """   .to(l8, { ...assembledState.l8, duration: 1 }, "<");"""
new_end = """   .to(l8, { ...assembledState.l8, duration: 1 }, "<");
} // End if(l1)"""

js = js.replace(old_setup, new_setup)
js = js.replace(old_end, new_end)

with open('script.js', 'w') as f:
    f.write(js)
print("Added null check in script.js")
