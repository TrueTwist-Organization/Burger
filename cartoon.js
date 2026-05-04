// DOM Elements for Cartoon Animation
let isAnimating = false;
let timers = [];
const totalDuration = 11000;

function openCartoonModal(burgerName, price) {
    const modal = document.getElementById('cartoon-modal');
    document.getElementById('cartoon-panel-title').innerText = burgerName.replace(' ', '\n').toUpperCase();
    document.getElementById('cartoon-price').innerText = '₹' + price + ' Only!';
    
    // reset animation if it was running
    resetAnimation();
    
    modal.classList.add('show');
    
    setTimeout(() => {
        startAnimation();
    }, 500);
}

function closeCartoonModal() {
    document.getElementById('cartoon-modal').classList.remove('show');
    resetAnimation();
}

function setSpeech(text) {
    const bubble = document.getElementById('speech-bubble');
    bubble.innerText = text;
    bubble.classList.add('active');
}

function setProgress(percent, label) {
    document.getElementById('progress-bar').style.width = percent + '%';
    const stepLbl = document.getElementById('step-label');
    stepLbl.innerText = label;
    stepLbl.style.opacity = 1;
}

function startAnimation() {
    if(isAnimating) return;
    isAnimating = true;
    
    const char = document.getElementById('character');
    const panel = document.getElementById('side-panel');
    const bubble = document.getElementById('speech-bubble');
    const burger = document.getElementById('burger-wrapper');
    const clickLbl = document.getElementById('click-label');
    const wow = document.getElementById('wow-text');
    const yummy = document.getElementById('yummy-text');
    const sparkles = document.querySelectorAll('.sparkle');
    const replayBtn = document.getElementById('replay-btn');
    const progBar = document.getElementById('progress-bar');
    const stepLbl = document.getElementById('step-label');
    const charSvg = document.getElementById('char-svg');

    // Hide click label
    if(clickLbl) clickLbl.style.display = 'none';

    // Reset timers array just in case
    timers.forEach(clearTimeout);
    timers = [];

    // Progress tracking
    const startTime = Date.now();
    const progInterval = setInterval(() => {
        let elapsed = Date.now() - startTime;
        if(elapsed > totalDuration) elapsed = totalDuration;
        if(progBar) progBar.style.width = (elapsed / totalDuration * 100) + '%';
        if(elapsed >= totalDuration) clearInterval(progInterval);
    }, 50);
    timers.push(progInterval);

    // STEP 1 & 2: MAN ENTERS & PANEL SLIDES IN
    setProgress(5, "Man & Panel Enter");
    if(char) char.classList.add('active');
    if(panel) panel.classList.add('active');

    // STEP 3: REACT TO BURGER
    timers.push(setTimeout(() => {
        setProgress(20, "Character Reacts");
        setSpeech("Wah! Burger!");
        if(charSvg) {
            charSvg.classList.add('eyes-big');
            charSvg.classList.add('eyebrow-up');
        }
    }, 1500));

    // STEP 4: GRAB BURGER
    timers.push(setTimeout(() => {
        setProgress(35, "Grabbing Burger");
        setSpeech("Maro burger!");
        if(charSvg) {
            charSvg.classList.add('mouth-open');
            charSvg.classList.add('tongue-visible');
        }
        
        // Move burger to hand area (relative to center)
        if(burger) {
            burger.style.transition = 'all 0.8s cubic-bezier(0.23, 1.2, 0.32, 1)';
            burger.style.transform = 'translate(-200px, -150px) scale(1.4)';
        }
    }, 3000));

    // STEP 5: SLOW EATING (Part 1)
    timers.push(setTimeout(() => {
        setProgress(50, "Eating slowly...");
        setSpeech("Khaauuu...");
        if(burger) {
            burger.style.transition = 'all 1.8s linear';
            burger.style.transform = 'translate(-200px, -150px) scale(0.85)';
        }
    }, 4500));

    // STEP 5: SLOW EATING (Part 2)
    timers.push(setTimeout(() => {
        setProgress(65, "Eating more...");
        if(burger) {
            burger.style.transition = 'all 2s linear';
            burger.style.transform = 'translate(-200px, -150px) scale(0.5)';
        }
    }, 6300));

    // STEP 6: BURGER DISAPPEARS
    timers.push(setTimeout(() => {
        setProgress(80, "Finished!");
        setSpeech("Khai lidhu!!");
        if(burger) {
            burger.style.transition = 'all 0.5s ease-in';
            burger.style.transform = 'translate(-200px, -150px) scale(0.08)';
            burger.style.opacity = '0';
        }
        
        if(charSvg) {
            charSvg.classList.remove('mouth-open');
            charSvg.classList.remove('tongue-visible');
        }
    }, 8300));

    // STEP 7: HAPPY REACTION
    timers.push(setTimeout(() => {
        setProgress(90, "Happy Reaction!");
        if(bubble) bubble.classList.remove('active');
        
        if(charSvg) {
            charSvg.classList.remove('eyes-big');
            charSvg.classList.remove('eyebrow-up');
            charSvg.classList.add('eyes-squint');
            charSvg.classList.add('mouth-smile-big');
            charSvg.classList.add('bounce-anim');
        }
        
        if(wow) wow.classList.add('active');
        if(yummy) yummy.classList.add('active');
        sparkles.forEach(s => s.classList.add('active'));
    }, 9200));

    // STEP 8: REPLAY BUTTON
    timers.push(setTimeout(() => {
        setProgress(100, "Done");
        if(replayBtn) replayBtn.classList.add('active');
    }, 10500));
}

function resetAnimation() {
    // Clear any running timers if clicked early
    timers.forEach(clearTimeout);
    timers = [];
    
    isAnimating = false;
    
    const char = document.getElementById('character');
    const panel = document.getElementById('side-panel');
    const bubble = document.getElementById('speech-bubble');
    const burger = document.getElementById('burger-wrapper');
    const clickLbl = document.getElementById('click-label');
    const wow = document.getElementById('wow-text');
    const yummy = document.getElementById('yummy-text');
    const sparkles = document.querySelectorAll('.sparkle');
    const replayBtn = document.getElementById('replay-btn');
    const progBar = document.getElementById('progress-bar');
    const stepLbl = document.getElementById('step-label');
    const charSvg = document.getElementById('char-svg');

    // Reset UI states
    if(char) char.classList.remove('active');
    if(panel) panel.classList.remove('active');
    if(bubble) bubble.classList.remove('active');
    if(wow) wow.classList.remove('active');
    if(yummy) yummy.classList.remove('active');
    sparkles.forEach(s => s.classList.remove('active'));
    if(replayBtn) replayBtn.classList.remove('active');
    
    // Reset character SVG classes
    if(charSvg) charSvg.className.baseVal = ''; // clear all SVG classes
    
    // Reset Burger
    if(burger) {
        burger.style.transition = 'none'; // Snap back
        burger.style.transform = 'translateX(-50%)';
        burger.style.opacity = '1';
    }
    if(clickLbl) clickLbl.style.display = 'block';
    
    // Reset progress
    if(progBar) progBar.style.width = '0%';
    if(stepLbl) stepLbl.style.opacity = '0';
    
    // Restore transition for hover effects after snap
    setTimeout(() => {
        if(burger) burger.style.transition = 'all 0.8s cubic-bezier(0.23, 1.2, 0.32, 1)';
    }, 100);
}
