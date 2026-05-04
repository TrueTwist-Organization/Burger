import os
import glob

# HTML to find
find_html = """                <a href="#" onclick="showToast('Redirecting to Facebook...'); return false;" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-facebook-f"></i></a>
                <a href="#" onclick="showToast('Redirecting to Instagram...'); return false;" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-instagram"></i></a>
                <a href="#" onclick="showToast('Redirecting to Twitter...'); return false;" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-twitter"></i></a>
            </div>
            <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="#" onclick="showToast('Privacy Policy coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="#" onclick="showToast('Terms of Service coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
                <a href="#" onclick="showToast('Cookie Policy coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Cookie Policy</a> | 
                <a href="#" onclick="showToast('Refund Policy coming soon!'); return false;" style="color: #bbb; text-decoration: none; margin: 0 10px;">Refund Policy</a>
            </div>"""

# HTML to replace
replace_html = """                <a href="https://facebook.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-facebook-f"></i></a>
                <a href="https://instagram.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-instagram"></i></a>
                <a href="https://twitter.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-twitter"></i></a>
            </div>
            <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="privacy_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="terms_of_service.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
                <a href="cookie_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Cookie Policy</a> | 
                <a href="refund_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Refund Policy</a>
            </div>"""

# Update all HTML files
html_files = glob.glob("*.html")
for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    if find_html in content:
        content = content.replace(find_html, replace_html)
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Skipped {f} (pattern not found)")

# Generate the 4 policy pages based on a generic template
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
        <nav>
            <a href="index.html">Home</a>
            <a href="index.html#menu">Menu</a>
            <a href="index.html#about">About</a>
            <a href="index.html#contact">Contact Us</a>
        </nav>
    </header>

    <div style="max-width: 800px; margin: 150px auto 100px auto; padding: 40px; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
        <h1 style="color: #D32F2F; font-family: 'Playfair Display', serif; margin-bottom: 30px;">{title}</h1>
        <div style="font-size: 1.1rem; color: #5D4037; line-height: 1.8;">
            <p>Welcome to The Perfect Burger. This page outlines our {title.lower()}.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <p>If you have any questions about our {title.lower()}, please feel free to <a href="index.html#contact" style="color: #E85A1F;">contact us</a>.</p>
            <p style="margin-top: 40px;"><em>Last updated: May 2026</em></p>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-logo">🍔 BURGER</div>
            <p>Crafted with flavor, served with love.</p>
            <div class="socials" style="display: flex; justify-content: center; gap: 20px;">
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
        <div class="footer-bottom" style="margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; color: #999;">
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
        file.write(template.format(title=title))
    print(f"Created {filename}")

