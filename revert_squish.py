import re

with open("index.html", "r") as f:
    html = f.read()

squished_burger = """    <!-- Fixed Burger Container (Center) -->
    <div class="burger-container" id="burger-container">
        <!-- Re-ordered based on stacking: Top bun is highest z-index -->
        <img src="layer8_bottombun.png" class="burger-layer" id="layer-8" alt="Bottom Bun" style="z-index: 1; transform: translateY(-28%) scale(0.95);">
        <img src="layer7_patty.png" class="burger-layer" id="layer-7" alt="Patty" style="z-index: 2; transform: translateY(-20%) scale(0.96);">
        <img src="layer6_cheese.png" class="burger-layer" id="layer-6" alt="Cheese" style="z-index: 3; transform: translateY(-14%) scale(0.97);">
        <img src="layer5_pickles.png" class="burger-layer" id="layer-5" alt="Pickles" style="z-index: 4; transform: translateY(-8%) scale(0.98);">
        <img src="layer4_onions.png" class="burger-layer" id="layer-4" alt="Onions" style="z-index: 5; transform: translateY(-4%) scale(1);">
        <img src="layer3_tomatoes.png" class="burger-layer" id="layer-3" alt="Tomatoes" style="z-index: 6; transform: translateY(6%) scale(1);">
        <img src="layer2_lettuce.png" class="burger-layer" id="layer-2" alt="Lettuce" style="z-index: 7; transform: translateY(12%) scale(0.98);">
        <img src="layer1_topbun.png" class="burger-layer" id="layer-1" alt="Top Bun" style="z-index: 8; transform: translateY(28%) scale(0.95);">
    </div>"""

original_burger = """    <!-- Fixed Burger Container (Center) -->
    <div class="burger-container" id="burger-container">
        <!-- Re-ordered based on stacking: Top bun is highest z-index -->
        <img src="layer8_bottombun.png" class="burger-layer" id="layer-8" alt="Bottom Bun" style="z-index: 1;">
        <img src="layer7_patty.png" class="burger-layer" id="layer-7" alt="Patty" style="z-index: 2;">
        <img src="layer6_cheese.png" class="burger-layer" id="layer-6" alt="Cheese" style="z-index: 3;">
        <img src="layer5_pickles.png" class="burger-layer" id="layer-5" alt="Pickles" style="z-index: 4;">
        <img src="layer4_onions.png" class="burger-layer" id="layer-4" alt="Onions" style="z-index: 5;">
        <img src="layer3_tomatoes.png" class="burger-layer" id="layer-3" alt="Tomatoes" style="z-index: 6;">
        <img src="layer2_lettuce.png" class="burger-layer" id="layer-2" alt="Lettuce" style="z-index: 7;">
        <img src="layer1_topbun.png" class="burger-layer" id="layer-1" alt="Top Bun" style="z-index: 8;">
    </div>"""

html = html.replace(squished_burger, original_burger)

with open("index.html", "w") as f:
    f.write(html)

print("Squish reverted!")
