import os
import glob

# 1. Update style.css
css_to_add = """
/* --- ENHANCED CART MODAL --- */
.cart-modal-content {
    background: #FFF8E1 !important;
    border-radius: 20px !important;
    padding: 30px !important;
    max-width: 450px !important;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2) !important;
    border: 4px solid white !important;
}
.cart-header h2 {
    font-family: 'Playfair Display', serif;
    color: #D32F2F;
    margin-bottom: 5px;
    font-size: 2rem;
}
.cart-header p {
    color: #E85A1F;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 20px;
}
.cart-items-wrapper {
    max-height: 45vh;
    overflow-y: auto;
    padding-right: 10px;
    margin-bottom: 20px;
    text-align: left;
}
/* Custom Scrollbar for Cart */
.cart-items-wrapper::-webkit-scrollbar {
    width: 6px;
}
.cart-items-wrapper::-webkit-scrollbar-thumb {
    background: #FFCC80;
    border-radius: 10px;
}
.cart-item-card {
    background: white;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    border-left: 4px solid #E85A1F;
    transition: transform 0.2s;
}
.cart-item-card:hover {
    transform: translateY(-2px);
}
.cart-item-info strong {
    color: #5D4037;
    font-size: 1.05rem;
    display: block;
    margin-bottom: 4px;
}
.cart-item-price {
    color: #D32F2F;
    font-weight: bold;
    font-size: 1.1rem;
}
.btn-remove-item {
    background: #FFEbee;
    color: #D32F2F;
    border: none;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    font-size: 1.2rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
}
.btn-remove-item:hover {
    background: #D32F2F;
    color: white;
    transform: rotate(90deg);
}
.cart-footer {
    border-top: 2px dashed #FFCC80;
    padding-top: 20px;
}
.cart-total-row {
    display: flex;
    justify-content: space-between;
    font-size: 1.4rem;
    font-family: 'Playfair Display', serif;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
}
.cart-total-row #cart-total-price {
    color: #D32F2F;
}
.btn-checkout {
    background: linear-gradient(135deg, #D32F2F, #E85A1F);
    color: white;
    border: none;
    padding: 16px;
    width: 100%;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(211, 47, 47, 0.4);
    transition: all 0.3s;
}
.btn-checkout:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(211, 47, 47, 0.6);
}
"""

with open('style.css', 'r') as f:
    style = f.read()
if ".cart-modal-content {" not in style:
    with open('style.css', 'a') as f:
        f.write(css_to_add)

# 2. Replace HTML in all files
old_modal = """<div id="cart-modal" class="modal-overlay">
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
            <button class="btn-primary" style="width: 100%;" onclick="checkout()">PROCEED TO CHECKOUT</button>
        </div>
    </div>"""

new_modal = """<div id="cart-modal" class="modal-overlay">
        <div class="modal-content cart-modal-content">
            <span class="close-btn" onclick="closeCartModal()">&times;</span>
            <div class="cart-header">
                <h2>Your Cart 🛒</h2>
                <p>Ready to satisfy your cravings?</p>
            </div>
            <div id="cart-items-container" class="cart-items-wrapper">
                <!-- Cart items will be injected here -->
            </div>
            <div class="cart-footer">
                <div class="cart-total-row">
                    <span>Total:</span>
                    <span id="cart-total-price">₹0</span>
                </div>
                <button class="btn-checkout" onclick="checkout()">PROCEED TO CHECKOUT 🍔</button>
            </div>
        </div>
    </div>"""

html_files = glob.glob("*.html")
for h_file in html_files:
    if h_file == "checkout.html": continue
    with open(h_file, 'r') as f:
        html = f.read()
    if old_modal in html:
        html = html.replace(old_modal, new_modal)
        with open(h_file, 'w') as f:
            f.write(html)
        print(f"Updated HTML structure in {h_file}")

# 3. Update cart.js
with open('cart.js', 'r') as f:
    js = f.read()

# Update render logic
old_render = """container.innerHTML += `
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #eee;">
                <div>
                    <strong>${item.name}</strong><br>
                    <span style="color: #E85A1F;">${item.price}</span>
                </div>
                <button onclick="removeFromCart(${index})" style="background: none; border: none; color: #D32F2F; cursor: pointer; font-size: 1.2rem;">&times;</button>
            </div>
        `;"""

new_render = """container.innerHTML += `
            <div class="cart-item-card">
                <div class="cart-item-info">
                    <strong>${item.name}</strong>
                    <div class="cart-item-price">${item.price}</div>
                </div>
                <button class="btn-remove-item" onclick="removeFromCart(${index})" title="Remove item">&times;</button>
            </div>
        `;"""

if old_render in js:
    js = js.replace(old_render, new_render)
else:
    print("Old render logic not found in cart.js")

# Update checkout logic
old_checkout = """function checkout() {
    let cart = JSON.parse(localStorage.getItem('burger_cart')) || [];
    if (cart.length === 0) {
        showToast("Cart is empty!");
        return;
    }
    closeCartModal();
    showToast("Processing your order...");
    setTimeout(() => {
        localStorage.removeItem('burger_cart');
        cartItems = [];
        updateCartDisplay();
        showToast("Order placed successfully! 🍔");
    }, 1500);
}"""

new_checkout = """function checkout() {
    let cart = JSON.parse(localStorage.getItem('burger_cart')) || [];
    if (cart.length === 0) {
        showToast("Cart is empty!");
        return;
    }
    // Redirect to the amazing multi-step checkout
    window.location.href = 'checkout.html';
}"""

if old_checkout in js:
    js = js.replace(old_checkout, new_checkout)
else:
    print("Old checkout logic not found in cart.js")

with open('cart.js', 'w') as f:
    f.write(js)

print("Updated cart.js!")

