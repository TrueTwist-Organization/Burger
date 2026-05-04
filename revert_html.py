import re

old_html_content = """        <div class="universe-cards-container">
            
            <!-- Card 1 -->
            <div class="u-card" onmouseenter="rollPrice(this.querySelector('.u-price-val'), '200')">
                <div class="u-burger-wrapper">
                    <div class="u-steam s1"></div><div class="u-steam s2"></div><div class="u-steam s3"></div>
                    <img src="classic_cheese_burger.png" class="u-burger-img" alt="Burger">
                    <div class="u-burger-shadow"></div>
                </div>
                <div class="u-card-info">
                    <a href="classic_cheese_burger.html" class="u-card-title">Classic Cheese Burger</a>
                    <div class="u-divider"></div>
                    <div class="u-price-wrapper">
                        <span class="u-price-currency">₹</span><span class="u-price-val">200</span>
                    </div>
                    <div class="u-flavor-tags">
                        <span class="u-tag">🧀 Cheesy</span><span class="u-tag">🥬 Fresh</span>
                    </div>
                    <div class="u-indicators">
                        <div class="u-ind-row spice">Spice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row taste">Taste <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                        <div class="u-ind-row juice">Juice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div></div></div>
                    </div>
                    <button class="u-btn-cart" onclick="addUniverseCart(this, 'Classic Cheese Burger', '₹200')">
                        <i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>
                    </button>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="u-card" onmouseenter="rollPrice(this.querySelector('.u-price-val'), '240')">
                <div class="u-burger-wrapper">
                    <div class="u-steam s1"></div><div class="u-steam s2"></div><div class="u-steam s3"></div>
                    <img src="spicy_chicken_burger.png" class="u-burger-img" alt="Burger">
                    <div class="u-burger-shadow"></div>
                </div>
                <div class="u-card-info">
                    <a href="spicy_chicken_burger.html" class="u-card-title">Spicy Chicken Burger</a>
                    <div class="u-divider"></div>
                    <div class="u-price-wrapper">
                        <span class="u-price-currency">₹</span><span class="u-price-val">240</span>
                    </div>
                    <div class="u-flavor-tags">
                        <span class="u-tag">🌶️ Spicy</span><span class="u-tag">🍗 Crispy</span>
                    </div>
                    <div class="u-indicators">
                        <div class="u-ind-row spice">Spice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                        <div class="u-ind-row taste">Taste <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row juice">Juice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                    </div>
                    <button class="u-btn-cart" onclick="addUniverseCart(this, 'Spicy Chicken Burger', '₹240')">
                        <i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>
                    </button>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="u-card" onmouseenter="rollPrice(this.querySelector('.u-price-val'), '260')">
                <div class="u-burger-wrapper">
                    <div class="u-steam s1"></div><div class="u-steam s2"></div><div class="u-steam s3"></div>
                    <img src="bbq_bacon_burger.png" class="u-burger-img" alt="Burger">
                    <div class="u-burger-shadow"></div>
                </div>
                <div class="u-card-info">
                    <a href="bbq_bacon_burger.html" class="u-card-title">BBQ Bacon Burger</a>
                    <div class="u-divider"></div>
                    <div class="u-price-wrapper">
                        <span class="u-price-currency">₹</span><span class="u-price-val">260</span>
                    </div>
                    <div class="u-flavor-tags">
                        <span class="u-tag">🥓 Smokey</span><span class="u-tag">🥩 Meaty</span>
                    </div>
                    <div class="u-indicators">
                        <div class="u-ind-row spice">Spice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row taste">Taste <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                        <div class="u-ind-row juice">Juice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div></div></div>
                    </div>
                    <button class="u-btn-cart" onclick="addUniverseCart(this, 'BBQ Bacon Burger', '₹260')">
                        <i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>
                    </button>
                </div>
            </div>

            <!-- Card 4 -->
            <div class="u-card" onmouseenter="rollPrice(this.querySelector('.u-price-val'), '280')">
                <div class="u-burger-wrapper">
                    <div class="u-steam s1"></div><div class="u-steam s2"></div><div class="u-steam s3"></div>
                    <img src="mushroom_swiss_burger.png" class="u-burger-img" alt="Burger">
                    <div class="u-burger-shadow"></div>
                </div>
                <div class="u-card-info">
                    <a href="mushroom_swiss_burger.html" class="u-card-title">Mushroom Swiss</a>
                    <div class="u-divider"></div>
                    <div class="u-price-wrapper">
                        <span class="u-price-currency">₹</span><span class="u-price-val">280</span>
                    </div>
                    <div class="u-flavor-tags">
                        <span class="u-tag">🍄 Earthy</span><span class="u-tag">🧀 Cheesy</span>
                    </div>
                    <div class="u-indicators">
                        <div class="u-ind-row spice">Spice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar"></div><div class="u-bar"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row taste">Taste <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row juice">Juice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                    </div>
                    <button class="u-btn-cart" onclick="addUniverseCart(this, 'Mushroom Swiss Burger', '₹280')">
                        <i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>
                    </button>
                </div>
            </div>
            
            <!-- Card 5 -->
            <div class="u-card" onmouseenter="rollPrice(this.querySelector('.u-price-val'), '350')">
                <div class="u-burger-wrapper">
                    <div class="u-steam s1"></div><div class="u-steam s2"></div><div class="u-steam s3"></div>
                    <img src="ultimate_monster_burger.png" class="u-burger-img" alt="Burger">
                    <div class="u-burger-shadow"></div>
                </div>
                <div class="u-card-info">
                    <a href="ultimate_monster_burger.html" class="u-card-title">Ultimate Monster</a>
                    <div class="u-divider"></div>
                    <div class="u-price-wrapper">
                        <span class="u-price-currency">₹</span><span class="u-price-val">350</span>
                    </div>
                    <div class="u-flavor-tags">
                        <span class="u-tag">🥩 Huge</span><span class="u-tag">🌶️ Bold</span>
                    </div>
                    <div class="u-indicators">
                        <div class="u-ind-row spice">Spice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar"></div></div></div>
                        <div class="u-ind-row taste">Taste <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                        <div class="u-ind-row juice">Juice <div class="u-bars"><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div><div class="u-bar fill"></div></div></div>
                    </div>
                    <button class="u-btn-cart" onclick="addUniverseCart(this, 'Ultimate Monster', '₹350')">
                        <i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>
                    </button>
                </div>
            </div>
        </div>"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<div class="menu-container">.*?</div>\s*</section>'
new_section_end = old_html_content + "\n    </section>"
new_html = re.sub(pattern, new_section_end, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Reverted HTML.")
