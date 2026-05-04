import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace explodedState
exploded_pattern = r'const explodedState = \{.*?l8:.*?\} \};'
# Wait, regex across multiple lines can be tricky. Let's just find and replace the exact blocks.
# Let's read lines and just replace between the markers.

lines = js.split('\n')
new_lines = []
skip = False

for line in lines:
    if "const explodedState = {" in line:
        skip = True
        new_lines.append("""// Exploded Positions (Tighter spread, to match the single side label layout)
const explodedState = {
    l1: { yPercent: -12, scale: 1, rotation: 0 },
    l2: { yPercent: -7, scale: 1, rotation: 0 },
    l3: { yPercent: -2, scale: 1, rotation: 0 },
    l4: { yPercent: 3, scale: 1, rotation: 0 },
    l5: { yPercent: 8, scale: 1, rotation: 0 },
    l6: { yPercent: 13, scale: 1, rotation: 0 },
    l7: { yPercent: 18, scale: 1, rotation: 0 },
    l8: { yPercent: 25, scale: 1, rotation: 0 }
};""")
        continue
    
    if "const assembledState = {" in line:
        skip = True
        new_lines.append("""// Real assembled state (squished tightly together)
const assembledState = {
    l1: { yPercent: 28, scale: 0.95, rotation: 0 },
    l2: { yPercent: 22, scale: 0.95, rotation: 0 },
    l3: { yPercent: 16, scale: 0.95, rotation: 0 },
    l4: { yPercent: 10, scale: 0.95, rotation: 0 },
    l5: { yPercent: 4, scale: 0.95, rotation: 0 },
    l6: { yPercent: -2, scale: 0.95, rotation: 0 },
    l7: { yPercent: -12, scale: 0.95, rotation: 0 },
    l8: { yPercent: -28, scale: 0.95, rotation: 0 }
};""")
        continue

    if skip and "};" in line:
        skip = False
        continue
        
    if not skip:
        new_lines.append(line)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Updated script.js")
