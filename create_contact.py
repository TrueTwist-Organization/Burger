import os
import re

html_content = """
    <!-- Section 5: Contact Us Universe -->
    <section class="sec-contact-universe" id="contact">
        <!-- Marquee -->
        <div class="contact-marquee">
            <div class="c-marquee-content">
                📞 REACH US ANYTIME &nbsp;·&nbsp; WE LOVE FEEDBACK &nbsp;·&nbsp; 🍔 YOUR OPINION MATTERS &nbsp;·&nbsp; 
                📞 REACH US ANYTIME &nbsp;·&nbsp; WE LOVE FEEDBACK &nbsp;·&nbsp; 🍔 YOUR OPINION MATTERS &nbsp;·&nbsp; 
                📞 REACH US ANYTIME &nbsp;·&nbsp; WE LOVE FEEDBACK &nbsp;·&nbsp; 🍔 YOUR OPINION MATTERS &nbsp;·&nbsp; 
            </div>
        </div>

        <!-- Ambient Backgrounds -->
        <div class="c-bg-layer"></div>
        <div class="c-blob-orange"></div>
        <div class="c-blob-red"></div>
        
        <!-- Floating Ingredients -->
        <div class="c-floating-ingredients">
            <span class="c-ing" style="--i:1; --s:15s; --x: 10%; --y: 20%;">🍅</span>
            <span class="c-ing" style="--i:2; --s:25s; --x: 80%; --y: 15%;">🧅</span>
            <span class="c-ing" style="--i:3; --s:20s; --x: 15%; --y: 80%;">🥬</span>
            <span class="c-ing" style="--i:4; --s:30s; --x: 85%; --y: 85%;">🧀</span>
        </div>

        <div class="contact-container">
            <!-- Left Panel -->
            <div class="c-left-panel">
                <h2 class="c-left-title">LET'S TALK 🍔</h2>
                <svg class="c-brush-stroke" viewBox="0 0 200 15"><path d="M 5 10 Q 100 0 195 10" fill="none" stroke="#E67E22" stroke-width="3" stroke-linecap="round"/></svg>
                <p class="c-left-subtext">"We respond faster than our burgers get eaten 😄"</p>
                
                <div class="c-info-list">
                    <div class="c-info-item">
                        <div class="c-info-icon"><i class="fa-solid fa-location-dot"></i></div>
                        <div class="c-info-text">123 Burger Lane, Food Street<br>Mumbai, Maharashtra</div>
                    </div>
                    <div class="c-info-item phone-item">
                        <div class="c-info-icon"><i class="fa-solid fa-phone"></i></div>
                        <div class="c-info-text"><a href="tel:+919876543210">+91 98765 43210</a></div>
                    </div>
                    <div class="c-info-item email-item">
                        <div class="c-info-icon"><i class="fa-solid fa-envelope"></i></div>
                        <div class="c-info-text"><a href="mailto:hello@burgerhouse.com">hello@burgerhouse.com</a></div>
                    </div>
                    <div class="c-info-item time-item">
                        <div class="c-info-icon"><i class="fa-solid fa-clock"></i></div>
                        <div class="c-info-text">Mon–Sun: 10AM – 11PM</div>
                    </div>
                </div>

                <div class="c-socials">
                    <a href="#" class="c-social-btn"><i class="fa-brands fa-instagram"></i></a>
                    <a href="#" class="c-social-btn"><i class="fa-brands fa-facebook-f"></i></a>
                    <a href="#" class="c-social-btn"><i class="fa-brands fa-twitter"></i></a>
                    <a href="#" class="c-social-btn" style="font-weight:bold; font-family:sans-serif; font-size: 1rem;">Z</a>
                </div>

                <img src="chef_1.png" class="c-chef-wave" alt="Waving Chef">
            </div>

            <!-- Right Panel (Form) -->
            <div class="c-right-panel" id="c-form-panel">
                <div class="c-form-header">
                    <h2 class="c-form-title" id="c-form-title"></h2>
                    <span class="c-form-burger">🍔</span>
                </div>
                <p class="c-form-subtext" id="c-form-subtext"></p>
                <svg class="c-divider-wavy" viewBox="0 0 300 20"><path d="M 0 10 Q 30 0 60 10 T 120 10 T 180 10 T 240 10 T 300 10" fill="none" stroke="#E8D5C0" stroke-width="2" stroke-linecap="round"/></svg>

                <!-- Form -->
                <form id="burger-contact-form" class="c-form" novalidate>
                    <div class="c-input-group">
                        <i class="fa-solid fa-user c-input-icon"></i>
                        <input type="text" id="c-name" class="c-input" required placeholder=" ">
                        <label for="c-name" class="c-label">Your Name</label>
                        <svg class="c-check-icon" viewBox="0 0 24 24"><path d="M5 12l5 5l10 -10" fill="none" stroke="#27AE60" stroke-width="3" stroke-linecap="round"/></svg>
                        <div class="c-error-msg"><i class="fa-solid fa-triangle-exclamation"></i> This field is required</div>
                    </div>

                    <div class="c-input-group">
                        <i class="fa-solid fa-envelope c-input-icon"></i>
                        <input type="email" id="c-email" class="c-input" required placeholder=" ">
                        <label for="c-email" class="c-label">Your Email</label>
                        <svg class="c-check-icon" viewBox="0 0 24 24"><path d="M5 12l5 5l10 -10" fill="none" stroke="#27AE60" stroke-width="3" stroke-linecap="round"/></svg>
                        <div class="c-error-msg" id="c-email-err"><i class="fa-solid fa-triangle-exclamation"></i> Hmm, check that email 🤔</div>
                    </div>

                    <div class="c-input-group c-textarea-group">
                        <textarea id="c-message" class="c-input" required placeholder=" " rows="4" maxlength="500"></textarea>
                        <label for="c-message" class="c-label">Tell us anything — feedback, orders, love for our burgers... 🍔❤️</label>
                        <div class="c-char-count"><span id="c-char-current">0</span> / 500</div>
                        <div class="c-error-msg"><i class="fa-solid fa-triangle-exclamation"></i> Message cannot be empty</div>
                    </div>

                    <button type="submit" class="c-btn-submit" id="c-btn-submit">
                        <span class="c-btn-text">SEND MESSAGE 🚀</span>
                        <div class="c-btn-loader">
                            <span class="c-spin-burger">🍔</span> Sending<span class="c-dots">...</span>
                        </div>
                        <div class="c-btn-success">
                            <svg class="c-btn-check" viewBox="0 0 24 24"><path d="M5 12l5 5l10 -10" fill="none" stroke="white" stroke-width="3" stroke-linecap="round"/></svg>
                            MESSAGE SENT!
                        </div>
                        <span class="c-paper-plane">✈️</span>
                    </button>
                </form>

                <!-- Success State Overlay -->
                <div class="c-success-overlay" id="c-success-overlay">
                    <img src="yummy.png" class="c-success-chef" alt="Chef on Phone">
                    <div class="c-success-bubble">Got it! We'll call you faster than you can say 'double patty'! 🍔</div>
                    
                    <div class="c-success-circle">
                        <svg class="c-big-check" viewBox="0 0 50 50"><path d="M10 25l10 10l20 -20" fill="none" stroke="#27AE60" stroke-width="4" stroke-linecap="round"/></svg>
                    </div>
                    <h3 class="c-success-title">WE'LL BE IN TOUCH SOON! 🎉</h3>
                    <p class="c-success-subtext" id="c-success-subtext"></p>
                    
                    <button class="c-btn-reset" onclick="resetContactForm()">SEND ANOTHER MESSAGE</button>
                </div>
                
                <img src="classic_cheese_burger.png" class="c-corner-burger top-left" alt="">
                <img src="spicy_chicken_burger.png" class="c-corner-burger bottom-right" alt="">
            </div>
        </div>
        
        <div id="c-toast" class="c-toast">Please fill all fields! 🙏</div>
    </section>
"""

with open('index.html', 'r') as f:
    index = f.read()

# Replace the existing #contact section
contact_regex = r'<!-- Section 5: Contact Us -->\s*<section id="contact".*?</section>'
index = re.sub(contact_regex, html_content, index, flags=re.DOTALL)

# Add CSS and JS links if not exist
if '<link rel="stylesheet" href="contact.css">' not in index:
    index = index.replace('<link rel="stylesheet" href="cart_enhanced.css">', '<link rel="stylesheet" href="cart_enhanced.css">\n    <link rel="stylesheet" href="contact.css">')

if '<script src="contact.js"></script>' not in index:
    index = index.replace('<script src="universe.js"></script>', '<script src="universe.js"></script>\n    <script src="contact.js"></script>')

with open('index.html', 'w') as f:
    f.write(index)

print("index.html updated successfully.")
