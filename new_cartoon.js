
var timers = [];
var running = false;
var nodInterval = null;
var shakeInterval = null;

function openNewCartoon(burgerName, price) {
    document.getElementById('nc-modal').classList.add('show');
    
    // Update panel text
    var title = burgerName.replace(' ', '\n').toUpperCase();
    document.getElementById('nc-panel-title').innerText = title;
    document.getElementById('nc-price').innerText = '₹' + price + ' Only!';
    
    // Start animation if not running
    if (!running) {
        setTimeout(startAnim, 500);
    }
}

function closeNewCartoon() {
    document.getElementById('nc-modal').classList.remove('show');
    clearAll();
    replayAnim();
}

function T(fn, ms) {
    var id = setTimeout(fn, ms);
    timers.push(id);
}

function clearAll() {
    timers.forEach(function(id) { clearTimeout(id); });
    timers = [];
    if(nodInterval) clearInterval(nodInterval);
    if(shakeInterval) clearInterval(shakeInterval);
}

function step(text, pct) {
    document.getElementById('nc-progress-bar').style.width = pct + '%';
    document.getElementById('nc-step-lbl').innerText = text;
}

function startHeadNod() {
    var avatar = document.getElementById('nc-avatar-wrap');
    var nod = false;
    avatar.style.transition = 'transform 0.35s ease-in-out';
    nodInterval = setInterval(function() {
        nod = !nod;
        avatar.style.transform = nod ? 'rotate(-4deg)' : 'rotate(0deg)';
    }, 700);
}

function stopHeadNod() {
    if(nodInterval) clearInterval(nodInterval);
    var avatar = document.getElementById('nc-avatar-wrap');
    avatar.style.transform = 'rotate(0deg)';
}

function shakeScene() {
    var scene = document.getElementById('nc-scene');
    var positions = [-8, 8, -6, 6, -4, 4, 0];
    var i = 0;
    shakeInterval = setInterval(function() {
        if(i >= positions.length) {
            clearInterval(shakeInterval);
            scene.style.transform = 'translateX(0)';
            return;
        }
        scene.style.transform = 'translateX(' + positions[i] + 'px)';
        i++;
    }, 70);
}

