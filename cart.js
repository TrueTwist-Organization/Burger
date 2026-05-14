
// ENHANCED CART & AUTH LOGIC
let cartItems = [];
try {
    cartItems = JSON.parse(localStorage.getItem('burger_cart')) || [];
} catch(e) {
    cartItems = [];
}

const fallbackPrices = {
    'classic cheese burger': 200,
    'veggie burger': 180,
    'veggie bean burger': 220,
    'avocado smash burger': 220,
    'mushroom swiss burger': 280,
    'spicy chicken burger': 240,
    'bbq bacon burger': 260,
    'truffle mayo burger': 300,
    'hawaiian pineapple': 260,
    'hawaiian pineapple burger': 250,
    'classic smash burger': 210,
    'ultimate monster': 350,
    'chicken grilled burger': 280,
    'texas smokehouse': 290,
    'crispy fish burger': 230,
    'double beef burger': 300,
    'buffalo chicken': 250
};

// Clean up and normalize cart items
function normalizeCart() {
    cartItems = cartItems.filter(item => item && item.name);
    cartItems.forEach(item => {
        if (typeof item.price === 'string') {
            item.price = parseInt(item.price.replace(/[^0-9]/g, '')) || 0;
        }
        if (isNaN(item.price) || item.price === null || item.price === 0 || item.price === undefined) {
            const key = item.name.toLowerCase().trim();
            item.price = fallbackPrices[key] || 200;
        }
        if (!item.qty) item.qty = 1;
    });
    localStorage.setItem('burger_cart', JSON.stringify(cartItems));
}
normalizeCart();

let isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
let userName = localStorage.getItem('userEmail') ? localStorage.getItem('userEmail').split('@')[0] : '';

// Init
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
});

// --- CART UI MODAL ---
function openCartModal() {
    const backdrop = document.getElementById('cart-modal');
    if (!backdrop) return;

    backdrop.classList.remove('hidden');
    // Force reflow
    void backdrop.offsetWidth;
    backdrop.classList.add('show');
    backdrop.classList.add('active');
    
    // Refresh data before rendering
    try {
        cartItems = JSON.parse(localStorage.getItem('burger_cart')) || [];
    } catch(e) {}
    
    renderEnhancedCart();
    
    // Reset states
    const splitPanel = document.getElementById('split-choice-panel');
    const mainCheckoutBtn = document.getElementById('btn-main-checkout');
    const flipper = document.getElementById('cart-flipper');
    
    if (splitPanel) splitPanel.classList.add('hidden');
    if (mainCheckoutBtn) mainCheckoutBtn.style.display = 'flex';
    if (flipper) flipper.classList.remove('flipped');
}

