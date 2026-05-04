import re
import glob

# 1. New HTML
new_html = """
    <!-- ENHANCED CART MODAL -->
    <div id="cart-modal" class="modal-overlay cart-backdrop hidden" onclick="handleBackdropClick(event)">
        <div class="cart-flip-container" id="cart-flip-container">
            <div class="cart-flipper" id="cart-flipper">
                
                <!-- FRONT: CART VIEW -->
                <div class="cart-front">
                    <div class="cart-header">
                        <h2>YOUR CART <span class="cart-icon-anim">🛒</span></h2>
                        <button class="close-btn" onclick="closeCartModal()">
                            <i class="fa-solid fa-xmark"></i>
                        </button>
                    </div>
                    <div class="cart-divider"></div>
                    
                    <div id="cart-items-container" class="cart-items-wrapper">
                        <!-- Dynamic Cart Items -->
                    </div>

                    <!-- Promo Code -->
                    <div class="promo-section" id="promo-section" style="display:none;">
                        <div class="promo-toggle" onclick="togglePromo()">Have a promo code? 🏷️</div>
                        <div class="promo-input-container hidden" id="promo-container">
                            <input type="text" id="promo-input" placeholder="Enter code (try: BURGER50)">
                            <button onclick="applyPromo()">Apply</button>
                        </div>
                        <div id="promo-msg"></div>
                    </div>

                    <div class="cart-order-summary" id="cart-order-summary" style="display:none;">
                        <div class="summary-row"><span>Subtotal</span><span id="cart-subtotal">₹0</span></div>
                        <div class="summary-row delivery-row">
                            <span>Delivery <i class="fa-solid fa-circle-info tooltip"><span class="tooltiptext">Free over ₹499</span></i></span>
                            <span id="cart-delivery">₹40</span>
                        </div>
                        <div class="summary-row discount-row hidden" id="discount-row">
                            <span>Discount</span><span id="cart-discount">-₹0</span>
                        </div>
                        <div class="cart-divider thick"></div>
                        <div class="summary-row total-row">
                            <span>TOTAL</span>
                            <div class="total-price-col">
                                <span id="cart-total-price">₹0</span>
                                <small>Inclusive of all taxes</small>
                            </div>
                        </div>
                    </div>

                    <!-- Login / Checkout Action Area -->
                    <div class="checkout-action-area" id="checkout-action-area">
                        <button class="btn-checkout-smart" id="btn-main-checkout" onclick="handleCheckoutClick()">
                            <i class="fa-solid fa-lock lock-icon" id="checkout-lock-icon"></i> <span id="checkout-btn-text">PROCEED TO CHECKOUT</span>
                        </button>
                        
                        <div class="split-choice-panel hidden" id="split-choice-panel">
                            <p>To place your order...</p>
                            <button class="btn-login-choice" onclick="flipToLogin()">
                                <i class="fa-solid fa-user"></i> LOGIN / SIGNUP
                            </button>
                            <div class="choice-divider"><span>or</span></div>
                            <button class="btn-guest-choice" onclick="proceedToCheckout(true)">
                                🚀 CONTINUE AS GUEST
                            </button>
                            <small>Login to earn reward points 🎯</small>
                        </div>
                    </div>
                </div>

                <!-- BACK: LOGIN VIEW -->
                <div class="cart-back">
                    <button class="back-to-cart-btn" onclick="flipToCart()">
                        <i class="fa-solid fa-arrow-left"></i>
                    </button>
                    <div class="login-inner">
                        <h2>Welcome Back! 👋</h2>
                        <form id="cart-login-form" onsubmit="handleCartLogin(event)">
                            <div class="input-group">
                                <input type="email" id="cart-email" required placeholder=" ">
                                <label>Email</label>
                            </div>
                            <div class="input-group">
                                <input type="password" id="cart-password" required placeholder=" ">
                                <label>Password</label>
                                <i class="fa-solid fa-eye toggle-pwd" onclick="toggleCartPwd()"></i>
                            </div>
                            <div class="forgot-link"><a href="#">Forgot Password?</a></div>
                            <button type="submit" class="btn-submit-login">LOGIN</button>
                        </form>
                        <div class="new-here">New here? <a href="#">Sign Up</a></div>
                    </div>
                </div>

            </div>
        </div>
    </div>
"""

