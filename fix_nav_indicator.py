with open('script.js', 'r') as f:
    js = f.read()

# Add a check in updateNavIndicator to gracefully hide or ignore if no activeLink
new_func = """function updateNavIndicator() {
    const indicator = document.querySelector('.nav-indicator');
    const activeLink = document.querySelector('.nav-link.active');
    
    if (activeLink && indicator) {
        indicator.style.width = activeLink.offsetWidth + 'px';
        indicator.style.left = activeLink.offsetLeft + 'px';
        indicator.style.opacity = '1';
    } else if (indicator) {
        indicator.style.opacity = '0';
    }
}"""

import re
js = re.sub(r'function updateNavIndicator\(\) \{.*?\n\}', new_func, js, flags=re.DOTALL)

with open('script.js', 'w') as f:
    f.write(js)
    
print("Fixed script.js nav indicator.")
