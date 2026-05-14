import re
import os

with open("index.html", "r") as f:
    html = f.read()

# 1. Update prices $ -> ₹ and add 0
html = re.sub(r'\$(\d+)', r'₹\g<1>0', html)

# 2. Add Footer if not present
footer = """
    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <a href="index.html" class="footer-logo">🍔 BURGER</a>
            <p>Crafted with flavor, served with love.</p>
            <div class="socials" style="display: flex; justify-content: center; gap: 20px;">
                <a href="#" onclick="showToast('Redirecting to Facebook...'); return false;" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-facebook-f"></i></a>
                <a href="#" onclick="showToast('Redirecting to Instagram...'); return false;" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-instagram"></i></a>
                <a href="#" onclick="showToast('Redirecting to Twitter...'); return false;" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-twitter"></i></a>
            </div>
            <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="#" onclick="showToast('Privacy Policy coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="#" onclick="showToast('Terms of Service coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
                <a href="#" onclick="showToast('Cookie Policy coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Cookie Policy</a> | 
                <a href="#" onclick="showToast('Refund Policy coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Refund Policy</a>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 The Perfect Burger. All rights reserved.
        </div>
    </footer>
"""
if "<footer>" not in html:
    html = html.replace("<script src=\"script.js\"></script>", footer + "\n    <script src=\"script.js\"></script>")

# 3. Extract burger data directly using image tags as anchors
burger_blocks = re.findall(r'<img src="([^"]+)" class="menu-burger-img" alt="([^"]+)">.*?<h3>(.*?)</h3>.*?₹(\d+)', html, re.DOTALL)

burgers = []
for img_src, alt_text, title, price_val in burger_blocks:
    price = '₹' + price_val
    page_name = img_src.split('/')[-1].replace('.png', '.html')
    burgers.append({"img": img_src, "title": title, "price": price, "page": page_name})
    
    # Update link if necessary
    if f'href="{page_name}"' not in html:
        pass

with open("index.html", "w") as f:
    f.write(html)

