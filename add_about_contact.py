import re

sections_html = """
    <!-- Section 4: About Us -->
    <section id="about" style="padding: 100px 20px; background-color: #fff; text-align: center;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #D32F2F; margin-bottom: 20px;">OUR STORY</h2>
            <p style="font-size: 1.1rem; color: #5D4037; line-height: 1.8; margin-bottom: 30px;">
                Founded with a simple mission: to create the ultimate burger experience. At The Perfect Burger, we believe that great food starts with great ingredients. From our daily baked artisan buns to our secret signature sauces and locally sourced premium meats, every single layer is crafted with passion and served with love.
            </p>
            <img src="chef_1.png" alt="Chef" style="width: 150px;">
        </div>
    </section>

    <!-- Section 5: Contact Us -->
    <section id="contact" style="padding: 100px 20px; background-color: #FFF8E1; text-align: center;">
        <div style="max-width: 600px; margin: 0 auto; background: #fff; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #E85A1F; margin-bottom: 10px;">GET IN TOUCH</h2>
            <p style="color: #777; margin-bottom: 30px;">We'd love to hear from you. Drop us a message!</p>
            <form onsubmit="event.preventDefault(); showToast('Message sent successfully! We will get back to you soon.'); this.reset();" style="display: flex; flex-direction: column; gap: 15px;">
                <input type="text" placeholder="Your Name" required style="padding: 12px 15px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Montserrat', sans-serif; font-size: 1rem;">
                <input type="email" placeholder="Your Email" required style="padding: 12px 15px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Montserrat', sans-serif; font-size: 1rem;">
                <textarea placeholder="Your Message" rows="4" required style="padding: 12px 15px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Montserrat', sans-serif; resize: vertical; font-size: 1rem;"></textarea>
                <button type="submit" class="btn-primary" style="margin-top: 10px; font-size: 1.1rem; border:none; padding:15px; border-radius:8px; background:#E85A1F; color:#fff; font-weight:bold; cursor:pointer;">Send Message</button>
            </form>
        </div>
    </section>
"""

# Update index.html
with open('index.html', 'r') as f:
    html = f.read()

# Insert the sections right before <!-- Login Modal -->
html = html.replace('<!-- Login Modal -->', sections_html + '\n    <!-- Login Modal -->')

# Update Nav Links in index.html
html = re.sub(r'<a href="#" onclick="showToast\(\'About page coming soon!\'\); return false;">About</a>', '<a href="#about">About</a>', html)
html = re.sub(r'<a href="#" onclick="showToast\(\'Contact page coming soon!\'\); return false;">Contact Us</a>', '<a href="#contact">Contact Us</a>', html)

with open('index.html', 'w') as f:
    f.write(html)

# Update generate_pages.py
with open('generate_pages.py', 'r') as f:
    py_code = f.read()

# For subpages, the links should point to index.html#about and index.html#contact
py_code = re.sub(r'<a href="#" onclick="showToast\(\'About page coming soon!\'\); return false;">About</a>', '<a href="index.html#about">About</a>', py_code)
py_code = re.sub(r'<a href="#" onclick="showToast\(\'Contact page coming soon!\'\); return false;">Contact Us</a>', '<a href="index.html#contact">Contact Us</a>', py_code)

with open('generate_pages.py', 'w') as f:
    f.write(py_code)

print("Added About and Contact Us sections.")
