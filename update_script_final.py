import re

with open("script.js", "r") as f:
    content = f.read()

# Replace the GSAP setup for labels with the attractive text setup
content = re.sub(
    r'// Ensure labels start hidden and perfectly offset vertically to match the assembled burger\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\ngsap\.set\("#label-l8", { opacity: 0, x: 30, y: -252 }\);',
    '// Setup attractive text\ngsap.set("#attractive-text", { opacity: 0, x: 50 });',
    content,
    flags=re.DOTALL
)

# Replace the tl_explode step 1
step1_old = """// Step 1: Sequentially explode each layer AND reveal its text at the same time
tl_explode.to(l1, { ...explodedState.l1, duration: 1 }, 0)
          .to("#label-l1", { opacity: 1, x: 0, y: 0, duration: 1 }, 0)
          
          .to(l2, { ...explodedState.l2, duration: 1 }, 1)
          .to("#label-l2", { opacity: 1, x: 0, y: 0, duration: 1 }, 1)
          
          .to(l3, { ...explodedState.l3, duration: 1 }, 2)
          .to("#label-l3", { opacity: 1, x: 0, y: 0, duration: 1 }, 2)
          
          .to(l4, { ...explodedState.l4, duration: 1 }, 3)
          .to("#label-l4", { opacity: 1, x: 0, y: 0, duration: 1 }, 3)
          
          .to(l5, { ...explodedState.l5, duration: 1 }, 4)
          .to("#label-l5", { opacity: 1, x: 0, y: 0, duration: 1 }, 4)
          
          .to(l6, { ...explodedState.l6, duration: 1 }, 5)
          .to("#label-l6", { opacity: 1, x: 0, y: 0, duration: 1 }, 5)
          
          .to(l7, { ...explodedState.l7, duration: 1 }, 6)
          .to("#label-l7", { opacity: 1, x: 0, y: 0, duration: 1 }, 6)
          
          .to(l8, { ...explodedState.l8, duration: 1 }, 7)
          .to("#label-l8", { opacity: 1, x: 0, y: 0, duration: 1 }, 7);"""

step1_new = """// Step 1: Sequentially explode each layer
tl_explode.to(l1, { ...explodedState.l1, duration: 1 }, 0)
          .to(l2, { ...explodedState.l2, duration: 1 }, 1)
          .to(l3, { ...explodedState.l3, duration: 1 }, 2)
          .to(l4, { ...explodedState.l4, duration: 1 }, 3)
          .to(l5, { ...explodedState.l5, duration: 1 }, 4)
          .to(l6, { ...explodedState.l6, duration: 1 }, 5)
          .to(l7, { ...explodedState.l7, duration: 1 }, 6)
          .to(l8, { ...explodedState.l8, duration: 1 }, 7);

// Reveal attractive text while exploding
tl_explode.to("#attractive-text", { opacity: 1, x: 0, duration: 4 }, 2);"""

content = content.replace(step1_old, step1_new)

# Replace Step 3
step3_old = """// Step 3: Reassemble and drop down
tl_explode.to(labels, { opacity: 0, x: 30, duration: 0.5 })
   .to("#burger-container", { bottom: initialBottom, yPercent: 0, duration: 1 }, "<")
   .to(l1, { ...assembledState.l1, duration: 1 }, "<")
   .to(l2, { ...assembledState.l2, duration: 1 }, "<")
   .to(l3, { ...assembledState.l3, duration: 1 }, "<")
   .to(l4, { ...assembledState.l4, duration: 1 }, "<")
   .to(l5, { ...assembledState.l5, duration: 1 }, "<")
   .to(l6, { ...assembledState.l6, duration: 1 }, "<")
   .to(l7, { ...assembledState.l7, duration: 1 }, "<")
   .to(l8, { ...assembledState.l8, duration: 1 }, "<");"""

step3_new = """// Step 3: Reassemble RIGHT THERE
tl_explode.to("#attractive-text", { opacity: 0, x: 30, duration: 0.5 })
   .to(l1, { ...assembledState.l1, duration: 1 }, "<")
   .to(l2, { ...assembledState.l2, duration: 1 }, "<")
   .to(l3, { ...assembledState.l3, duration: 1 }, "<")
   .to(l4, { ...assembledState.l4, duration: 1 }, "<")
   .to(l5, { ...assembledState.l5, duration: 1 }, "<")
   .to(l6, { ...assembledState.l6, duration: 1 }, "<")
   .to(l7, { ...assembledState.l7, duration: 1 }, "<")
   .to(l8, { ...assembledState.l8, duration: 1 }, "<");"""

content = content.replace(step3_old, step3_new)

with open("script.js", "w") as f:
    f.write(content)

print("Updated script.js successfully!")
