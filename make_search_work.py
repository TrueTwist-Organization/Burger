import glob
import re

search_modal_html = """
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
"""

search_js = """
    <script>
        function openSearchModal() {
            const modal = document.getElementById('search-modal');
            modal.classList.remove('hidden');
            setTimeout(() => document.getElementById('search-input').focus(), 100);
        }
        function closeSearchModal() {
            document.getElementById('search-modal').classList.add('hidden');
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
                // Redirect to index.html with search query
                window.location.href = 'index.html?search=' + encodeURIComponent(val) + '#menu';
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
"""

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the search icon to ALWAYS call openSearchModal()
    # It might be `onclick="window.location.href='index.html#menu'"` or `onclick="openSearchModal()"`
    pattern_icon = r'<span onclick="[^"]*" style="cursor:pointer;">🔍</span>'
    html = re.sub(pattern_icon, '<span onclick="openSearchModal()" style="cursor:pointer;">🔍</span>', html)
    
    # 2. Inject Search Modal HTML and JS if not already there
    # Remove old search modal scripts from index.html if it exists
    if file == 'index.html':
        old_modal_pattern = r'<!-- Search Modal -->.*?</div>\s*</div>'
        html = re.sub(old_modal_pattern, '', html, flags=re.DOTALL)
        
        old_script_pattern = r'<script>\s*function openSearchModal\(\).*?function performSearch\(\).*?</script>'
        html = re.sub(old_script_pattern, '', html, flags=re.DOTALL)
    
    if 'id="search-modal"' not in html:
        # Insert right before </body>
        html = html.replace('</body>', search_modal_html + search_js + '\n</body>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Injected universal Search Modal and logic into all pages!")
