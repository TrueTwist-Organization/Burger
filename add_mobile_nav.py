import glob
import re

# 1. Update HTML files to add menu toggle inside .icons
html_files = glob.glob('*.html')

toggle_html = '            <span class="menu-toggle" onclick="document.querySelector(\'nav\').classList.toggle(\'active\')" style="cursor:pointer; display:none; margin-left:15px; color:#D32F2F; font-size: 1.5rem;"><i class="fa-solid fa-bars"></i></span>\n        </div>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check if menu-toggle already exists
    if 'class="menu-toggle"' not in html:
        # Replace the closing </div> of .icons with the toggle and closing </div>
        # But we need to make sure we only match the one for .icons.
        # Actually, let's find the .user-icon span and insert right after it.
        # <span class="user-icon" ...>👤</span>
        pattern = r'(<span class="user-icon"[^>]*>👤</span>)'
        new_html = re.sub(pattern, r'\1\n            <span class="menu-toggle" onclick="document.querySelector(\'nav\').classList.toggle(\'active\')" style="cursor:pointer; display:none; margin-left:15px; color:#D32F2F; font-size: 1.5rem;"><i class="fa-solid fa-bars"></i></span>', html)
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)

# 2. Append CSS to style.css
css_addition = '''
/* MOBILE NAVBAR TOGGLE */
@media (max-width: 768px) {
    header .menu-toggle {
        display: inline-block !important;
    }
    header nav {
        display: none !important;
        flex-direction: column !important;
        position: absolute !important;
        top: 100% !important;
        left: 0 !important;
        width: 100% !important;
        background: #FFF !important;
        box-shadow: 0 15px 30px rgba(0,0,0,0.15) !important;
        padding: 10px 0 !important;
        z-index: 1000 !important;
        border-top: 3px solid #E85A1F !important;
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
    }
    header nav.active {
        display: flex !important;
        animation: slideDownNav 0.3s ease forwards;
    }
    header nav a {
        font-size: 1.2rem !important;
        padding: 15px 20px !important;
        width: 100% !important;
        text-align: center !important;
        border-bottom: 1px solid rgba(0,0,0,0.05) !important;
        color: #D32F2F !important;
    }
    header nav a:last-child {
        border-bottom: none !important;
    }
    header nav .nav-indicator {
        display: none !important;
    }
}

@keyframes slideDownNav {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '/* MOBILE NAVBAR TOGGLE */' not in css_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)

print("Added mobile navbar toggle successfully!")
