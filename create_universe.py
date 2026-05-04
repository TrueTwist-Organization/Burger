import re

css_content = """
/* ━━━ FLOATING BURGER UNIVERSE ━━━ */
.sec-menu-universe {
    position: relative;
    background-color: #F5ECD7;
    padding: 100px 20px;
    overflow: hidden;
    color: #2C1810;
    cursor: none; /* custom cursor */
}

/* Ambient Backgrounds */
.universe-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: 0;
    pointer-events: none;
    background-image: radial-gradient(rgba(0,0,0,0.04) 2px, transparent 2px);
    background-size: 30px 30px;
}
.universe-vignette {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: 0;
    pointer-events: none;
    box-shadow: inset 0 0 150px rgba(0,0,0,0.1);
}
.blob-orange {
    position: absolute; bottom: -10%; left: -10%;
    width: 600px; height: 600px;
    background: #E67E22;
    border-radius: 50%;
    filter: blur(150px);
    opacity: 0.15;
    z-index: 0;
}
.blob-red {
    position: absolute; top: -10%; right: -10%;
    width: 600px; height: 600px;
    background: #C0392B;
    border-radius: 50%;
    filter: blur(150px);
    opacity: 0.15;
    z-index: 0;
}
.bg-lineart {
    position: absolute;
    opacity: 0.08;
    animation: slowRotate 60s linear infinite;
    z-index: 0;
    width: 300px;
}
@keyframes slowRotate { 100% { transform: rotate(360deg); } }

/* Marquee */
.menu-marquee {
    position: absolute;
    top: 0; left: 0; width: 100%;
    background: #C0392B;
    color: #FFF8F0;
    padding: 10px 0;
    font-size: 0.9rem;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    z-index: 10;
    box-shadow: 0 4px 15px rgba(192,57,43,0.3);
}
.marquee-content {
    display: inline-block;
    animation: marquee 20s linear infinite;
}
@keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* Section Title */
.universe-header-container {
    text-align: center;
    position: relative;
    z-index: 2;
    margin-bottom: 80px;
}
.title-badge {
    display: inline-flex;
    align-items: center;
    background: #C0392B;
    color: white;
    padding: 8px 16px;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: bold;
    letter-spacing: 1px;
    margin-bottom: 20px;
    animation: bounceBadge 2s infinite;
}
@keyframes bounceBadge { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
.title-badge .flame { margin-left: 5px; animation: flicker 0.5s infinite alternate; }
@keyframes flicker { 0% { opacity: 0.8; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1.1); } }

.universe-title {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    color: #C0392B;
    text-shadow: 4px 4px 0px rgba(180,50,20,0.15);
    display: flex;
    justify-content: center;
    position: relative;
}
.universe-title .char {
    display: inline-block;
    opacity: 0;
    transform: translateY(-50px);
}
.floating-burger-title {
    font-size: 3rem;
    margin-left: 15px;
    animation: floatTitleRotate 4s ease-in-out infinite;
    display: inline-block;
}
@keyframes floatTitleRotate { 0%, 100% { transform: translateY(0) rotate(-10deg); } 50% { transform: translateY(-10px) rotate(10deg); } }

.brush-stroke {
    width: 300px;
    margin: -20px auto 0 auto;
    display: block;
}
.brush-stroke path {
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
}

/* Cards Horizontal Scroll */
.universe-cards-container {
    position: relative;
    z-index: 2;
    display: flex;
    gap: 40px;
    padding: 60px 40px;
    overflow-x: auto;
    cursor: grab;
    scroll-behavior: smooth;
    /* Hide scrollbar */
    -ms-overflow-style: none;  
    scrollbar-width: none;  
}
.universe-cards-container::-webkit-scrollbar { display: none; }
.universe-cards-container:active { cursor: grabbing; }

/* The Card */
.u-card {
    min-width: 320px;
    background: #FFFDF8;
    border-radius: 28px;
    padding: 30px;
    position: relative;
    box-shadow: 0 4px 6px rgba(0,0,0,0.04), 0 12px 24px rgba(180,80,20,0.10), 0 32px 48px rgba(180,80,20,0.06);
    transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
    opacity: 0;
    transform: translateY(60px) rotate(8deg);
    margin-top: 50px;
}
.u-card:nth-child(odd) { transform: translateY(0) rotate(-1.5deg); }
.u-card:nth-child(even) { transform: translateY(0) rotate(1.5deg); }

/* Card Hover */
.u-card:hover {
    transform: translateY(-16px) rotate(0deg) !important;
    box-shadow: 0 40px 80px rgba(180,80,20,0.25), inset 0 0 0 2px rgba(230,126,34,0.5);
    background: radial-gradient(circle at center, #FFFDF8 0%, #FFEFE5 100%);
    z-index: 10;
}

/* Hero Burger Image */
.u-burger-wrapper {
    position: relative;
    margin-top: -80px;
    margin-bottom: 20px;
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.u-burger-img {
    width: 220px;
    filter: drop-shadow(0 20px 10px rgba(0,0,0,0.2));
    transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
    animation: floatBurger 3s ease-in-out infinite;
}
@keyframes floatBurger { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }

/* Stagger float animations for cards */
.u-card:nth-child(1) .u-burger-img { animation-delay: 0s; }
.u-card:nth-child(2) .u-burger-img { animation-delay: 0.5s; }
.u-card:nth-child(3) .u-burger-img { animation-delay: 1.0s; }
.u-card:nth-child(4) .u-burger-img { animation-delay: 1.5s; }

/* Fake shadow below burger */
.u-burger-shadow {
    position: absolute;
    bottom: -10px; left: 50%;
    transform: translateX(-50%);
    width: 140px; height: 20px;
    background: radial-gradient(ellipse at center, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0) 70%);
    transition: all 0.5s;
}

.u-card:hover .u-burger-img {
    transform: scale(1.08) translateY(-12px);
    filter: drop-shadow(0 30px 15px rgba(0,0,0,0.3));
    animation-play-state: paused;
}
.u-card:hover .u-burger-shadow {
    width: 160px; opacity: 0.5;
}

/* Steam Effect */
.u-steam {
    position: absolute;
    top: -20px;
    width: 10px; height: 30px;
    background: rgba(255,255,255,0.6);
    border-radius: 50%;
    filter: blur(8px);
    opacity: 0;
    transition: all 0.5s;
}
.s1 { left: 40%; animation-delay: 0s; }
.s2 { left: 50%; animation-delay: 0.3s; }
.s3 { left: 60%; animation-delay: 0.6s; }

.u-card:hover .u-steam {
    animation: riseSteam 2s infinite ease-in;
}
@keyframes riseSteam { 0% { transform: translateY(0) scale(1); opacity: 0; } 50% { opacity: 0.8; } 100% { transform: translateY(-40px) scale(2); opacity: 0; } }

/* Card Info */
.u-card-info { text-align: center; }
.u-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #2C1810;
    margin-bottom: 10px;
    text-decoration: none;
    display: block;
}
.u-divider {
    height: 2px; width: 0;
    background: #E67E22;
    margin: 0 auto 15px auto;
    transition: width 0.4s ease;
}
.u-card:hover .u-divider { width: 50px; }

/* Price Slot Machine */
.u-price-wrapper {
    font-size: 2rem;
    font-weight: 800;
    color: #C0392B;
    margin-bottom: 15px;
    display: flex;
    justify-content: center;
    align-items: baseline;
}
.u-price-currency { font-size: 1.2rem; margin-right: 2px; }
.u-price-val {
    display: inline-block;
    overflow: hidden;
    height: 2.2rem;
    line-height: 2.2rem;
}

/* Flavor Tags */
.u-flavor-tags {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-bottom: 20px;
    opacity: 0.7;
    transform: translateY(10px);
    transition: all 0.4s ease;
}
.u-card:hover .u-flavor-tags { opacity: 1; transform: translateY(0); }
.u-tag {
    font-size: 0.75rem;
    padding: 4px 10px;
    border-radius: 50px;
    background: rgba(230,126,34,0.1);
    color: #E67E22;
    font-weight: 600;
}

/* Indicators */
.u-indicators {
    margin-bottom: 25px;
    text-align: left;
}
.u-ind-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.75rem;
    margin-bottom: 5px;
    color: #7F8C8D;
}
.u-bars { display: flex; gap: 3px; }
.u-bar { width: 12px; height: 6px; background: #eee; border-radius: 3px; transition: all 0.5s; }
.u-card:hover .u-ind-row.spice .u-bar.fill { background: #C0392B; }
.u-card:hover .u-ind-row.taste .u-bar.fill { background: #E67E22; }
.u-card:hover .u-ind-row.juice .u-bar.fill { background: #F39C12; }

/* Add to Cart Button */
.u-btn-cart {
    width: 100%;
    padding: 16px;
    border-radius: 50px;
    background: linear-gradient(135deg, #C0392B, #E74C3C);
    color: white;
    border: none;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 1px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0;
}
.u-btn-icon { width: 0; opacity: 0; overflow: hidden; transition: all 0.3s; white-space: nowrap; }
.u-btn-cart:hover {
    transform: scale(1.02);
    box-shadow: 0 10px 20px rgba(192,57,43,0.3);
}
.u-btn-cart:hover .u-btn-icon { width: 20px; opacity: 1; margin-right: 8px; }

/* Button Click sequence */
.u-btn-cart.clicked { animation: btnCompress 0.2s forwards; }
@keyframes btnCompress { 50% { transform: scale(0.94); } 100% { transform: scale(1); } }
.u-btn-cart.loading { pointer-events: none; }
.u-btn-cart.loading .u-btn-text, .u-btn-cart.loading .u-btn-icon { display: none; }
.u-btn-cart.loading::after { content: '🍔'; animation: spin 0.8s linear infinite; }
.u-btn-cart.success { background: #27AE60 !important; box-shadow: 0 10px 20px rgba(39,174,96,0.3); }

/* View More Button */
.u-view-more-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 50px;
    position: relative;
    z-index: 2;
}
.u-view-more {
    background: #C0392B;
    color: white;
    padding: 18px 40px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: bold;
    border: none;
    cursor: pointer;
    position: relative;
    box-shadow: 0 0 0 0 rgba(192,57,43,0.7);
    animation: pulseGlow 2s infinite;
    transition: all 0.3s;
    overflow: hidden;
}
@keyframes pulseGlow { 70% { box-shadow: 0 0 0 15px rgba(192,57,43,0); } 100% { box-shadow: 0 0 0 0 rgba(192,57,43,0); } }
.u-view-more .arrow { display: inline-block; margin-left: -15px; opacity: 0; transition: all 0.3s; }
.u-view-more:hover { transform: scale(1.05); padding-right: 30px; }
.u-view-more:hover .arrow { margin-left: 10px; opacity: 1; }

.orbiting-dots { position: absolute; top: 50%; left: 50%; width: 100%; height: 100%; pointer-events: none; }
.o-dot { position: absolute; font-size: 1.2rem; transform-origin: center; transition: all 0.3s; animation: viewOrbit 4s linear infinite; }
@keyframes viewOrbit { 0% { transform: rotate(calc(var(--i) * 90deg)) translateX(100px) rotate(calc(var(--i) * -90deg)); } 100% { transform: rotate(calc(var(--i) * 90deg + 360deg)) translateX(100px) rotate(calc(var(--i) * -90deg - 360deg)); } }
.u-view-more:hover ~ .orbiting-dots .o-dot { animation-duration: 2s; }

/* Custom Cursor */
.u-cursor {
    position: fixed;
    top: 0; left: 0;
    width: 30px; height: 30px;
    font-size: 24px;
    pointer-events: none;
    z-index: 9999;
    transform: translate(-50%, -50%);
    transition: transform 0.1s;
    display: none;
}
.u-cursor-trail {
    position: fixed;
    width: 6px; height: 6px;
    background: #E67E22;
    border-radius: 50%;
    pointer-events: none;
    z-index: 9998;
    transform: translate(-50%, -50%);
    animation: fadeTrail 0.5s forwards;
}
@keyframes fadeTrail { to { opacity: 0; transform: translate(-50%, -50%) scale(0); } }

/* Flying Burger */
.flying-burger {
    position: fixed;
    z-index: 10000;
    width: 150px;
    transition: all 1s cubic-bezier(0.25, 1, 0.5, 1);
    pointer-events: none;
}

@media (max-width: 768px) {
    .universe-title { font-size: 2.5rem; }
    .floating-burger-title { font-size: 2rem; }
    .u-card { min-width: 280px; }
}
"""

