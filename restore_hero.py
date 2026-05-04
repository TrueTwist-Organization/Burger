import re

with open("index.html", "r") as f:
    html = f.read()

hero_html = """
    <!-- Fixed Burger Container (Center) -->
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
    </div>

    <!-- Section 1: Landing -->
    <section class="sec-landing" id="home">
        <div class="text-content">
            <svg class="steam-vibe" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <path d="M40,60 C30,40 50,30 45,10" stroke="#E85A1F" stroke-width="4" stroke-linecap="round" fill="none"
                    opacity="0.3" />
                <path d="M60,60 C70,40 50,30 55,10" stroke="#E85A1F" stroke-width="4" stroke-linecap="round" fill="none"
                    opacity="0.3" />
                <path d="M50,70 C40,50 60,40 50,20" stroke="#E85A1F" stroke-width="4" stroke-linecap="round" fill="none"
                    opacity="0.3" />
            </svg>
            <h1>CRAFTED WITH FLAVOR<br>SERVED WITH LOVE</h1>
            <p>From sizzling patties fresh off the grill to crisp veggies, each burger is crafted with passion. We
                believe in better ingredients, amazing taste, and an unforgettable experience.</p>
            <div class="hero-ctas">
                <a href="#menu" class="cta-primary">View Menu</a>
                <a href="#menu" class="cta-secondary">Order Now</a>
            </div>
        </div>
        <!-- Chef 1 -->
        <img src="chef_1.png" class="chef-img chef-1" alt="Cartoon Chef Thumbs Up">
    </section>

    <!-- STATIC INGREDIENTS SECTION (RESPONSIVE) -->"""

html = html.replace("    <!-- STATIC INGREDIENTS SECTION (RESPONSIVE) -->", hero_html)

with open("index.html", "w") as f:
    f.write(html)

with open("script.js", "r") as f:
    js = f.read()

# Add tl_transition back
transition_js = """
// Wait for images to load before setting up ScrollTrigger
window.addEventListener("load", () => {
    // Timeline 1: Landing Transition
    const tl_transition = gsap.timeline({
        scrollTrigger: {
            trigger: ".sec-landing",
            start: "top top",
            end: "bottom top",
            scrub: 1
        }
    });

    tl_transition.to("#burger-container", {
        scale: 0.8,
        yPercent: -10,
        opacity: 0,
        duration: 1
    });
"""

js = js.replace('// Wait for images to load before setting up ScrollTrigger', transition_js)

with open("script.js", "w") as f:
    f.write(js)

print("Hero section restored!")