function startAnim() {
    if(running) return;
    running = true;
    
    document.getElementById('nc-click-label').style.display = 'none';
    document.getElementById('nc-burger-area').onclick = null;
    document.getElementById('nc-burger-area').style.cursor = 'default';
    
    var leftPanel = document.getElementById('nc-left-panel');
    var avatarWrap = document.getElementById('nc-avatar-wrap');
    var speech = document.getElementById('nc-speech');
    var lbrow = document.getElementById('lbrow');
    var rbrow = document.getElementById('rbrow');
    var lp = document.getElementById('lp');
    var rp = document.getElementById('rp');
    var mouth = document.getElementById('mouth');
    var burgerArea = document.getElementById('nc-burger-area');
    var reactions = document.getElementById('nc-reactions');
    var replayBtn = document.getElementById('nc-replay-btn');
    
    // Initial Progress
    step("Ready", 5);
    
    // TIMER 1 (200ms)
    T(function() {
        leftPanel.classList.add('show');
    }, 200);
    
    // TIMER 2 (300ms)
    T(function() {
        avatarWrap.classList.add('enter');
        step("Man aa raha hai...", 18);
    }, 300);
    
    // TIMER 3 (1700ms)
    T(function() {
        speech.textContent = "Wow! Burger! 😍";
        speech.classList.add('show');
        lbrow.setAttribute('d', 'M 74 106 Q 90 98 106 104');
        rbrow.setAttribute('d', 'M 134 104 Q 150 98 166 106');
        lp.setAttribute('rx', '7.5'); lp.setAttribute('ry', '7.5');
        rp.setAttribute('rx', '7.5'); rp.setAttribute('ry', '7.5');
        step("Burger dekha! Aankhein phaili!", 32);
    }, 1700);
    
    // TIMER 4 (2800ms)
    T(function() {
        speech.textContent = "Mera burger! 🤤";
        burgerArea.style.transition = 'transform 0.9s cubic-bezier(0.23,1.2,0.32,1), opacity 0.5s';
        burgerArea.style.transform = 'translateX(-200px) translateY(-60px) scale(1.35)';
        mouth.setAttribute('d', 'M 98 185 Q 120 208 142 185');
        step("Haath mein liya! Bada burger!", 47);
    }, 2800);
    
    // TIMER 5 (3700ms)
    T(function() {
        speech.textContent = "Mmmm... 😋 Bahut acha hai!";
        burgerArea.style.transition = 'transform 1.8s ease-in-out, opacity 0.5s';
        burgerArea.style.transform = 'translateX(-200px) translateY(-60px) scale(0.9)';
        startHeadNod();
        step("Kha raha hai... dhire dhire...", 58);
    }, 3700);
    
    // TIMER 6 (5600ms)
    T(function() {
        burgerArea.style.transition = 'transform 2s ease-in-out, opacity 0.5s';
        burgerArea.style.transform = 'translateX(-200px) translateY(-60px) scale(0.5)';
        step("Aur kha raha hai...", 68);
    }, 5600);
    
    // TIMER 7 (7700ms)
    T(function() {
        speech.textContent = "Kha liya! 🎉";
        burgerArea.style.transition = 'transform 1.1s ease-in, opacity 0.5s';
        burgerArea.style.transform = 'translateX(-200px) translateY(-60px) scale(0.05)';
        burgerArea.style.opacity = '0';
        stopHeadNod();
        step("Kha liya!! Burger khatam!", 80);
    }, 7700);
    
    // TIMER 8 (9000ms)
    T(function() {
        speech.classList.remove('show');
        mouth.setAttribute('d', 'M 88 183 Q 120 210 152 183');
        lbrow.setAttribute('d', 'M 74 108 Q 90 100 106 106');
        rbrow.setAttribute('d', 'M 134 106 Q 150 100 166 108');
        lp.setAttribute('cy', '138'); lp.setAttribute('rx', '5'); lp.setAttribute('ry', '5');
        rp.setAttribute('cy', '138'); rp.setAttribute('rx', '5'); rp.setAttribute('ry', '5');
        
        avatarWrap.classList.add('happyBounce');
        reactions.classList.add('show');
        step("WOW! YUMMY! 🎉", 100);
        
        shakeScene();
        
        T(function() { document.getElementById('cs1').classList.add('pop'); }, 100);
        T(function() { document.getElementById('cs3').classList.add('pop'); }, 200);
        T(function() { document.getElementById('cs2').classList.add('pop'); }, 300);
        T(function() { document.getElementById('cs4').classList.add('pop'); }, 400);
    }, 9000);
    
    // TIMER 9 (11500ms)
    T(function() {
        replayBtn.style.display = 'block';
        document.getElementById('nc-step-lbl').innerText = '';
        running = false;
    }, 11500);
}

function replayAnim() {
    clearAll();
    running = false;
    
    document.getElementById('nc-left-panel').classList.remove('show');
    
    var avatarWrap = document.getElementById('nc-avatar-wrap');
    avatarWrap.classList.remove('enter');
    avatarWrap.classList.remove('happyBounce');
    avatarWrap.style.transition = 'none';
    avatarWrap.style.transform = 'none';
    // left reverts to -350px via css remove class
    
    document.getElementById('nc-reactions').classList.remove('show');
    document.getElementById('nc-speech').classList.remove('show');
    
    var stars = document.querySelectorAll('.corner-star');
    for(var i=0; i<stars.length; i++) {
        stars[i].classList.remove('pop');
        // force reflow
        void stars[i].offsetWidth;
    }
    
    var burgerArea = document.getElementById('nc-burger-area');
    burgerArea.style.transition = 'none';
    burgerArea.style.transform = 'translateX(-50%)';
    burgerArea.style.opacity = '1';
    burgerArea.style.cursor = 'pointer';
    burgerArea.onclick = startAnim;
    
    document.getElementById('mouth').setAttribute('d', 'M 98 185 Q 120 200 142 185');
    document.getElementById('lbrow').setAttribute('d', 'M 74 112 Q 90 105 106 110');
    document.getElementById('rbrow').setAttribute('d', 'M 134 110 Q 150 105 166 112');
    var lp = document.getElementById('lp');
    var rp = document.getElementById('rp');
    lp.setAttribute('cy', '135'); lp.setAttribute('rx', '6'); lp.setAttribute('ry', '6');
    rp.setAttribute('cy', '135'); rp.setAttribute('rx', '6'); rp.setAttribute('ry', '6');
    
    document.getElementById('nc-replay-btn').style.display = 'none';
    document.getElementById('nc-click-label').style.display = 'block';
    
    document.getElementById('nc-progress-bar').style.width = '0%';
    document.getElementById('nc-step-lbl').innerText = '';
    
    document.getElementById('nc-scene').style.transform = 'none';
    
    setTimeout(function() {
        // restore transition logic handled by CSS classes generally, but just in case
    }, 100);
}