js_content = """
// FLOATING BURGER UNIVERSE LOGIC

document.addEventListener('DOMContentLoaded', () => {
    // 1. Entrance Animations for Letters
    const titleContainer = document.getElementById('u-title');
    if(titleContainer) {
        const text = "EXPLORE OUR MENU";
        titleContainer.innerHTML = '';
        text.split('').forEach((char, i) => {
            if(char === ' ') {
                titleContainer.innerHTML += '&nbsp;';
            } else {
                const span = document.createElement('span');
                span.className = 'char';
                span.innerText = char;
                span.style.animation = `dropWord 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) ${i * 0.04}s forwards`;
                titleContainer.appendChild(span);
            }
        });
        titleContainer.innerHTML += '<span class="floating-burger-title">🍔</span>';
        
        // Draw brush stroke after text
        setTimeout(() => {
            const path = document.querySelector('.brush-stroke path');
            if(path) {
                path.style.transition = 'stroke-dashoffset 1.2s ease';
                path.style.strokeDashoffset = '0';
            }
        }, text.length * 40 + 500);
    }
    
    // 2. Entrance Animation for Cards
    const cards = document.querySelectorAll('.u-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                cards.forEach((card, i) => {
                    setTimeout(() => {
                        card.style.opacity = '1';
                        // Keep the alternating rotation logic by removing transform override after fade in
                        // Actually better to handle via CSS class
                        card.classList.add('animate-in');
                    }, i * 120);
                });
                observer.disconnect();
            }
        });
    });
    
    const universeSec = document.getElementById('universe-menu');
    if(universeSec) observer.observe(universeSec);

    // 3. Horizontal Scroll dragging
    const slider = document.querySelector('.universe-cards-container');
    let isDown = false;
    let startX;
    let scrollLeft;

    if(slider) {
        slider.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - slider.offsetLeft;
            scrollLeft = slider.scrollLeft;
        });
        slider.addEventListener('mouseleave', () => { isDown = false; });
        slider.addEventListener('mouseup', () => { isDown = false; });
        slider.addEventListener('mousemove', (e) => {
            if(!isDown) return;
            e.preventDefault();
            const x = e.pageX - slider.offsetLeft;
            const walk = (x - startX) * 2; // scroll-fast
            slider.scrollLeft = scrollLeft - walk;
        });
    }

    // 4. Custom Cursor
    const cursor = document.getElementById('u-cursor');
    if(universeSec && cursor) {
        universeSec.addEventListener('mousemove', (e) => {
            cursor.style.display = 'block';
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
            
            // Trail
            if(Math.random() > 0.5) {
                const trail = document.createElement('div');
                trail.className = 'u-cursor-trail';
                trail.style.left = e.clientX + 'px';
                trail.style.top = e.clientY + 'px';
                document.body.appendChild(trail);
                setTimeout(() => trail.remove(), 500);
            }
        });
        universeSec.addEventListener('mouseleave', () => {
            cursor.style.display = 'none';
        });
        
        // Buttons hover
        document.querySelectorAll('.u-btn-cart, .u-view-more').forEach(btn => {
            btn.addEventListener('mouseenter', () => {
                cursor.innerHTML = '👆';
                cursor.style.textShadow = '0 0 10px red';
            });
            btn.addEventListener('mouseleave', () => {
                cursor.innerHTML = '🍔';
                cursor.style.textShadow = 'none';
            });
        });
    }
});

// Slot machine price effect
function rollPrice(element, finalPrice) {
    if(element.dataset.rolling === 'true') return;
    element.dataset.rolling = 'true';
    
    let ticks = 0;
    const interval = setInterval(() => {
        element.innerText = Math.floor(Math.random() * 900) + 100;
        ticks++;
        if(ticks > 10) {
            clearInterval(interval);
            element.innerText = finalPrice;
            setTimeout(() => { element.dataset.rolling = 'false'; }, 1000);
        }
    }, 50);
}

// Add to Cart Magic
function addUniverseCart(btn, name, price) {
    if(btn.classList.contains('loading')) return;
    
    // UI states
    btn.classList.add('clicked');
    setTimeout(() => btn.classList.remove('clicked'), 200);
    
    btn.classList.add('loading');
    
    // Flying Burger Logic
    const card = btn.closest('.u-card');
    const burgerImg = card.querySelector('.u-burger-img');
    const cartIcon = document.querySelector('.cart-icon') || document.querySelector('.fa-cart-shopping');
    
    if(burgerImg && cartIcon) {
        const startRect = burgerImg.getBoundingClientRect();
        const endRect = cartIcon.getBoundingClientRect();
        
        const flying = document.createElement('img');
        flying.src = burgerImg.src;
        flying.className = 'flying-burger';
        flying.style.left = startRect.left + 'px';
        flying.style.top = startRect.top + 'px';
        flying.style.width = startRect.width + 'px';
        document.body.appendChild(flying);
        
        // Animate parabolic arc using cubic-bezier for x and linear for y or vice versa
        // Actually simpler: CSS transitions
        setTimeout(() => {
            flying.style.left = endRect.left + 'px';
            flying.style.top = endRect.top + 'px';
            flying.style.width = '20px';
            flying.style.opacity = '0.5';
            flying.style.transform = 'rotate(360deg)';
        }, 50);
        
        setTimeout(() => {
            flying.remove();
            // Cart icon bounce
            cartIcon.style.transform = 'scale(1.5)';
            setTimeout(() => cartIcon.style.transform = 'scale(1)', 200);
            
            // Proceed to cart
            addToCart(name, price); // original function
        }, 1050);
    }
    
    // Button Success
    setTimeout(() => {
        btn.classList.remove('loading');
        btn.classList.add('success');
        btn.innerHTML = '<svg style="width:20px;height:20px" viewBox="0 0 24 24"><path fill="none" stroke="white" stroke-width="3" d="M5 13l4 4L19 7"/></svg> <span style="margin-left:5px">Added!</span>';
        
        setTimeout(() => {
            btn.classList.remove('success');
            btn.innerHTML = '<i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>';
        }, 2000);
    }, 800);
}
"""

