import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Fix the invalid JavaScript syntax and clean up the inline styles
    pattern = r'<span class="menu-toggle" onclick="document\.querySelector\(\\\'nav\\\'\)\.classList\.toggle\(\\\'active\\\'\)"[^>]*>'
    replacement = '<span class="menu-toggle" onclick="document.querySelector(\'nav\').classList.toggle(\'active\')">'
    html = re.sub(pattern, replacement, html)
    
    # Also fix in case the backslashes are not there but display:none is
    pattern2 = r'<span class="menu-toggle" onclick="document\.querySelector\(\'nav\'\)\.classList\.toggle\(\'active\'\)"[^>]*>'
    html = re.sub(pattern2, replacement, html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed the toggle button JS syntax and HTML!")
