import glob
import re

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update GSAP initial state to scale down on mobile
    setup_code = '''
            if (window.innerWidth < 768) {
                gsap.set("#naughty-chef", { width: 300, right: -100, bottom: -20 });
                gsap.set("#chef-speech", { scale: 0.5, transformOrigin: "bottom right", right: -20, top: 0 });
            }
            const tl = gsap.timeline();'''
    
    html = re.sub(r'const tl = gsap\.timeline\(\);', setup_code, html)
    
    # 2. Update x movement for naughty chef
    html = re.sub(
        r'x: -350,(\s*rotation: -5,)',
        r'x: window.innerWidth < 768 ? -180 : -350,\1',
        html
    )
    
    # 3. Update exit animation x movement
    html = re.sub(
        r'x: 400,(\s*duration: 1\.5,)',
        r'x: window.innerWidth < 768 ? 200 : 400,\1',
        html
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated GSAP animations to be mobile-responsive!")