# 4. Generate the 15 pages
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The Perfect Burger</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Bangers&family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background-color: #FFF8E1;">

    <!-- Header -->
    <header style="background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: relative;">
        <a href="index.html" class="logo">
            <span class="icon">🍔</span> BURGER
        </a>
        <nav style="position: relative; display: flex; gap: 20px;">
            <a href="index.html#home" class="nav-link">Home</a>
            <a href="index.html#menu" class="nav-link active">Menu</a>
            <a href="index.html#about" class="nav-link">About</a>
            <a href="index.html#contact" class="nav-link">Contact Us</a>
            <div class="nav-indicator"></div>
        </nav>
        <div class="icons">
            <span onclick="showToast('Search feature coming soon!')" style="cursor:pointer;">🔍</span>
            <span class="cart-icon" onclick="openCartModal()" style="position:relative; cursor:pointer;">🛒 <span id="cart-count" style="position:absolute; top:-10px; right:-10px; background:#E85A1F; color:white; border-radius:50%; padding:2px 6px; font-size:12px; display:none;">0</span></span>
            <span class="user-icon" onclick="openLoginModal()" style="cursor:pointer; transition: color 0.3s;">👤</span>
        </div>
    </header>

    <!-- Product Detail -->
    <div style="max-width: 1200px; margin: 50px auto; padding: 20px; display: flex; flex-wrap: wrap; gap: 50px; align-items: center; min-height: 70vh;">
        <div style="flex: 1; min-width: 300px; text-align: center; position: relative;" id="burger-img-container">
            <img src="{img}" alt="{title}" class="main-burger-img" style="width: 100%; max-width: 500px; filter: drop-shadow(0px 20px 30px rgba(0,0,0,0.3)); mix-blend-mode: multiply; position: relative; z-index: 2;">
            <img src="yummy.png" id="naughty-chef" alt="Chef" style="position: absolute; width: 200px; right: -50px; bottom: 0; z-index: 3; opacity: 0; pointer-events: none;">
            <div id="chef-speech" style="position: absolute; right: -100px; top: -50px; background: white; padding: 10px 15px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-weight: bold; color: #D32F2F; opacity: 0; z-index: 4; pointer-events: none;">Oops! I ate it! 😋<br>Making a fresh one...</div>
        </div>
        <div style="flex: 1; min-width: 300px;">
            <h1 style="font-family: 'Bangers', cursive; font-size: 4rem; color: #FF5722; margin-top: 0;">{title}</h1>
            <p style="font-size: 2rem; color: #D32F2F; font-weight: 900; margin: 20px 0;">{price}</p>
            <p style="font-size: 1.2rem; color: #5D4037; line-height: 1.6; margin-bottom: 40px;">
                Experience the ultimate taste of our {title}. Made with the freshest ingredients, premium meat, and our signature sauces, it's guaranteed to satisfy your cravings.
            </p>
            <button class="btn-add-cart" onclick="addToCart(event, '{title}', '{price}')">Add to Cart</button>
        </div>
    </div>

    
    <!-- Cart Modal -->
    <div id="cart-modal" class="modal-overlay">
        <div class="modal-content" style="max-height: 80vh; overflow-y: auto;">
            <span class="close-btn" onclick="closeCartModal()">&times;</span>
            <h2 style="font-family: 'Playfair Display', serif; color: #D32F2F; margin-bottom: 20px;">Your Cart 🛒</h2>
            <div id="cart-items-container" style="text-align: left; margin-bottom: 20px;">
                <!-- Cart items will be injected here -->
            </div>
            <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 1.2rem; margin-bottom: 20px;">
                <span>Total:</span>
                <span id="cart-total-price">₹0</span>
            </div>
            <button class="btn-add-cart" style="width: 100%;" onclick="checkout()">PROCEED TO CHECKOUT</button>
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
                <button type="submit" class="btn-add-cart" style="width:100%; margin-top:20px;">LOGIN</button>
            </form>
            <p style="margin-top:20px; font-size:0.9rem;">
                <span id="toggle-text">Don't have an account?</span> 
                <a href="#" onclick="toggleAuthMode(); return false;" id="toggle-link" style="color:#E85A1F; font-weight:bold;">Sign Up</a>
            </p>
        </div>
    </div>

{footer}


    <script src="cart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof gsap === 'undefined') return;
            const tl = gsap.timeline();
            
            // 1. Burger bounces in from top-left
            tl.from(".main-burger-img", {
                x: -800,
                y: -400,
                rotation: -360,
                duration: 2,
                ease: "bounce.out"
            })
            // 2. Naughty chef slides in
            .to("#naughty-chef", {
                opacity: 1,
                x: -120,
                rotation: -10,
                duration: 0.8,
                ease: "power2.out"
            }, "+=0.5")
            // 3. Chef "eats" the burger
            .to(".main-burger-img", {
                scale: 0,
                opacity: 0,
                rotation: 180,
                duration: 0.5,
                ease: "back.in(2)"
            })
            .to("#naughty-chef", {
                scale: 1.2,
                duration: 0.3,
                yoyo: true,
                repeat: 1
            })
            // 4. Chef speaks
            .to("#chef-speech", {
                opacity: 1,
                y: -20,
                duration: 0.5,
                ease: "back.out(2)"
            })
            // 5. Chef runs away after 2 seconds
            .to(["#naughty-chef", "#chef-speech"], {
                opacity: 0,
                x: 300,
                duration: 1,
                ease: "power2.in"
            }, "+=2")
            // 6. Fresh burger drops down!
            .set(".main-burger-img", {
                scale: 1,
                opacity: 1,
                y: -800,
                rotation: 0
            })
            .to(".main-burger-img", {
                y: 0,
                duration: 1.5,
                ease: "bounce.out"
            });
        });
    </script>
</body>

</html>
"""

for b in burgers:
    page_content = template.replace('{title}', b['title']).replace('{img}', b['img']).replace('{price}', b['price']).replace('{footer}', footer)
    with open(b['page'], "w") as f:
        f.write(page_content)

print("Generated 15 pages and updated index.html")
