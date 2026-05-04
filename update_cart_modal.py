import re

cart_modal_html = """
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
            <button class="btn-primary" style="width: 100%;" onclick="checkout()">PROCEED TO CHECKOUT</button>
        </div>
    </div>
"""

# Update index.html
with open('index.html', 'r') as f:
    html = f.read()

# Change cart icon onclick
html = html.replace("showToast('Opening Cart...')", "openCartModal()")

# Insert Cart Modal before Login Modal
html = html.replace('<!-- Login Modal -->', cart_modal_html + '\n    <!-- Login Modal -->')

# Add Add to Cart buttons to menu cards in index.html
def add_button(match):
    # match is the </a> tag
    # we need to extract title and price from the card to create the button
    # but the regex is complex. Let's just do it with a simple replacement.
    pass

with open('index.html', 'w') as f:
    f.write(html)

# Update generate_pages.py
with open('generate_pages.py', 'r') as f:
    py_code = f.read()

py_code = py_code.replace("showToast('Opening Cart...')", "openCartModal()")
py_code = py_code.replace('<!-- Login Modal -->', cart_modal_html + '\n    <!-- Login Modal -->')

with open('generate_pages.py', 'w') as f:
    f.write(py_code)

print("Updated HTML files.")
