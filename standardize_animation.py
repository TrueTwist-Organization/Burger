import glob
import re

html_files = glob.glob('*_burger.html')

# Extract the script from avocado_smash_burger.html
with open('avocado_smash_burger.html', 'r', encoding='utf-8') as f:
    avocado_html = f.read()

script_pattern = r"<script>\s*document\.addEventListener\('DOMContentLoaded', \(\) => \{\s*if \(typeof gsap === 'undefined'\) return;.*?\}\);\s*</script>"
match = re.search(script_pattern, avocado_html, flags=re.DOTALL)
if match:
    standard_script = match.group(0)
    
    for file in html_files:
        if file == 'avocado_smash_burger.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace the script in other files
        html = re.sub(script_pattern, standard_script, html, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
            
    print("Standardized GSAP animations on all pages!")
else:
    print("Could not find script pattern in avocado_smash_burger.html")
