import glob

files = glob.glob('*_burger.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Fix the main container inline styles for mobile
    content = content.replace(
        'style="max-width: 1200px; margin: 50px auto; padding: 20px; display: flex; flex-wrap: wrap; gap: 50px; align-items: center; min-height: 70vh;"',
        'class="product-detail-container" style="max-width: 1200px; margin: 50px auto; padding: 20px; display: flex; flex-wrap: wrap; gap: 50px; align-items: center; min-height: 70vh;"'
    )
    
    # 2. Add class to columns
    content = content.replace(
        'style="flex: 1; min-width: 300px; text-align: center; position: relative;" id="burger-img-container"',
        'class="product-img-col" style="flex: 1; min-width: 300px; text-align: center; position: relative;" id="burger-img-container"'
    )
    content = content.replace(
        '<div style="flex: 1; min-width: 300px;">',
        '<div class="product-text-col" style="flex: 1; min-width: 300px;">'
    )
    
    # 3. Make GSAP mobile-friendly
    content = content.replace('x: -800,', 'x: window.innerWidth < 768 ? 0 : -800,')
    content = content.replace('y: -400,', 'y: window.innerWidth < 768 ? -400 : -400,')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated {len(files)} files!")
