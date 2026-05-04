import re

burgers = [
    {"name": "Classic Cheese Burger", "price": "200", "img": "classic_cheese_burger.png", "tags": ["🧀 Cheesy", "🥬 Fresh"], "url": "classic_cheese_burger.html"},
    {"name": "Veggie Burger", "price": "180", "img": "veggie_burger.png", "tags": ["🌱 Healthy", "🌿 Fresh"], "url": "veggie_burger.html"},
    {"name": "Avocado Smash Burger", "price": "220", "img": "avocado_smash_burger.png", "tags": ["🥑 Creamy", "🥑 Superfood"], "url": "avocado_smash_burger.html"},
    {"name": "Mushroom Swiss Burger", "price": "280", "img": "mushroom_swiss_burger.png", "tags": ["🍄 Earthy", "🧀 Cheesy"], "url": "mushroom_swiss_burger.html"},
    {"name": "Spicy Chicken Burger", "price": "240", "img": "spicy_chicken_burger.png", "tags": ["🌶️ Spicy", "🍗 Crispy"], "url": "spicy_chicken_burger.html"},
    {"name": "BBQ Bacon Burger", "price": "260", "img": "bbq_bacon_burger.png", "tags": ["🥓 Smokey", "🥩 Meaty"], "url": "bbq_bacon_burger.html", "extra": True},
    {"name": "Truffle Mayo Burger", "price": "300", "img": "truffle_mayo_burger.png", "tags": ["🍄 Rich", "✨ Premium"], "url": "truffle_mayo_burger.html", "extra": True},
    {"name": "Hawaiian Pineapple Burger", "price": "250", "img": "hawaiian_pineapple_burger.png", "tags": ["🍍 Sweet", "🏝️ Tropical"], "url": "hawaiian_pineapple_burger.html", "extra": True},
    {"name": "Classic Smash Burger", "price": "210", "img": "classic_smash_burger.png", "tags": ["🍔 Crispy", "😋 Juicy"], "url": "classic_smash_burger.html", "extra": True}
]

cards_html = ""
for i, b in enumerate(burgers):
    tags_html = "".join([f'<span class="u-tag">{t}</span>' for t in b["tags"]])
    
    card = f"""
            <!-- Card {i+1} -->
            <div class="u-card" onmouseenter="rollPrice(this.querySelector('.u-price-val'), '{b['price']}')">
                <div class="u-burger-wrapper">
                    <div class="u-steam s1"></div>
                    <div class="u-steam s2"></div>
                    <div class="u-steam s3"></div>
                    <a href="{b['url']}" style="display:block; z-index:10; position:relative;"><img src="{b['img']}" class="u-burger-img" alt="Burger"></a>
                    <div class="u-burger-shadow"></div>
                </div>
                <div class="u-card-info">
                    <a href="{b['url']}" class="u-card-title">{b['name']}</a>
                    <div class="u-divider"></div>
                    <div class="u-price-wrapper">
                        <span class="u-price-currency">₹</span><span class="u-price-val">{b['price']}</span>
                    </div>
                    <div class="u-flavor-tags">
                        {tags_html}
                    </div>
                    <div class="u-indicators">
                        <div class="u-ind-row spice">Spice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row taste">Taste <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row juice">Juice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                    </div>
                    <button class="u-btn-cart" onclick="addUniverseCart(this, '{b['name']}', '₹{b['price']}')">
                        <i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>
                    </button>
                </div>
            </div>"""
    cards_html += card

view_more_html = """
        </div>
        </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything inside <div class="universe-cards-container"> ... </div>
pattern = re.compile(r'<div class="universe-cards-container">.*?</section>', re.DOTALL)

# For CSS marquee, we use universe-cards-container as viewport, and inner container as track
new_content = '<div class="universe-cards-container" style="overflow: hidden; white-space: nowrap; padding: 60px 0 60px 40px;"><div class="marquee-track" style="display: flex; gap: 40px; padding-right: 40px; animation: scrollMarquee 30s linear infinite;">' + cards_html + cards_html + view_more_html + '    </section>'

content = pattern.sub(new_content, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu updated successfully!")
