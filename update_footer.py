import os
import glob
import re

html_files = glob.glob('*.html')

new_links = '''            <div class="legal-links" style="margin-top: 20px; font-size: 0.85rem;">
                <a href="index.html#about" style="color: #bbb; text-decoration: none; margin: 0 10px;">About Us</a> | 
                <a href="index.html#contact" style="color: #bbb; text-decoration: none; margin: 0 10px;">Contact Us</a> | 
                <a href="disclaimer.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Disclaimer</a> | 
                <a href="privacy_policy.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="terms_of_service.html" style="color: #bbb; text-decoration: none; margin: 0 10px;">Terms & Conditions</a>
            </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # regex to replace the old legal-links div
    pattern = r'<div class="legal-links".*?</div>'
    new_html = re.sub(pattern, new_links, html, flags=re.DOTALL)
    
    if html != new_html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Updated footer links in all HTML files.")
