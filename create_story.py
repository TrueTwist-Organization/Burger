import re

html_content = """
    <!-- Section 3: The Epic Story (Replaces old exploded section) -->
    <section class="sec-story" id="story">
        <div class="story-bg"></div>
        <div class="story-park">
            <div class="sky"></div>
            <div class="grass"></div>
            <div class="sun"></div>
        </div>
        
        <!-- Comic Effects -->
        <div class="comic-snap c-top-left">SNAP!</div>
        <div class="comic-snap c-top-right">SNAP!</div>
        <div class="comic-snap c-bottom-left">SNAP!</div>
        <div class="comic-snap c-bottom-right">SNAP!</div>
        <div class="flash-ring"></div>
        <div class="impact-lines"></div>
        <div class="perfect-text">THE PERFECT BURGER</div>
        
        <div class="comic-chomp">CHOMP!</div>
        <div class="comic-nom">NOM NOM NOM!</div>
        
        <!-- Characters -->
        <div class="char char-boy">
            <div class="c-head"><div class="c-eye l"></div><div class="c-eye r"></div><div class="c-mouth"></div></div>
            <div class="c-body"></div>
            <div class="c-leg l"></div><div class="c-leg r"></div>
            <div class="c-arm l"></div><div class="c-arm r"></div>
            <div class="c-bubble boy-bubble">SO GOOD!</div>
        </div>
        
        <div class="char char-girl">
            <div class="c-pigtail l"></div><div class="c-pigtail r"></div>
            <div class="c-head"><div class="c-eye l"></div><div class="c-eye r"></div><div class="c-mouth"></div></div>
            <div class="c-body"></div>
            <div class="c-leg l"></div><div class="c-leg r"></div>
            <div class="c-arm l"></div><div class="c-arm r"></div>
            <div class="c-bubble girl-bubble">YUMMY YUMMY!</div>
            <div class="new-burger">🍔</div>
        </div>
        
        <div class="char char-dad">
            <div class="c-head"><div class="c-sunglasses"></div><div class="c-mustache"></div><div class="c-mouth"></div></div>
            <div class="c-body"></div>
            <div class="c-leg l"></div><div class="c-leg r"></div>
            <div class="c-arm l"></div><div class="c-arm r"></div>
            <div class="c-bubble dad-bubble">BEST BURGER EVER!</div>
        </div>
        
        <div class="char char-mom">
            <div class="c-bun"></div>
            <div class="c-head"><div class="c-eye l"></div><div class="c-eye r"></div><div class="c-mouth"></div></div>
            <div class="c-body"></div>
            <div class="c-leg l"></div><div class="c-leg r"></div>
            <div class="c-arm l"></div><div class="c-arm r"></div>
            <div class="c-bubble mom-bubble">PERFECT! 💕</div>
        </div>
        
        <!-- Finale -->
        <div class="finale-text">
            <span class="y">Y</span><span class="u">U</span><span class="m1">M</span><span class="m2">M</span><span class="y2">Y</span><span class="exc">!</span>
            <div class="wow-text">WOW! 🤩</div>
        </div>
        <div class="confetti-container"></div>
        <button class="final-cta">ORDER NOW 🍔</button>
    </section>
"""

with open('index.html', 'r') as f:
    index = f.read()

# Replace .sec-exploded with .sec-story
index = re.sub(r'<section class="sec-exploded">.*?</section>', html_content, index, flags=re.DOTALL)

if '<link rel="stylesheet" href="story.css">' not in index:
    index = index.replace('<link rel="stylesheet" href="contact.css">', '<link rel="stylesheet" href="contact.css">\n    <link rel="stylesheet" href="story.css">')
if '<script src="story.js"></script>' not in index:
    index = index.replace('<script src="contact.js"></script>', '<script src="contact.js"></script>\n    <script src="story.js"></script>')

with open('index.html', 'w') as f:
    f.write(index)

print("Injected story section to index.html")
