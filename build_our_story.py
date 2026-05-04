import re

html_content = """
    <!-- Section 3: Our Story (Cinematic Redesign) -->
    <section class="sec-story-new" id="story">
        <!-- Background Atmosphere -->
        <div class="story-bg-texture"></div>
        <div class="story-bg-blobs">
            <div class="blob blob-orange"></div>
            <div class="blob blob-red"></div>
        </div>
        <div class="story-watermark">
            <img src="burger_transparent.png" alt="Watermark Burger" style="opacity: 0.15; filter: grayscale(100%); width: 800px; height: 800px; object-fit: contain;">
        </div>
        
        <!-- Top Wave Divider -->
        <div class="story-wave wave-top">
            <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" fill="#FFF8EE"></path>
            </svg>
        </div>

        <div class="story-container">
            
            <!-- Heading -->
            <div class="story-header io-trigger">
                <div class="est-badge">EST. 2018 🍔</div>
                <div class="title-wrapper">
                    <span class="quote-mark-bg">"</span>
                    <div class="title-line-1">OUR</div>
                    <div class="title-line-2">STORY <span class="beating-heart">❤️</span></div>
                    <svg class="title-underline" viewBox="0 0 400 20" preserveAspectRatio="none">
                        <path class="draw-line" d="M10,10 Q200,20 390,5" fill="none" stroke="#E67E22" stroke-width="6" stroke-linecap="round"/>
                    </svg>
                </div>
            </div>

            <!-- Pull Quote -->
            <div class="story-pull-quote io-trigger">
                " Every burger tells a story. "
            </div>

            <!-- Two Column Layout -->
            <div class="story-columns">
                <!-- Left: Visual -->
                <div class="story-col-left io-trigger">
                    <div class="chef-spotlight"></div>
                    <div class="chef-wrapper" id="story-chef">
                        <img src="chef_1.png" class="chef-hero" alt="Chef Marco">
                        <div class="chef-platform">Since 2018</div>
                        <div class="steam-wisps"></div>
                        <div class="chef-speech-bubble" id="chef-speech">Psst... secret ingredient is love! ❤️</div>
                    </div>
                    <div class="chef-badges">
                        <div class="badge-item badge-award">
                            <span class="badge-icon">🏆</span>
                            <span class="badge-text">Best Burger<br>2022</span>
                        </div>
                        <div class="badge-item badge-rating">
                            <span class="badge-icon">⭐</span>
                            <span class="badge-text">4.9<br>Rating</span>
                        </div>
                        <div class="badge-item badge-orders">
                            <span class="badge-icon">🍔</span>
                            <span class="badge-text">50K+<br>Orders</span>
                        </div>
                    </div>
                </div>

                <!-- Right: Text -->
                <div class="story-col-right">
                    <div class="story-chapter io-trigger" data-chapter="1">
                        <div class="chapter-icon">🌱</div>
                        <h3>HOW IT STARTED</h3>
                        <p class="reveal-text">Founded with a simple mission: to create the ultimate burger experience. It all started in a small kitchen...</p>
                    </div>
                    <div class="chapter-divider"></div>
                    <div class="story-chapter io-trigger" data-chapter="2">
                        <div class="chapter-icon">💪</div>
                        <h3>WHAT WE BELIEVE</h3>
                        <p class="reveal-text">We believe great food starts with great ingredients. From daily baked artisan buns to secret signature sauces...</p>
                    </div>
                    <div class="chapter-divider"></div>
                    <div class="story-chapter io-trigger" data-chapter="3">
                        <div class="chapter-icon">🤝</div>
                        <h3>OUR PROMISE</h3>
                        <p class="reveal-text">Every single layer is crafted with passion and served with love. That's our promise to you.</p>
                    </div>
                </div>
            </div>

            <!-- Stats Counter Row -->
            <div class="story-stats" id="stats-counter-trigger">
                <div class="stat-card io-trigger">
                    <div class="stat-icon-wrap"><span class="stat-icon">🍔</span></div>
                    <div class="stat-number-wrap">
                        <span class="stat-number" data-target="50000">0</span><span class="stat-suffix">+</span>
                    </div>
                    <div class="stat-label">Burgers Served</div>
                </div>
                <div class="stat-card io-trigger">
                    <div class="stat-icon-wrap"><span class="stat-icon">⭐</span></div>
                    <div class="stat-number-wrap">
                        <span class="stat-number" data-target="4.9" data-decimals="1">0</span><span class="stat-suffix">/5</span>
                    </div>
                    <div class="stat-label">Average Rating</div>
                </div>
                <div class="stat-card io-trigger">
                    <div class="stat-icon-wrap"><span class="stat-icon">👨‍🍳</span></div>
                    <div class="stat-number-wrap">
                        <span class="stat-number" data-target="8">0</span><span class="stat-suffix">+</span>
                    </div>
                    <div class="stat-label">Years of Passion</div>
                </div>
                <div class="stat-card io-trigger">
                    <div class="stat-icon-wrap"><span class="stat-icon">📍</span></div>
                    <div class="stat-number-wrap">
                        <span class="stat-number" data-target="3">0</span><span class="stat-suffix"></span>
                    </div>
                    <div class="stat-label">Locations</div>
                </div>
            </div>

            <!-- Timeline -->
            <div class="story-timeline-section io-trigger" id="timeline-trigger">
                <div class="timeline-line-track">
                    <div class="timeline-line-fill" id="timeline-fill"></div>
                </div>
                <div class="timeline-points">
                    <div class="t-point" style="left: 0%;">
                        <div class="t-dot"></div>
                        <div class="t-content">
                            <span class="t-year">2018</span>
                            <p>Started in a garage kitchen</p>
                            <div class="t-ill">🏠</div>
                        </div>
                    </div>
                    <div class="t-point" style="left: 33%;">
                        <div class="t-dot"></div>
                        <div class="t-content">
                            <span class="t-year">2019</span>
                            <p>First 1000 customers</p>
                            <div class="t-ill">🙌</div>
                        </div>
                    </div>
                    <div class="t-point" style="left: 66%;">
                        <div class="t-dot"></div>
                        <div class="t-content">
                            <span class="t-year">2021</span>
                            <p>Opened 2nd location</p>
                            <div class="t-ill">🏪</div>
                        </div>
                    </div>
                    <div class="t-point" style="left: 100%;">
                        <div class="t-dot"></div>
                        <div class="t-content">
                            <span class="t-year">2024</span>
                            <p>50,000 orders milestone</p>
                            <div class="t-ill">🎉</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Chef Quote Card -->
            <div class="story-quote-card io-trigger">
                <div class="sqc-left">
                    <img src="chef_1.png" alt="Chef Holding Burger" class="sqc-chef">
                </div>
                <div class="sqc-right">
                    <span class="sqc-quote-mark-large">"</span>
                    <div class="sqc-lines">
                        <p class="sqc-line">I pour my heart into every burger.</p>
                        <p class="sqc-line">When you take that first bite and</p>
                        <p class="sqc-line">smile — that's why I do this.</p>
                    </div>
                    <div class="sqc-author">— Chef Marco, Founder</div>
                    <div class="sqc-signature-line"></div>
                </div>
                <div class="sqc-hat-icon">👨‍🍳</div>
            </div>

        </div>

        <!-- Bottom Wave Divider -->
        <div class="story-wave wave-bottom">
            <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" fill="#F5ECD7"></path>
            </svg>
        </div>
    </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<!-- Section 3: The Epic Story \(Replaces old exploded section\) -->\s*<section class="sec-story" id="story">.*?</section>'
new_html = re.sub(pattern, html_content, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html")