function closeCartModal() {
    const backdrop = document.getElementById('cart-modal');
    if (!backdrop) return;
    backdrop.classList.remove('show');
    backdrop.classList.remove('active');
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
window.addToCart = function(itemName, priceStr, thirdArg) {
    // Refresh cartItems from localStorage to ensure sync
    cartItems = JSON.parse(localStorage.getItem('burger_cart')) || [];
    cartItems = cartItems.filter(item => item && !isNaN(item.price) && item.price !== null);

    // Handle (event/btn, name, price) vs (name, price)
    let eventObj = null;
    if (typeof itemName === 'object' && itemName) {
        // If it's an event or a DOM element
        if (itemName.target || itemName.type || itemName.tagName) {
            eventObj = itemName;
            itemName = priceStr;
            priceStr = thirdArg;
        }
    }

    if (!itemName) {
        console.error("addToCart: No item name provided");
        return;
    }

    // Add item logic
    let price = parseInt(String(priceStr).replace(/[^0-9]/g, '')) || 0;
    
    // Fallback if price is 0 or NaN
    if (!price || isNaN(price)) {
        const key = itemName.toLowerCase().trim();
        price = fallbackPrices[key] || 200;
    }

    const existing = cartItems.find(i => i.name.toLowerCase().trim() === itemName.toLowerCase().trim());
    
    if(existing) {
        existing.qty = (existing.qty || 1) + 1;
    } else {
        // default image mapping based on name
        let img = itemName.toLowerCase().trim().replace(/ /g, '_') + '.png';
        // Fallback for names that don't match image files exactly
        if (itemName.toLowerCase().includes('monster')) img = 'ultimate_monster_burger.png';
        if (itemName.toLowerCase().includes('veggie')) img = 'veggie_burger.png';
        if (itemName.toLowerCase().includes('cheese')) img = 'classic_cheese_burger.png';
        
        cartItems.push({ 
            name: itemName.trim(), 
            price: price, 
            qty: 1, 
            img: img 
        });
    }
    
    localStorage.setItem('burger_cart', JSON.stringify(cartItems));
    updateCartBadge();
    
    // --- FLYING BURGER ANIMATION ---
    const btn = (eventObj && eventObj.currentTarget) || (window.event && window.event.target);
    const cartIcon = document.querySelector('.cart-icon') || document.querySelector('.fa-cart-shopping');
    
    // Find the burger image to fly
    let burgerImg = null;
    if (btn) {
        // Try to find image in the same card
        const card = btn.closest('.u-card') || btn.closest('.menu-card') || btn.closest('.product-detail-container');
        if (card) {
            burgerImg = card.querySelector('.u-burger-img') || card.querySelector('.main-burger-img') || card.querySelector('img');
        }
    }

    if (burgerImg && cartIcon) {
        const startRect = burgerImg.getBoundingClientRect();
        const endRect = cartIcon.getBoundingClientRect();
        
        const flying = document.createElement('img');
        flying.src = burgerImg.src;
        flying.className = 'flying-burger';
        flying.style.position = 'fixed';
        flying.style.zIndex = '10000';
        flying.style.left = startRect.left + 'px';
        flying.style.top = startRect.top + 'px';
        flying.style.width = startRect.width + 'px';
        flying.style.transition = 'all 0.8s cubic-bezier(0.25, 1, 0.5, 1)';
        document.body.appendChild(flying);
        
        setTimeout(() => {
            flying.style.left = (endRect.left + 10) + 'px';
            flying.style.top = (endRect.top + 10) + 'px';
            flying.style.width = '20px';
            flying.style.opacity = '0.5';
            flying.style.transform = 'rotate(360deg)';
        }, 50);
        
        setTimeout(() => {
            flying.remove();
            // Cart icon bounce
            cartIcon.style.transform = 'scale(1.5)';
            setTimeout(() => cartIcon.style.transform = 'scale(1)', 200);
            
            // Open Cart Modal after animation
            if (typeof openCartModal === 'function') {
                openCartModal();
            }
        }, 850);
    } else {
        // Fallback: Open cart immediately if no animation
        if (typeof openCartModal === 'function') {
            openCartModal();
        }
    }

    // UI Effects on button
    if (btn && btn.tagName === 'BUTTON') {
        const oldHtml = btn.innerHTML;
        btn.innerHTML = '✔ Added';
        btn.style.background = '#27AE60';
        setTimeout(() => {
            btn.innerHTML = oldHtml;
            btn.style.background = '';
        }, 1500);
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
    // Refresh cartItems from localStorage to ensure sync
    try {
        const stored = localStorage.getItem('burger_cart');
        cartItems = stored ? JSON.parse(stored) : [];
    } catch(e) {
        cartItems = [];
    }
    
    // Filter out invalid items
    cartItems = cartItems.filter(item => item && item.name);

    const container = document.getElementById('cart-items-container');
    const summary = document.getElementById('cart-order-summary');
    const promo = document.getElementById('promo-section');
    const action = document.getElementById('checkout-action-area');
    
    if (!container) return;
    
    if(cartItems.length === 0) {
        if (summary) summary.style.display = 'none';
        if (promo) promo.style.display = 'none';
        if (action) action.style.display = 'none';
        
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
    
    if (summary) summary.style.display = 'block';
    if (promo) promo.style.display = 'block';
    if (action) action.style.display = 'block';
    
    let subtotal = 0;
    let html = '';
    
    cartItems.forEach((item, index) => {
        let q = parseInt(item.qty) || 1;
        let price = parseInt(item.price) || 0;
        if (!price || isNaN(price)) {
            const key = item.name ? item.name.toLowerCase().trim() : '';
            price = fallbackPrices[key] || 200;
        }
        subtotal += price * q;
        
        html += `
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
                <div class="c-item-price">₹${price * q}</div>
                <button class="c-item-remove" onclick="removeItem(${index})"><i class="fa-solid fa-trash"></i></button>
            </div>
        `;
    });
    
    container.innerHTML = html;
    
    // Update Totals
    const subtotalEl = document.getElementById('cart-subtotal');
    if (subtotalEl) subtotalEl.innerText = '₹' + subtotal;
    
    let delivery = subtotal >= 499 ? 0 : 40;
    const deliveryEl = document.getElementById('cart-delivery');
    if (deliveryEl) deliveryEl.innerText = delivery === 0 ? 'FREE' : '₹' + delivery;
    
    let total = subtotal + delivery - discountApplied;
    
    // Animate total change
    const totEl = document.getElementById('cart-total-price');
    if (totEl) {
        animateValue(totEl, parseInt(totEl.innerText.replace('₹','')) || 0, total, 400);
    }
    
    // Checkout button state
    const btnText = document.getElementById('checkout-btn-text');
    const btnLock = document.getElementById('checkout-lock-icon');
    const mainBtn = document.getElementById('btn-main-checkout');
    
    if (btnText && btnLock && mainBtn) {
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
        msg.innerHTML = `<span style="color:#C0392B; font-size:0.8rem">Hmm, that didn't work 🤔</span>`;
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
            window.location.href = 'checkout.html' + (isGuest ? '?guest=true' : '');
        }, 400);
    }, 800);
}