pattern = re.compile(r'<div id="cart-modal".*?<!-- Login Modal -->', re.DOTALL)

for h_file in glob.glob("*.html"):
    if h_file == "checkout.html": continue
    with open(h_file, 'r') as f:
        html = f.read()
    if 'id="cart-modal"' in html:
        # replace the old cart modal block
        # we know it's followed by <!-- Login Modal -->
        html = re.sub(pattern, new_html + '\n    <!-- Login Modal -->', html)
        if '<link rel="stylesheet" href="cart_enhanced.css">' not in html:
            html = html.replace('</head>', '    <link rel="stylesheet" href="cart_enhanced.css">\n</head>')
        with open(h_file, 'w') as f:
            f.write(html)
        print(f"Updated HTML structure in {h_file}")

# 2. Generate cart_enhanced.css
css = """
/* ENHANCED CART MODAL */
.cart-backdrop {
    background: rgba(30,10,5,0.6) !important;
    backdrop-filter: blur(8px);
    display: none;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.4s ease;
}
.cart-backdrop.show {
    display: flex;
    opacity: 1;
}

.cart-flip-container {
    perspective: 1000px;
    width: 100%;
    max-width: 480px;
    margin: 0 20px;
    transform: translateY(100%);
    transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.cart-backdrop.show .cart-flip-container {
    transform: translateY(0);
}
.cart-backdrop.show .cart-flip-container.shake-warning {
    animation: shakeWarn 0.4s ease;
}
@keyframes shakeWarn {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

.cart-flipper {
    position: relative;
    width: 100%;
    height: auto;
    transform-style: preserve-3d;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}
.cart-flipper.flipped {
    transform: rotateY(180deg);
}

.cart-front, .cart-back {
    width: 100%;
    backface-visibility: hidden;
    background: #FFFDF8;
    border-radius: 32px;
    padding: 30px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.25);
    border: 2px solid #F5ECD7;
    position: absolute;
    top: 0; left: 0;
}
.cart-front {
    position: relative;
}
.cart-back {
    transform: rotateY(180deg);
    padding-top: 60px;
}

/* Header */
.cart-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.cart-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #2C1810;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 10px;
}
.cart-icon-anim {
    display: inline-block;
    animation: bounceIcon 0.5s ease backwards 0.2s;
}
@keyframes bounceIcon {
    0% { transform: scale(0) rotate(-20deg); }
    50% { transform: scale(1.2) rotate(10deg); }
    100% { transform: scale(1) rotate(0); }
}
.close-btn {
    background: #FFF0E5;
    border: none;
    width: 40px; height: 40px;
    border-radius: 50%;
    font-size: 1.2rem;
    color: #C0392B;
    cursor: pointer;
    transition: all 0.3s;
    display: flex; align-items: center; justify-content: center;
}
.close-btn:hover {
    background: #C0392B;
    color: white;
    transform: rotate(90deg);
}
.cart-divider {
    height: 1px;
    background: linear-gradient(90deg, #E67E22, transparent);
    margin: 20px 0;
}
.cart-divider.thick { height: 2px; margin: 15px 0; }

/* Empty State */
.empty-cart-state {
    text-align: center;
    padding: 30px 0;
}
.empty-bowl {
    font-size: 4rem;
    display: inline-block;
    animation: rockBowl 3s infinite ease-in-out;
}
@keyframes rockBowl { 0%, 100% { transform: rotate(-10deg); } 50% { transform: rotate(10deg); } }
.empty-cart-state h3 { font-family: 'Playfair Display', serif; font-style: italic; color: #2C1810; margin: 10px 0; }
.empty-cart-state p { color: #E67E22; margin-bottom: 25px; }
.floating-bg-emojis {
    position: absolute;
    bottom: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    z-index: -1;
    overflow: hidden;
}
.f-emoji { position: absolute; font-size: 2rem; opacity: 0; animation: floatUpEmoji 4s infinite linear; }
@keyframes floatUpEmoji { 0% { transform: translateY(100px) rotate(0deg); opacity: 0; } 20% { opacity: 0.3; } 80% { opacity: 0.3; } 100% { transform: translateY(-200px) rotate(180deg); opacity: 0; } }
.btn-explore {
    background: linear-gradient(135deg, #C0392B, #E74C3C);
    color: white; border: none; padding: 12px 24px; border-radius: 50px;
    font-weight: bold; cursor: pointer; animation: gentleBounce 2s infinite;
    transition: all 0.3s;
}
.btn-explore:hover { padding-right: 30px; box-shadow: 0 10px 20px rgba(192,57,43,0.3); }

/* Cart Items */
.cart-items-wrapper {
    max-height: 40vh; overflow-y: auto; padding-right: 5px;
}
.cart-items-wrapper::-webkit-scrollbar { width: 4px; }
.cart-items-wrapper::-webkit-scrollbar-thumb { background: #FFCC80; border-radius: 10px; }

.c-item {
    display: flex; align-items: center; justify-content: space-between;
    padding: 15px 0; border-bottom: 1px dashed #E67E22;
    animation: slideInRight 0.4s ease backwards;
    transition: all 0.3s;
}
@keyframes slideInRight { from { transform: translateX(30px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }

.c-item-left { display: flex; align-items: center; gap: 15px; flex: 1; }
.c-item-img {
    width: 60px; height: 60px; border-radius: 12px; object-fit: contain;
    background: #FFF8E1; padding: 5px; transition: transform 0.3s; cursor: help;
}
.c-item-img:hover { transform: scale(1.1); }
.c-item-info strong { color: #2C1810; display: block; font-size: 1rem; }
.c-item-info small { color: #7F8C8D; font-size: 0.75rem; }

.qty-ctrl {
    display: flex; align-items: center; gap: 10px;
    background: #FFF8E1; padding: 5px; border-radius: 50px; border: 1px solid #FFE0B2;
}
.qty-btn {
    width: 24px; height: 24px; border-radius: 50%; border: 1px solid #C0392B;
    background: transparent; color: #C0392B; cursor: pointer; font-weight: bold;
    display: flex; align-items: center; justify-content: center; transition: all 0.2s;
}
.qty-btn:hover { background: #C0392B; color: white; }
.qty-val { font-weight: bold; font-size: 0.9rem; width: 15px; text-align: center; }

.c-item-price { font-weight: bold; color: #C0392B; font-size: 1.1rem; margin-left: 15px; min-width: 60px; text-align: right; }

.c-item-remove {
    background: none; border: none; color: #E74C3C; font-size: 1.2rem;
    margin-left: 10px; cursor: pointer; opacity: 0; transition: all 0.3s; transform: scale(0.5);
}
.c-item:hover .c-item-remove { opacity: 1; transform: scale(1); }

/* Promo & Summary */
.promo-toggle { font-size: 0.9rem; color: #E67E22; cursor: pointer; margin: 15px 0; font-weight: 500; }
.promo-input-container { display: flex; gap: 10px; margin-bottom: 10px; }
.promo-input-container input {
    flex: 1; padding: 10px 15px; border-radius: 50px; border: 1px solid #E67E22; outline: none; font-family: 'Poppins';
}
.promo-input-container button {
    padding: 10px 20px; border-radius: 50px; background: #E67E22; color: white; border: none; cursor: pointer; font-weight: bold;
}
.promo-input-container.shake { animation: shakeError 0.4s; }
@keyframes shakeError { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-5px); } 75% { transform: translateX(5px); } }

.summary-row { display: flex; justify-content: space-between; margin-bottom: 8px; color: #7F8C8D; font-size: 0.95rem; }
.delivery-row { color: #E67E22; }
.discount-row { color: #27AE60; font-weight: bold; animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.total-row { font-size: 1.3rem; color: #2C1810; font-family: 'Playfair Display', serif; align-items: flex-end; }
.total-price-col { text-align: right; }
.total-price-col #cart-total-price { color: #C0392B; font-size: 1.6rem; display: block; }
.total-price-col small { font-size: 0.6rem; color: #7F8C8D; font-family: 'Poppins'; display: block; margin-top: -5px; }

/* Checkout Action Area */
.checkout-action-area { margin-top: 20px; }
.btn-checkout-smart {
    width: 100%; padding: 18px; border-radius: 50px; background: linear-gradient(135deg, #E67E22, #C0392B);
    color: white; border: none; font-size: 1.1rem; font-weight: bold; cursor: pointer;
    box-shadow: 0 8px 20px rgba(192,57,43,0.3); transition: all 0.3s;
    display: flex; justify-content: center; align-items: center; gap: 10px;
}
.btn-checkout-smart:hover { transform: scale(1.02); box-shadow: 0 12px 25px rgba(192,57,43,0.4); }
.btn-checkout-smart.logged-in { background: linear-gradient(135deg, #C0392B, #A93226); }

.split-choice-panel {
    background: #FFF8E1; border-radius: 20px; padding: 20px; margin-top: 15px;
    animation: slideDownPanel 0.4s ease forwards; text-align: center;
}
@keyframes slideDownPanel { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
.split-choice-panel p { margin-bottom: 15px; color: #2C1810; font-weight: 500; }
.btn-login-choice {
    width: 100%; padding: 14px; border-radius: 50px; background: #C0392B; color: white; border: none; font-weight: bold; cursor: pointer; margin-bottom: 15px;
}
.choice-divider { position: relative; margin: 10px 0 20px 0; text-align: center; }
.choice-divider::before { content: ''; position: absolute; left: 0; top: 50%; width: 100%; height: 1px; background: #E67E22; opacity: 0.3; }
.choice-divider span { background: #FFF8E1; padding: 0 10px; position: relative; z-index: 1; color: #E67E22; font-size: 0.8rem; }
.btn-guest-choice {
    width: 100%; padding: 14px; border-radius: 50px; background: transparent; color: #2C1810; border: 2px dashed #E67E22; font-weight: bold; cursor: pointer; margin-bottom: 10px;
}
.split-choice-panel small { color: #7F8C8D; font-size: 0.75rem; }

/* Login Back Panel */
.back-to-cart-btn {
    position: absolute; top: 20px; left: 20px; background: #FFF0E5; border: none; width: 40px; height: 40px; border-radius: 50%; color: #C0392B; cursor: pointer;
}
.login-inner h2 { font-family: 'Playfair Display', serif; color: #C0392B; margin-bottom: 30px; font-size: 2rem; }
.login-inner .input-group { margin-bottom: 20px; position: relative; }
.login-inner .input-group input { width: 100%; padding: 15px; border: 2px solid #FFE0B2; border-radius: 12px; outline: none; }
.login-inner .input-group label { position: absolute; left: 15px; top: 15px; color: #7F8C8D; transition: 0.3s; pointer-events: none; }
.login-inner .input-group input:focus + label, .login-inner .input-group input:not(:placeholder-shown) + label { top: -10px; left: 10px; background: #FFFDF8; padding: 0 5px; font-size: 0.8rem; color: #E67E22; }
.login-inner .forgot-link { text-align: right; margin-bottom: 20px; }
.login-inner .forgot-link a { color: #C0392B; text-decoration: none; font-size: 0.85rem; border-bottom: 1px solid #C0392B; }
.btn-submit-login { width: 100%; padding: 16px; border-radius: 50px; background: linear-gradient(135deg, #C0392B, #E74C3C); color: white; border: none; font-weight: bold; font-size: 1.1rem; cursor: pointer; }
.login-inner .new-here { text-align: center; margin-top: 20px; font-size: 0.9rem; }
.login-inner .new-here a { color: #C0392B; font-weight: bold; }

@media (max-width: 768px) {
    .cart-flip-container { margin: 0; max-width: 100%; transform: translateY(100%); margin-top: auto; }
    .cart-front, .cart-back { border-radius: 32px 32px 0 0; padding: 25px 20px; border-bottom: none; }
}
"""

