import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update openSearchModal function
    # It currently has: modal.classList.remove('hidden');
    # We want it to also have: modal.style.display = 'flex';
    # And close to have modal.style.display = 'none';
    
    # Let's replace the whole function block to be completely safe
    # We can just replace the definition of openSearchModal and closeSearchModal
    
    html = re.sub(
        r'modal\.classList\.remove\(\'hidden\'\);',
        r"modal.classList.remove('hidden');\n            modal.style.display = 'flex';",
        html
    )
    
    html = re.sub(
        r'document\.getElementById\(\'search-modal\'\)\.classList\.add\(\'hidden\'\);',
        r"document.getElementById('search-modal').classList.add('hidden');\n            document.getElementById('search-modal').style.display = 'none';",
        html
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed the search modal to properly show and hide!")