// --- LOGIN SUBMIT ---
function handleCartLogin(e) {
    e.preventDefault();
    const email = document.getElementById('cart-email').value;
    const pwd = document.getElementById('cart-password').value;
    const form = document.getElementById('cart-login-form');
    
    if(email.trim() === '' || pwd.trim() === '') {
        form.style.animation = 'shakeError 0.4s';
        setTimeout(() => form.style.animation = '', 400);
        
        // Show a brief message or alert
        if(typeof showToast === 'function') showToast("Please fill all fields!");
        else alert("Please fill all fields!");
        
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

// Polyfills for old login handlers to use the new Cart Flip Login
window.openLoginModal = function() {
    openCartModal();
    setTimeout(flipToLogin, 50);
};

window.closeLoginModal = function() {
    closeCartModal();
};

window.toggleAuthMode = function() {
    console.log("Auth mode toggle not needed in new design");
};

window.handleLogin = function(e) {
    e.preventDefault();
    const form = e.target;
    let email = '', pwd = '';
    
    // Try to get values from standard login modal if it exists
    const emailInput = document.getElementById('email-input');
    const pwdInput = document.getElementById('password-input');
    
    if (emailInput && pwdInput) {
        email = emailInput.value.trim();
        pwd = pwdInput.value.trim();
    } else {
        // Fallback to cart login
        if(typeof handleCartLogin === 'function') return handleCartLogin(e);
    }
    
    if (email === '' || pwd === '') {
        alert("Please fill all fields!");
        return;
    }
    
    // Success simulation
    const btn = form.querySelector('button[type="submit"]');
    if(btn) {
        btn.innerHTML = '<i class="fa-solid fa-check"></i>';
        btn.style.background = '#27AE60';
    }
    
    setTimeout(() => {
        isLoggedIn = true;
        userName = email.split('@')[0];
        localStorage.setItem('isLoggedIn', 'true');
        localStorage.setItem('userEmail', email);
        
        if (typeof closeLoginModal === 'function') closeLoginModal();
        if (typeof renderEnhancedCart === 'function') renderEnhancedCart();
        
        // Show success
        if (typeof showToast === 'function') showToast("Logged in successfully! 🎉");
        else alert("Logged in successfully!");
    }, 800);
};

// --- DIET INDICATOR INJECTION ---
document.addEventListener('DOMContentLoaded', () => {
    const vegBurgers = ['veggie', 'avocado smash', 'mushroom swiss', 'classic cheese', 'truffle mayo', 'hawaiian pineapple', 'classic smash'];
    
    // Icon styles for Cards (Absolute Top-Left)
    const getCardIcon = (isVeg) => {
        const color = isVeg ? '#28a745' : '#8b0000';
        const innerShape = isVeg 
            ? `<span style="width:10px; height:10px; border-radius:50%; background-color:${color};"></span>`
            : `<span style="width:0; height:0; border-left:5px solid transparent; border-right:5px solid transparent; border-bottom:10px solid ${color}; margin-top:-2px;"></span>`;
            
        return `<span class="diet-indicator" style="position:absolute; top:20px; left:20px; display:inline-flex; align-items:center; justify-content:center; width:20px; height:20px; border:2px solid ${color}; border-radius:4px; background: white; z-index: 10; box-shadow: 0 2px 5px rgba(0,0,0,0.1);" title="${isVeg ? 'Veg' : 'Non-Veg'}">${innerShape}</span>`;
    };

    // Icon styles for Product H1 (Inline)
    const getInlineIcon = (isVeg) => {
        const color = isVeg ? '#28a745' : '#8b0000';
        const innerShape = isVeg 
            ? `<span style="width:12px; height:12px; border-radius:50%; background-color:${color};"></span>`
            : `<span style="width:0; height:0; border-left:6px solid transparent; border-right:6px solid transparent; border-bottom:12px solid ${color}; margin-top:-2px;"></span>`;
            
        return `<span class="diet-indicator" style="display:inline-flex; align-items:center; justify-content:center; width:24px; height:24px; border:2px solid ${color}; border-radius:4px; margin-left:15px; vertical-align:middle; background: white; flex-shrink: 0;" title="${isVeg ? 'Veg' : 'Non-Veg'}">${innerShape}</span>`;
    };

    // 1. Add to Universe Cards on Home Page (Corner)
    document.querySelectorAll('.u-card').forEach(card => {
        if(card.querySelector('.diet-indicator')) return; // Already added
        const titleEl = card.querySelector('.u-card-title');
        if(!titleEl) return;
        const title = titleEl.innerText.trim().toLowerCase();
        const isVeg = vegBurgers.some(v => title.includes(v));
        card.insertAdjacentHTML('afterbegin', getCardIcon(isVeg));
        
        // Remove it from title if it was previously added there by old cache
        const oldIcon = titleEl.querySelector('.diet-indicator');
        if (oldIcon) oldIcon.remove();
    });

    // 2. Add to Product Detail Pages (h1)
    document.querySelectorAll('h1').forEach(h1 => {
        if(h1.querySelector('.diet-indicator')) return;
        const title = h1.innerText.trim().toLowerCase();
        if(title.includes('burger') || title.includes('monster') || title.includes('swiss')) {
            const isVeg = vegBurgers.some(v => title.includes(v));
            h1.insertAdjacentHTML('beforeend', getInlineIcon(isVeg));
        }
    });
});
