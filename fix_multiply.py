import glob
import re

files = glob.glob('*.html')
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        new_content = content.replace(' mix-blend-mode: multiply;', '')
        new_content = new_content.replace('mix-blend-mode: multiply;', '')
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Removed multiply from {f}")
    except Exception as e:
        print(f"Failed on {f}: {e}")
