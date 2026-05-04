import re

with open('index.html', 'r') as f:
    html = f.read()

# Find all menu cards
cards = re.findall(r'<div class="menu-card[^"]*">(.*?)</div>\s*(?:<!--|<\/div)', html, re.DOTALL)

for i, card in enumerate(cards):
    if '<div class="card-inner">' in card:
        continue # Already updated
    
    # Extract info for the back side
    title_match = re.search(r'<h3>(.*?)</h3>', card)
    title = title_match.group(1) if title_match else "Burger"
    
    # Create the new structure
    new_card = f'''
        <div class="card-inner">
            <div class="card-front">
                {card.strip()}
            </div>
            <div class="card-back">
                <h3>{title}</h3>
                <ul>
                    <li>Freshly baked artisan bun</li>
                    <li>Premium quality patty</li>
                    <li>Crisp organic vegetables</li>
                    <li>Our signature secret sauce</li>
                    <li>Melted premium cheese</li>
                </ul>
                <p style="margin-top:20px; font-style:italic; font-size:0.9rem;">Tap again to flip back.</p>
            </div>
        </div>
'''
    html = html.replace(f'<div class="menu-card">\n{card}', f'<div class="menu-card" onclick="this.classList.toggle(\'flipped\')">\n{new_card}')

with open('index.html', 'w') as f:
    f.write(html)
