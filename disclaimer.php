<?php declare(strict_types=1); require_once __DIR__ . '/includes/config.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@1,400;1,600&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css?v=1348">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background-color: #FFF8E1;">
    <header>
        <a href="index.php" class="logo">
            <span class="icon">🍔</span> BURGER
        </a>
        <nav style="display: flex; gap: 20px;">
            <a href="index.php" class="nav-link">Home</a>
            <a href="index.php#menu" class="nav-link">Menu</a>
            <a href="index.php#story" class="nav-link">About</a>
            <a href="index.php#contact" class="nav-link">Contact Us</a>
        </nav>
    </header>

    <div style="max-width: 800px; margin: 150px auto 100px auto; padding: 40px; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
        <h1 style="color: #D32F2F; font-family: 'Playfair Display', serif; margin-bottom: 30px;">Disclaimer</h1>
        <div style="font-size: 1.1rem; color: #5D4037; line-height: 1.8;">
            <p>The information provided by The Perfect Burger on this website is for general informational purposes only. All information on the Site is provided in good faith, however we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information on the Site.</p>
            <p>Under no circumstance shall we have any liability to you for any loss or damage of any kind incurred as a result of the use of the site or reliance on any information provided on the site. Your use of the site and your reliance on any information on the site is solely at your own risk.</p>
            <p>The Site may contain links to other websites or content belonging to or originating from third parties. Such external links are not investigated, monitored, or checked for accuracy, adequacy, validity, reliability, availability or completeness by us.</p>
            <p style="margin-top: 40px;"><em>Last updated: May 2026</em></p>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-content" style="text-align: center; color: white;">
            <a href="index.php" class="footer-logo">🍔 BURGER</a>
            <p>Crafted with flavor, served with love.</p>
            <div class="socials" style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
                <a href="https://facebook.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s; color: white;"><i class="fab fa-facebook-f"></i></a>
                <a href="https://instagram.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s; color: white;"><i class="fab fa-instagram"></i></a>
                <a href="https://twitter.com" target="_blank" style="font-size: 1.5rem; transition: color 0.3s; color: white;"><i class="fab fa-twitter"></i></a>
            </div>
                        <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="index.php#story" style="color: #bbb; text-decoration: none; margin: 0 10px;">About Us</a> | 
                <a href="index.php#contact" style="color: #bbb; text-decoration: none; margin: 0 10px;">Contact Us</a> | 
                <a href="disclaimer.php" style="color: #bbb; text-decoration: none; margin: 0 10px;">Disclaimer</a> | 
                <a href="privacy_policy.php" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="terms_of_service.php" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms & Conditions</a>
            </div>
        </div>
        <div class="footer-bottom" style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; color: #999;">
            &copy; 2026 The Perfect Burger. All rights reserved.
        </div>
    </footer>

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
