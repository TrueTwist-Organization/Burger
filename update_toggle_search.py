import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update search icon on product pages
    if file != 'index.html':
        html = html.replace("showToast('Search feature coming soon!')", "window.location.href='index.html#menu'")
        # Also handle any variations
        html = re.sub(r'onclick="showToast\([^)]+\)"(?=[^>]*>🔍)', 'onclick="window.location.href=\'index.html#menu\'"', html)

    # 2. Clean up menu-toggle inline styles to avoid specificity issues
    html = re.sub(
        r'<span class="menu-toggle" onclick="document\.querySelector\(\'nav\'\)\.classList\.toggle\(\'active\'\)" style="[^"]*">',
        r'<span class="menu-toggle" onclick="document.querySelector(\'nav\').classList.toggle(\'active\')">',
        html
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

# 3. Add base CSS for menu-toggle
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

base_css = '''
.menu-toggle {
    display: none;
    cursor: pointer;
    margin-left: 15px;
    color: #D32F2F;
    font-size: 1.5rem;
}
'''
if '.menu-toggle {' not in css:
    css = base_css + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated search functionality and cleaned up toggle CSS!")
