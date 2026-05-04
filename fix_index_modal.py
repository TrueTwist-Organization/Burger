import re

with open('index.html', 'r') as f:
    html = f.read()

pattern = re.compile(r'<div id="cart-modal".*?</div>\s*</div>', re.DOTALL)

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

html = re.sub(pattern, new_modal, html)

with open('index.html', 'w') as f:
    f.write(html)
    
print("Fixed index.html cart modal.")