with open('cart_enhanced.css', 'w') as f:
    f.write(css)

# 3. Generate cart.js replacement (completely rewriting cart logic)
new_cart_js = """
// ENHANCED CART & AUTH LOGIC
let cartItems = JSON.parse(localStorage.getItem('burger_cart')) || [];
let isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
let userName = localStorage.getItem('userEmail') ? localStorage.getItem('userEmail').split('@')[0] : '';

// Init
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
});

// --- CART UI MODAL ---
function openCartModal() {
    const backdrop = document.getElementById('cart-modal');
    backdrop.classList.remove('hidden');
    // Force reflow
    void backdrop.offsetWidth;
    backdrop.classList.add('show');
    renderEnhancedCart();
    
    // Reset states
    document.getElementById('split-choice-panel').classList.add('hidden');
    document.getElementById('btn-main-checkout').style.display = 'flex';
    document.getElementById('cart-flipper').classList.remove('flipped');
}

function closeCartModal() {
    const backdrop = document.getElementById('cart-modal');
    backdrop.classList.remove('show');
    setTimeout(() => {
        backdrop.classList.add('hidden');
    }, 400); // match transition
}

function handleBackdropClick(e) {
    if(e.target.id === 'cart-modal') {
        const container = document.getElementById('cart-flip-container');
        container.classList.add('shake-warning');
        setTimeout(() => container.classList.remove('shake-warning'), 400);
        
        // Next click outside will close it
        e.target.onclick = (ev) => {
            if(ev.target.id === 'cart-modal') closeCartModal();
            // reset handler
            setTimeout(() => { e.target.onclick = handleBackdropClick; }, 500);
        };
    }
}

// --- ADD TO CART OVERRIDE ---
window.addToCart = function(itemName, priceStr) {
    // Add item logic
    const price = parseInt(priceStr.replace(/[^0-9]/g, ''));
    const existing = cartItems.find(i => i.name === itemName);
    if(existing) {
        existing.qty += 1;
    } else {
        // default image mapping based on name
        let img = itemName.toLowerCase().replace(/ /g, '_') + '.png';
        if(!img.includes('burger')) img = 'burger.png';
        cartItems.push({ name: itemName, price: price, qty: 1, img: img });
    }
    
    localStorage.setItem('burger_cart', JSON.stringify(cartItems));
    updateCartBadge();
    
    // UI Effects
    const e = window.event;
    if (e && e.target && e.target.tagName === 'BUTTON') {
        const btn = e.target;
        const oldHtml = btn.innerHTML;
        btn.innerHTML = '✔ Added';
        btn.style.background = '#27AE60';
        setTimeout(() => {
            btn.innerHTML = oldHtml;
            btn.style.background = '';
        }, 1500);
    }
    
    // Navbar icon rotation
    const navIcon = document.querySelector('.fa-cart-shopping');
    if(navIcon) {
        navIcon.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1)';
        navIcon.style.transform = 'rotate(360deg) scale(1.2)';
        setTimeout(() => { navIcon.style.transform = 'none'; }, 500);
    }
}

function updateCartBadge() {
    const count = cartItems.reduce((acc, item) => acc + (item.qty||1), 0);
    const countEl = document.getElementById('cart-count');
    if(countEl) {
        countEl.innerText = count;
        countEl.style.display = count > 0 ? 'inline-block' : 'none';
        countEl.style.animation = 'none';
        void countEl.offsetWidth;
        countEl.style.animation = 'popIn 0.3s ease forwards';
    }
}

// --- RENDER CART ---
let discountApplied = 0;

function renderEnhancedCart() {
    const container = document.getElementById('cart-items-container');
    const summary = document.getElementById('cart-order-summary');
    const promo = document.getElementById('promo-section');
    const action = document.getElementById('checkout-action-area');
    
    container.innerHTML = '';
    
    if(cartItems.length === 0) {
        summary.style.display = 'none';
        promo.style.display = 'none';
        action.style.display = 'none';
        
        container.innerHTML = `
            <div class="empty-cart-state">
                <div class="floating-bg-emojis">
                    <div class="f-emoji" style="left:10%; animation-delay:0s">🍔</div>
                    <div class="f-emoji" style="left:80%; animation-delay:1.5s">🍟</div>
                    <div class="f-emoji" style="left:40%; animation-delay:2.5s">🥤</div>
                </div>
                <div class="empty-bowl">😢</div>
                <h3>Nothing here yet!</h3>
                <p class="typewriter-p" style="overflow:hidden; white-space:nowrap; margin:0 auto 20px auto; border-right:2px solid; width:0; animation: typing 2s steps(40, end) forwards, blink 0.75s step-end infinite;">Your burger is waiting for you 🍔</p>
                <button class="btn-explore" onclick="closeCartModal(); document.getElementById('menu')?.scrollIntoView({behavior:'smooth'})">EXPLORE MENU &rarr;</button>
            </div>
        `;
        return;
    }
    
    summary.style.display = 'block';
    promo.style.display = 'block';
    action.style.display = 'block';
    
    let subtotal = 0;
    
    cartItems.forEach((item, index) => {
        let q = item.qty || 1;
        subtotal += item.price * q;
        
        container.innerHTML += `
            <div class="c-item" id="c-item-${index}" style="animation-delay: ${index * 0.1}s">
                <div class="c-item-left">
                    <img src="${item.img || 'burger.png'}" class="c-item-img" title="Tap to customize ✏️" onerror="this.src='burger.png'">
                    <div class="c-item-info">
                        <strong>${item.name}</strong>
                        <div class="qty-ctrl">
                            <button class="qty-btn" onclick="updateQty(${index}, -1)">−</button>
                            <span class="qty-val" id="qty-val-${index}">${q}</span>
                            <button class="qty-btn" onclick="updateQty(${index}, 1)">+</button>
                        </div>
                    </div>
                </div>
                <div class="c-item-price">₹${item.price * q}</div>
                <button class="c-item-remove" onclick="removeItem(${index})"><i class="fa-solid fa-trash"></i></button>
            </div>
        `;
    });
    
    // Update Totals
    document.getElementById('cart-subtotal').innerText = '₹' + subtotal;
    
    let delivery = subtotal >= 499 ? 0 : 40;
    document.getElementById('cart-delivery').innerText = delivery === 0 ? 'FREE' : '₹' + delivery;
    
    let total = subtotal + delivery - discountApplied;
    
    // Animate total change
    const totEl = document.getElementById('cart-total-price');
    animateValue(totEl, parseInt(totEl.innerText.replace('₹','')) || 0, total, 400);
    
    // Checkout button state
    const btnText = document.getElementById('checkout-btn-text');
    const btnLock = document.getElementById('checkout-lock-icon');
    const mainBtn = document.getElementById('btn-main-checkout');
    
    if(isLoggedIn) {
        btnText.innerText = `Checkout as ${userName} →`;
        btnLock.className = 'fa-solid fa-arrow-right';
        mainBtn.classList.add('logged-in');
    } else {
        btnText.innerText = 'PROCEED TO CHECKOUT';
        btnLock.className = 'fa-solid fa-lock lock-icon';
        mainBtn.classList.remove('logged-in');
    }
}

function updateQty(index, delta) {
    let q = (cartItems[index].qty || 1) + delta;
    if(q <= 0) {
        const itemCard = document.getElementById(`c-item-${index}`);
        itemCard.style.transform = 'translateX(-100px)';
        itemCard.style.opacity = '0';
        setTimeout(() => { removeItem(index); }, 300);
    } else {
        cartItems[index].qty = q;
        const valEl = document.getElementById(`qty-val-${index}`);
        valEl.innerText = q;
        valEl.style.animation = 'none';
        void valEl.offsetWidth;
        valEl.style.animation = delta > 0 ? 'bounceInUp 0.3s' : 'bounceInDown 0.3s';
        
        localStorage.setItem('burger_cart', JSON.stringify(cartItems));
        updateCartBadge();
        renderEnhancedCart();
    }
}

function removeItem(index) {
    cartItems.splice(index, 1);
    localStorage.setItem('burger_cart', JSON.stringify(cartItems));
    updateCartBadge();
    renderEnhancedCart();
    // Toast
    const toast = document.createElement('div');
    toast.style = "position:fixed; bottom:20px; right:20px; background:#333; color:white; padding:10px 20px; border-radius:5px; z-index:10000; display:flex; gap:10px; align-items:center;";
    toast.innerHTML = `<span>Removed!</span> <button style="color:#E67E22; background:none; border:none; cursor:pointer; font-weight:bold" onclick="undoRemove()">UNDO</button>`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// --- PROMO CODE ---
function togglePromo() {
    const p = document.getElementById('promo-container');
    p.classList.toggle('hidden');
    if(!p.classList.contains('hidden')) {
        p.style.animation = 'slideDownPanel 0.3s forwards';
    }
}

function applyPromo() {
    const val = document.getElementById('promo-input').value.toUpperCase();
    const cont = document.getElementById('promo-container');
    const msg = document.getElementById('promo-msg');
    
    if(val === 'BURGER50') {
        discountApplied = 50;
        cont.style.display = 'none';
        msg.innerHTML = '<span style="color:#27AE60; font-weight:bold; animation:popIn 0.5s">WOOHOO! ₹50 OFF! 🎉</span>';
        document.getElementById('discount-row').classList.remove('hidden');
        document.getElementById('cart-discount').innerText = '-₹50';
        renderEnhancedCart(); // recalculates total
        // Confetti
        try { fireConfetti(); } catch(e){}
    } else {
        cont.classList.add('shake');
        document.getElementById('promo-input').style.borderColor = '#C0392B';
        setTimeout(() => cont.classList.remove('shake'), 400);
        msg.innerHTML = '<span style="color:#C0392B; font-size:0.8rem">Hmm, that didn\'t work 🤔</span>';
    }
}

// --- CHECKOUT LOGIC ---
function handleCheckoutClick() {
    if(isLoggedIn) {
        proceedToCheckout(false);
    } else {
        // Expand split choice panel
        document.getElementById('btn-main-checkout').style.display = 'none';
        document.getElementById('split-choice-panel').classList.remove('hidden');
    }
}

function flipToLogin() {
    document.getElementById('cart-flipper').classList.add('flipped');
}

function flipToCart() {
    document.getElementById('cart-flipper').classList.remove('flipped');
}

function proceedToCheckout(isGuest) {
    const btn = document.getElementById('btn-main-checkout');
    btn.style.display = 'flex';
    document.getElementById('split-choice-panel').classList.add('hidden');
    
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Preparing checkout...';
    btn.style.pointerEvents = 'none';
    
    setTimeout(() => {
        // Slide away modal
        document.getElementById('cart-flip-container').style.transform = 'translateY(100%)';
        setTimeout(() => {
            window.location.href = 'checkout.html';
        }, 400);
    }, 800);
}

// --- LOGIN SUBMIT ---
function handleCartLogin(e) {
    e.preventDefault();
    const email = document.getElementById('cart-email').value;
    const pwd = document.getElementById('cart-password').value;
    const form = document.getElementById('cart-login-form');
    
    if(pwd === '') {
        form.style.animation = 'shakeError 0.4s';
        setTimeout(() => form.style.animation = '', 400);
        return;
    }
    
    // Success
    const submitBtn = document.querySelector('.btn-submit-login');
    submitBtn.innerHTML = '<i class="fa-solid fa-check"></i>';
    submitBtn.style.background = '#27AE60';
    
    setTimeout(() => {
        isLoggedIn = true;
        userName = email.split('@')[0];
        localStorage.setItem('isLoggedIn', 'true');
        localStorage.setItem('userEmail', email);
        
        flipToCart();
        renderEnhancedCart();
        
        // Hide split panel and show main checkout button again
        document.getElementById('split-choice-panel').classList.add('hidden');
        document.getElementById('btn-main-checkout').style.display = 'flex';
        
        try { fireConfetti(); } catch(e){}
    }, 800);
}

function toggleCartPwd() {
    const pwd = document.getElementById('cart-password');
    const icon = document.querySelector('.cart-back .toggle-pwd');
    if (pwd.type === 'password') { pwd.type = 'text'; icon.classList.remove('fa-eye'); icon.classList.add('fa-eye-slash'); }
    else { pwd.type = 'password'; icon.classList.remove('fa-eye-slash'); icon.classList.add('fa-eye'); }
}

// Helpers
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = '₹' + Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        } else {
            obj.style.animation = 'popIn 0.3s ease';
            setTimeout(()=>obj.style.animation='none', 300);
        }
    };
    window.requestAnimationFrame(step);
}

// Keyframes styles injected via JS for missing ones
const styleSheet = document.createElement("style");
styleSheet.innerText = `
    @keyframes typing { from { width: 0 } to { width: 100% } }
    @keyframes blink { 50% { border-color: transparent } }
    @keyframes popIn { 0% { transform: scale(0.8); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
    @keyframes bounceInUp { from { transform: translateY(10px); opacity:0; } to { transform: translateY(0); opacity:1; } }
    @keyframes bounceInDown { from { transform: translateY(-10px); opacity:0; } to { transform: translateY(0); opacity:1; } }
    @keyframes gentleBounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
`;
document.head.appendChild(styleSheet);
"""

with open('cart.js', 'w') as f:
    f.write(new_cart_js)

print("Cart upgrade successful.")