menu_html = """
    <!-- FLOATING BURGER UNIVERSE MENU -->
    <section class="sec-menu-universe" id="universe-menu">
        <div class="u-cursor" id="u-cursor">🍔</div>
        
        <!-- Ambient Backgrounds -->
        <div class="universe-bg"></div>
        <div class="universe-vignette"></div>
        <div class="blob-orange"></div>
        <div class="blob-red"></div>
        <img src="burger_lineart.svg" class="bg-lineart" style="top:10%; left:5%" alt="">
        <img src="burger_lineart.svg" class="bg-lineart" style="bottom:10%; right:5%; width:400px; animation-duration:90s; animation-direction: reverse;" alt="">
        
        <!-- Marquee -->
        <div class="menu-marquee">
            <div class="marquee-content">
                🔥 BEST SELLERS &nbsp;·&nbsp; FRESH DAILY &nbsp;·&nbsp; ORDER NOW &nbsp;·&nbsp; FREE DELIVERY ABOVE ₹499 &nbsp;·&nbsp; 🍔 MADE WITH LOVE &nbsp;·&nbsp; 
                🔥 BEST SELLERS &nbsp;·&nbsp; FRESH DAILY &nbsp;·&nbsp; ORDER NOW &nbsp;·&nbsp; FREE DELIVERY ABOVE ₹499 &nbsp;·&nbsp; 🍔 MADE WITH LOVE &nbsp;·&nbsp;
                🔥 BEST SELLERS &nbsp;·&nbsp; FRESH DAILY &nbsp;·&nbsp; ORDER NOW &nbsp;·&nbsp; FREE DELIVERY ABOVE ₹499 &nbsp;·&nbsp; 🍔 MADE WITH LOVE &nbsp;·&nbsp;
            </div>
        </div>
        
        <div class="universe-header-container">
            <div class="title-badge">🍔 FRESHLY MADE DAILY <i class="fa-solid fa-fire flame"></i></div>
            <h2 class="universe-title" id="u-title">EXPLORE OUR MENU</h2>
            <svg class="brush-stroke" viewBox="0 0 300 20">
                <path d="M 10 15 Q 150 0 290 15" fill="none" stroke="#C0392B" stroke-width="4" stroke-linecap="round"/>
            </svg>
        </div>
        
        <div class="universe-cards-container">
            
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

        </div>
        
        <div class="u-view-more-wrapper">
            <button class="u-view-more">VIEW FULL MENU <span class="arrow">→</span></button>
            <div class="orbiting-dots">
                <span class="o-dot" style="--i:1;">🍔</span>
                <span class="o-dot" style="--i:2;">🍔</span>
                <span class="o-dot" style="--i:3;">🍔</span>
                <span class="o-dot" style="--i:4;">🍔</span>
            </div>
        </div>
        
    </section>
"""

# 1. Save CSS
with open('universe.css', 'w') as f:
    f.write(css_content)

# 2. Save JS
with open('universe.js', 'w') as f:
    f.write(js_content)

# 3. Modify index.html
with open('index.html', 'r') as f:
    html = f.read()

# Replace old sec-menu
import re
pattern = re.compile(r'<section class="sec-menu" id="menu">.*?</section>', re.DOTALL)
html = re.sub(pattern, menu_html, html)

# Inject CSS and JS links into index.html
if 'universe.css' not in html:
    html = html.replace('</head>', '    <link rel="stylesheet" href="universe.css">\n</head>')
if 'universe.js' not in html:
    html = html.replace('</body>', '    <script src="universe.js"></script>\n</body>')

with open('index.html', 'w') as f:
    f.write(html)

print("Created Floating Burger Universe successfully.")
