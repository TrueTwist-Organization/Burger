<?php declare(strict_types=1); require_once __DIR__ . '/includes/config.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPICY CHICKEN BURGER - The Perfect Burger</title>
    <link rel="stylesheet" href="style.css?v=1348">
    <link href="https://fonts.googleapis.com/css2?family=Bangers&family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="cart_enhanced.css">
</head>
<body style="background-color: #FFF8E1;">

    <!-- Header -->
    <header style="background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: relative;">
        <a href="index.php" class="logo">
            <span class="icon">🍔</span> BURGER
        </a>
        <nav style="position: relative; display: flex; gap: 20px;">
            <a href="index.php#home" class="nav-link">Home</a>
            <a href="index.php#menu" class="nav-link active">Menu</a>
            <a href="index.php#story" class="nav-link">About</a>
            <a href="index.php#contact" class="nav-link">Contact Us</a>
            <div class="nav-indicator"></div>
        </nav>
        <div class="icons">
            <span onclick="openSearchModal()" style="cursor:pointer;">🔍</span>
            <span class="cart-icon" onclick="openCartModal()" style="position:relative; cursor:pointer;">🛒 <span id="cart-count" style="position:absolute; top:-10px; right:-10px; background:#E85A1F; color:white; border-radius:50%; padding:2px 6px; font-size:12px; display:none;">0</span></span>
            <span class="user-icon" onclick="openLoginModal()" style="cursor:pointer; transition: color 0.3s;">👤</span>
            <span class="menu-toggle" onclick="document.querySelector('nav').classList.toggle('active')"><i class="fa-solid fa-bars"></i></span>
        </div>
    </header>

    <!-- Product Detail -->
    <div class="product-detail-container" class="product-detail-container" style="max-width: 1200px; margin: 50px auto; padding: 20px; display: flex; flex-wrap: wrap; gap: 50px; align-items: center; min-height: 70vh;">
        <div class="product-img-col" class="product-img-col" style="flex: 1; min-width: 300px; text-align: center; position: relative;" id="burger-img-container">
            <img src="spicy_chicken_burger.png" alt="SPICY CHICKEN BURGER" class="main-burger-img" style="width: 100%; max-width: 500px; filter: drop-shadow(0px 20px 30px rgba(0,0,0,0.3)); position: relative; z-index: 2;">
            <img src="avocado_chef_transparent.png" id="naughty-chef" alt="Chef" style="position: absolute; width: 500px; right: -150px; bottom: -50px; z-index: 3; opacity: 0; pointer-events: none; filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.3));">
            <div id="chef-speech" style="position: absolute; right: 10px; top: 40px; z-index: 4; pointer-events: none; opacity: 0; display: flex; flex-direction: column; align-items: center; gap: 10px;">
    <div style="font-family: 'Bangers', cursive; font-size: 6rem; color: #FFEB3B; line-height: 1; transform: rotate(-10deg); text-shadow: 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 3px 0 #000, 0 -3px 0 #000, 8px 8px 0px #0288D1, 10px 10px 0px #000;">WOW!</div>
    <div style="font-family: 'Bangers', cursive; font-size: 4.5rem; color: #FFFFFF; line-height: 1; transform: rotate(5deg) translateX(40px); text-shadow: 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 3px 0 #000, 0 -3px 0 #000, 6px 6px 0px #000;">YUMMY!</div>
