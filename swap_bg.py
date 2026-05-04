import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the hero section
# We want to restore the correct content and add the background to sec-landing
correct_hero = """    <section class="sec-landing" id="home" style="background-image: url('promo_banner.png'); background-size: cover; background-position: center; background-attachment: fixed; background-repeat: no-repeat;">
        <!-- Left content -->
        <div class="hero-content">
            <h1 style="font-family: 'Bangers', cursive; font-size: 5rem; line-height: 1; color: #D32F2F; text-shadow: 2px 2px 0 #FFF, 4px 4px 0 rgba(0,0,0,0.1);">CRAFTED WITH FLAVOR<br><span style="color: #E85A1F;">SERVED WITH LOVE</span></h1>
            <p style="font-size: 1.2rem; margin: 20px 0; color: #555; max-width: 500px; font-weight: 500;">From sizzling patties fresh off the grill to crisp veggies, each burger is crafted with passion. We believe in better ingredients, amazing taste, and an unforgettable experience.</p>
            <div class="hero-ctas">
                <a href="#menu" class="cta-primary">View Menu</a>
                <a href="#menu" class="cta-secondary">Order Now</a>
            </div>
        </div>"""

# Replace whatever is between <section class="sec-landing" id="home"... and <!-- Chef 1 -->
pattern = r'<section class="sec-landing" id="home".*?(?=<!-- Chef 1 -->)'
html = re.sub(pattern, correct_hero + '\n        ', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed the hero section!")
