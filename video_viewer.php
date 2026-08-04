<?php declare(strict_types=1); require_once __DIR__ . '/includes/config.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Video Viewer</title>
</head>
<body>
    <video id="vid" src="animation.mp4" controls autoplay muted style="max-width: 100%;"></video>
    <div id="info" style="font-size: 20px; font-family: monospace; margin-top: 20px;"></div>
    <script>
        const vid = document.getElementById('vid');
        const info = document.getElementById('info');
        
        vid.addEventListener('timeupdate', () => {
            info.innerText = "Current Time: " + vid.currentTime.toFixed(2) + "s";
        });
        
        // Expose a function to jump to time
        window.jumpTo = function(t) {
            vid.currentTime = t;
        }
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