</div>
            
        </div>
        <div class="product-text-col" style="flex: 1; min-width: 300px;">
            <h1 style="font-family: 'Bangers', cursive; font-size: 4rem; color: #FF5722; margin-top: 0;">SPICY CHICKEN BURGER</h1>
            <p style="font-size: 2rem; color: #D32F2F; font-weight: 900; margin: 20px 0;">₹240</p>
            <p style="font-size: 1.2rem; color: #5D4037; line-height: 1.6; margin-bottom: 40px;">
                Experience the ultimate taste of our SPICY CHICKEN BURGER. Made with the freshest ingredients, premium meat, and our signature sauces, it's guaranteed to satisfy your cravings.
            </p>
            <button class="btn-explore" style="border: none; cursor: pointer;" onclick="addToCart('SPICY CHICKEN BURGER', '₹240')">ADD TO CART 🛒</button>
        </div>
    </div>

    
    <!-- Cart Modal -->
    
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

    <!-- Login Modal -->
    <div id="login-modal" class="modal-overlay">
        <div class="modal-content">
            <span class="close-btn" onclick="closeLoginModal()">&times;</span>
            <h2 id="modal-title">Welcome Back!</h2>
            <p id="modal-subtitle">Log in to your account</p>
            <form id="login-form" onsubmit="handleLogin(event)">
                <input type="email" id="email-input" placeholder="Email Address" required>
                <input type="password" id="password-input" placeholder="Password" required>
                <button type="submit" class="btn-primary" style="width:100%; margin-top:20px;">LOGIN</button>
            </form>
            <p style="margin-top:20px; font-size:0.9rem;">
                <span id="toggle-text">Don't have an account?</span> 
                <a href="#" onclick="toggleAuthMode(); return false;" id="toggle-link" style="color:#E85A1F; font-weight:bold;">Sign Up</a>
            </p>
        </div>
    </div>


    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <a href="index.php" class="footer-logo">🍔 BURGER</a>
            <p>Crafted with flavor, served with love.</p>
            <div class="socials" style="display: flex; justify-content: center; gap: 20px;">
                <a href="https://facebook.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-facebook-f"></i></a>
                <a href="https://instagram.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-instagram"></i></a>
                <a href="https://twitter.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-twitter"></i></a>
            </div>
                        <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="index.php#story" style="color: #bbb; text-decoration: none; margin: 0 10px;">About Us</a> | 
                <a href="index.php#contact" style="color: #bbb; text-decoration: none; margin: 0 10px;">Contact Us</a> | 
                <a href="disclaimer.php" style="color: #bbb; text-decoration: none; margin: 0 10px;">Disclaimer</a> | 
                <a href="privacy_policy.php" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="terms_of_service.php" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms & Conditions</a>
            </div>
        </div>
                <div class="footer-bottom">
            <div>&copy; 2026 The Perfect Burger. All rights reserved.</div>
            <div class="footer-credits" style="margin-top: 10px; font-size: 0.8rem; opacity: 0.7; letter-spacing: 0.5px;">
                design by <a href="https://truetwist.in" target="_blank" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.2);">truetwist.in</a> | 
                marketing by <a href="https://369network.com/" target="_blank" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.2);">369network.com</a>
            </div>
        </div>
    </footer>



    <script src="cart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof gsap === 'undefined') return;
            
            if (window.innerWidth < 768) {
                gsap.set("#naughty-chef", { width: 300, right: -100, bottom: -20 });
                gsap.set("#chef-speech", { scale: 0.5, transformOrigin: "bottom right", right: -20, top: 0 });
            }
            const tl = gsap.timeline();
            
            // 1. Burger bounces in from top-left
            tl.from(".main-burger-img", {
                x: window.innerWidth < 768 ? 0 : -800,
                y: window.innerWidth < 768 ? -400 : -400,
                rotation: -360,
                duration: 2,
                ease: "bounce.out"
            })
            // 2. Naughty chef slides in
            .to("#naughty-chef", {
                opacity: 1,
                x: window.innerWidth < 768 ? -180 : -350,
                rotation: -5,
                duration: 0.8,
                ease: "power2.out"
            }, "+=0.5")
            .to("#naughty-chef", {
                scale: 1.1,
                duration: 0.3,
                yoyo: true,
                repeat: 1
            })

            // 4. Chef speaks "Wow yummy"
            .to("#chef-speech", {
                opacity: 1,
                y: -20,
                duration: 0.4,
                ease: "back.out(2)"
            })
            // 5. Chef stays for a bit, then leaves
            .to(["#naughty-chef", "#chef-speech"], {
                opacity: 0,
                x: window.innerWidth < 768 ? 200 : 400,
                duration: 1.5,
                ease: "power2.in"
            }, "+=2");
        });
    </script>

    <!-- Search Modal -->
    <div id="search-modal" class="modal-overlay hidden"
        onclick="if(event.target.id==='search-modal') closeSearchModal()" style="z-index: 10000;">
        <div class="search-container"
            style="background: white; padding: 30px; border-radius: 12px; width: 400px; max-width: 90%; text-align: center; position: absolute; top: 20%; left: 50%; transform: translate(-50%, 0); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <h2 style="color: #FF5722; font-family: 'Bangers', cursive; font-size: 2rem; margin-bottom: 20px;">Search Menu</h2>
            <div style="display: flex; gap: 10px;">
                <input type="text" id="search-input" placeholder="Type a burger name..." onkeypress="if(event.key === 'Enter') performSearch()"
                    style="flex: 1; padding: 10px 15px; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; outline: none;">
                <button onclick="performSearch()"
                    style="background: #FF5722; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer;">Search</button>
            </div>
            <button class="close-btn" onclick="closeSearchModal()"
                style="position: absolute; top: 10px; right: 15px; background: none; border: none; font-size: 1.5rem; color: #888; cursor: pointer;">&times;</button>
        </div>
    </div>

    <script>
        function openSearchModal() {
            const modal = document.getElementById('search-modal');
            modal.classList.remove('hidden');
            modal.style.display = 'flex';
            setTimeout(() => document.getElementById('search-input').focus(), 100);
        }
        function closeSearchModal() {
            document.getElementById('search-modal').classList.add('hidden');
            document.getElementById('search-modal').style.display = 'none';
        }
        function performSearch() {
            const val = document.getElementById('search-input').value.toLowerCase().trim();
            closeSearchModal();
            
            // Check if we are on the homepage
            if (document.getElementById('menu') && document.querySelectorAll('.u-card').length > 0) {
                document.getElementById('menu').scrollIntoView({ behavior: 'smooth' });
                
                const cards = document.querySelectorAll('.u-card');
                let found = false;
                
                cards.forEach(card => {
                    const titleEl = card.querySelector('.u-card-title');
                    if (titleEl) {
                        const title = titleEl.innerText.toLowerCase();
                        if (val === '' || title.includes(val)) {
                            card.style.display = 'flex';
                            found = true;
                        } else {
                            card.style.display = 'none';
                        }
                    }
                });
                
                if(!found) {
                    if (typeof showToast === 'function') {
                        showToast("No burgers found matching your search!");
                    } else {
                        alert("No burgers found matching your search!");
                    }
                }
            } else {
                // Redirect to index.php with search query
                window.location.href = 'index.php?search=' + encodeURIComponent(val) + '#menu';
            }
        }
        
        // Auto-search on page load if ?search= is present
        window.addEventListener('DOMContentLoaded', () => {
            const urlParams = new URLSearchParams(window.location.search);
            const searchParam = urlParams.get('search');
            if (searchParam && document.getElementById('menu') && document.querySelectorAll('.u-card').length > 0) {
                setTimeout(() => {
                    document.getElementById('search-input').value = searchParam;
                    performSearch();
                }, 500);
            }
        });
    </script>

</body>

</html>
