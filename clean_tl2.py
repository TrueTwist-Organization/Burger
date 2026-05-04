with open('script.js', 'r') as f:
    js = f.read()

import re
# Remove the burgerContainer animation from tl2
js = re.sub(r'\.to\(burgerContainer,\s*\{[^}]+\},\s*0\)', '', js)

with open('script.js', 'w') as f:
    f.write(js)
print("Removed burgerContainer from tl2")
