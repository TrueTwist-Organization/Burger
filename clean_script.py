import re

with open('script.js', 'r') as f:
    js = f.read()

# Remove tl_transition block
js = re.sub(r'// Timeline 1: Transition into Exploded View.*?// Check if mobile for bottom position', '// Old tl_transition removed\n', js, flags=re.DOTALL)

# Remove tl_explode block
js = re.sub(r'// Timeline 2: Explode and Reassemble.*?\} // End if\(l1\)', '} // End if(l1)', js, flags=re.DOTALL)

with open('script.js', 'w') as f:
    f.write(js)
print("Cleaned up old timelines in script.js")
