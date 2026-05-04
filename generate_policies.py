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
            <p>Welcome to The Perfect Burger. This page outlines our {title_lower}.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
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
    "privacy_policy.html": "Privacy Policy",
    "terms_of_service.html": "Terms of Service",
    "cookie_policy.html": "Cookie Policy",
    "refund_policy.html": "Refund Policy"
}

for filename, title in pages.items():
    with open(filename, 'w') as file:
        file.write(template.format(title=title, title_lower=title.lower()))
    print(f"Created {filename}")

