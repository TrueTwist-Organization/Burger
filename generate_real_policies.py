template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@1,400;1,600&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background-color: #FFF8E1;">
    <header>
        <div class="logo">
            <span class="icon">🍔</span> BURGER
        </div>
        <nav style="display: flex; gap: 20px;">
            <a href="index.html" class="nav-link">Home</a>
            <a href="index.html#menu" class="nav-link">Menu</a>
            <a href="index.html#about" class="nav-link">About</a>
            <a href="index.html#contact" class="nav-link">Contact Us</a>
        </nav>
    </header>

    <div style="max-width: 800px; margin: 150px auto 100px auto; padding: 40px; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
        <h1 style="color: #D32F2F; font-family: 'Playfair Display', serif; margin-bottom: 30px;">{title}</h1>
        <div style="font-size: 1.1rem; color: #5D4037; line-height: 1.8;">
{content}
            <p>If you have any questions about our {title_lower}, please feel free to <a href="index.html#contact" style="color: #E85A1F;">contact us</a>.</p>
            <p style="margin-top: 40px;"><em>Last updated: May 2026</em></p>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-content" style="text-align: center; color: white;">
            <div class="footer-logo" style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #F5ECD7; margin-bottom: 10px;">🍔 BURGER</div>
            <p>Crafted with flavor, served with love.</p>
            <div class="socials" style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
                <a href="https://facebook.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s; color: white;"><i class="fab fa-facebook-f"></i></a>
                <a href="https://instagram.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s; color: white;"><i class="fab fa-instagram"></i></a>
                <a href="https://twitter.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s; color: white;"><i class="fab fa-twitter"></i></a>
            </div>
            <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="privacy_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="terms_of_service.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
                <a href="cookie_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Cookie Policy</a> | 
                <a href="refund_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Refund Policy</a>
            </div>
        </div>
        <div class="footer-bottom" style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; color: #999;">
            &copy; 2026 The Perfect Burger. All rights reserved.
        </div>
    </footer>
</body>
</html>
"""

pages = {
    "privacy_policy.html": {
        "title": "Privacy Policy",
        "content": '''            <p>Welcome to The Perfect Burger. We respect your privacy and are committed to protecting your personal data.</p>
            <p>This privacy policy will inform you about how we look after your personal data when you visit our website and tell you about your privacy rights and how the law protects you. We collect minimal information such as your name, email address, and order history strictly for the purpose of fulfilling your orders and improving our services.</p>
            <p>We do not sell or share your personal data with third parties for marketing purposes. By using our website, you consent to the data practices described in this statement.</p>'''
    },
    "terms_of_service.html": {
        "title": "Terms of Service",
        "content": '''            <p>Welcome to The Perfect Burger. These Terms of Service govern your use of our website and services.</p>
            <p>By accessing or using our website, you agree to be bound by these Terms. All content, including images, text, and logos, is the property of The Perfect Burger and may not be copied or reproduced without permission. When placing an order, you agree to provide accurate and complete information.</p>
            <p>We reserve the right to refuse service, terminate accounts, or cancel orders at our sole discretion. Prices for our products are subject to change without notice.</p>'''
    },
    "cookie_policy.html": {
        "title": "Cookie Policy",
        "content": '''            <p>The Perfect Burger uses cookies to enhance your browsing experience and analyze our website traffic.</p>
            <p>Cookies are small data files stored on your device that help us remember your preferences and understand how you interact with our site. We use essential cookies to enable basic functions like page navigation and access to secure areas of the website. We may also use analytical cookies to collect aggregated data about our visitors.</p>
            <p>You can choose to accept or decline cookies through your browser settings, though declining may prevent you from taking full advantage of the website.</p>'''
    },
    "refund_policy.html": {
        "title": "Refund Policy",
        "content": '''            <p>At The Perfect Burger, we strive to serve you the freshest and most delicious meals. If you are not entirely satisfied with your order, we're here to help.</p>
            <p>If your food arrives cold, incorrect, or damaged, please contact us within 2 hours of delivery with your order details and a photo of the item. We will gladly offer a replacement or process a full or partial refund to your original method of payment.</p>
            <p>Please note that since our products are perishable, we cannot accept returns of food items. Refunds may take 3-5 business days to process depending on your bank.</p>'''
    }
}

for filename, data in pages.items():
    with open(filename, 'w') as file:
        file.write(template.format(
            title=data['title'], 
            content=data['content'], 
            title_lower=data['title'].lower()
        ))
    print(f"Updated {filename} with real text")

