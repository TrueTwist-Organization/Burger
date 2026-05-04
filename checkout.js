let currentStep = 1;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const isGuest = urlParams.get('guest') === 'true';
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
    
    if (isGuest || isLoggedIn) {
        document.getElementById('step-1').classList.remove('active');
        document.getElementById('step-2').classList.add('active');
        updateProgress(2);
        typeWriter("Where should we deliver? 📍", "address-h2", 80);
    } else {
        // Typewriter effects
        typeWriter("Welcome Back! 👋", "welcome-h2", 100);
        
        // Setup login events
        document.getElementById('btn-show-login').addEventListener('click', () => {
            document.getElementById('login-actions').classList.add('hidden');
            const form = document.getElementById('login-form');
            form.classList.remove('hidden');
            form.style.animation = 'slideInRight 0.4s ease forwards';
        });
    }
    
    // Render the cart summary with actual items and ₹ symbol
    renderCheckoutSummary();
});

function typeWriter(text, elementId, speed) {
    let i = 0;
    document.getElementById(elementId).innerHTML = '';
    function type() {
        if (i < text.length) {
            document.getElementById(elementId).innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    type();
}

function togglePwd() {
    const pwd = document.getElementById('password');
    const icon = document.querySelector('.toggle-pwd');
    if (pwd.type === 'password') {
        pwd.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        pwd.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

function attemptLogin() {
    const pwd = document.getElementById('password').value;
    const form = document.getElementById('login-form');
    const chef = document.getElementById('chef-reaction');
    
    if (pwd === '') {
        form.classList.add('shake');
        document.querySelectorAll('#login-form input').forEach(i => i.classList.add('error-border'));
        chef.innerHTML = '😤';
        setTimeout(() => {
            form.classList.remove('shake');
            document.querySelectorAll('#login-form input').forEach(i => i.classList.remove('error-border'));
        }, 500);
        return;
    }
    
    // Success
    chef.innerHTML = '👍';
    document.getElementById('btn-login-submit').innerHTML = '<i class="fa-solid fa-check"></i>';
    document.getElementById('btn-login-submit').style.backgroundColor = 'var(--green)';
    
    fireConfetti();
    
    setTimeout(() => {
        goToStep(2);
    }, 1000);
}

function goToStep(step) {
    if(step === 2) {
        // Transition 1 -> 2: Paper Turn
        const curr = document.getElementById('step-1');
        const next = document.getElementById('step-2');
        curr.classList.add('paper-turn-out');
        setTimeout(() => {
            curr.classList.remove('active', 'paper-turn-out');
            next.classList.add('active', 'paper-turn-in');
            setTimeout(() => next.classList.remove('paper-turn-in'), 600);
            updateProgress(2);
            typeWriter("Where should we deliver? 📍", "address-h2", 80);
        }, 300);
    } 
    else if (step === 3) {
        // Transition 2 -> 3: Blind Wipe
        const curr = document.getElementById('step-2');
        const next = document.getElementById('step-3');
        const blind = document.getElementById('trans-blind');
        
        blind.classList.add('active');
        
        setTimeout(() => {
            curr.classList.remove('active');
            next.classList.add('active');
            updateProgress(3);
        }, 300);
        
        setTimeout(() => {
            blind.classList.remove('active');
        }, 1000);
    }
    else if (step === 4) {
        // Transition 3 -> 4: Zoom burst
        const curr = document.getElementById('step-3');
        const next = document.getElementById('step-4');
        const zoom = document.getElementById('trans-zoom');
        
        zoom.classList.add('active');
        
        setTimeout(() => {
            curr.classList.remove('active');
            next.classList.add('active');
            updateProgress(4);
            typeWriter("Your burger is on its way!", "success-sub", 50);
            setTimeout(fireMassiveConfetti, 300);
        }, 400);
        
        setTimeout(() => {
            zoom.classList.remove('active');
        }, 800);
    }
}

function updateProgress(step) {
    document.getElementById(`ind-${currentStep}`).classList.remove('active');
    document.getElementById(`ind-${currentStep}`).classList.add('completed');
    
    currentStep = step;
    
    document.getElementById(`ind-${step}`).classList.add('active');
    
    const fillWidth = ((step - 1) / 3) * 100;
    document.getElementById('progress-fill').style.width = `${fillWidth}%`;
}

// Step 2 Logic
function validatePincode(el) {
    const tick = document.getElementById('valid-pincode');
    if (el.value.length === 6 && !isNaN(el.value)) {
        tick.classList.remove('hidden');
    } else {
        tick.classList.add('hidden');
    }
}

function validateAddressAndProceed() {
    const btn = document.getElementById('btn-deliver');
    btn.classList.add('btn-loading');
    
    setTimeout(() => {
        btn.classList.remove('btn-loading');
        goToStep(3);
    }, 1500);
}

// Step 3 Logic
function selectPayment(method) {
    document.querySelectorAll('.pay-card').forEach(c => c.classList.remove('selected'));
    document.querySelector(`.pay-card[data-method="${method}"]`).classList.add('selected');
    document.getElementById('payment-methods').classList.add('has-selection');
    
    document.querySelectorAll('.pay-ui').forEach(ui => ui.classList.add('hidden'));
    
    if(method === 'card') {
        document.getElementById('pay-card-ui').classList.remove('hidden');
    } else if (method === 'upi') {
        document.getElementById('pay-upi-ui').classList.remove('hidden');
    } else if (method === 'cod') {
        document.getElementById('pay-cod-ui').classList.remove('hidden');
    }
}

function updateCardVisual(el) {
    let val = el.value.replace(/\s+/g, '');
    let formatted = val.match(/.{1,4}/g)?.join(' ') || '#### #### #### ####';
    if(val.length === 0) formatted = '#### #### #### ####';
    document.getElementById('cc-number-display').innerText = formatted;
    
    if(val.startsWith('4')) document.getElementById('cc-logo').innerText = 'Visa';
    else if(val.startsWith('5')) document.getElementById('cc-logo').innerText = 'Mastercard';
    else document.getElementById('cc-logo').innerText = 'Card';
}

function placeOrder() {
    const btn = document.getElementById('btn-place-order');
    btn.innerHTML = 'Processing... 🍔';
    btn.style.animation = 'compressFill 2s forwards';
    
    setTimeout(() => {
        btn.innerHTML = '<i class="fa-solid fa-check"></i> SUCCESS';
        setTimeout(() => {
            goToStep(4);
        }, 500);
    }, 2000);
}

// Step 4 Logic
function danceBoy() {
    const boy = document.getElementById('delivery-boy');
    boy.style.animation = 'none';
    void boy.offsetWidth; // trigger reflow
    boy.style.animation = 'shake 0.5s';
    
    const msg = document.getElementById('boy-msg');
    msg.classList.add('show');
    setTimeout(() => msg.classList.remove('show'), 2000);
}

// Confetti logic
function fireConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const colors = ['#C0392B', '#E67E22', '#FFF8F0', '#F1C40F'];
    
    for(let i=0; i<50; i++) {
        particles.push({
            x: canvas.width/2, y: canvas.height/2,
            r: Math.random() * 6 + 2,
            dx: Math.random() * 10 - 5,
            dy: Math.random() * -10 - 5,
            color: colors[Math.floor(Math.random() * colors.length)]
        });
    }
    
    function animate() {
        ctx.clearRect(0,0,canvas.width,canvas.height);
        let active = false;
        particles.forEach(p => {
            p.x += p.dx;
            p.y += p.dy;
            p.dy += 0.3; // gravity
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
            ctx.fillStyle = p.color;
            ctx.fill();
            if(p.y < canvas.height) active = true;
        });
        if(active) requestAnimationFrame(animate);
        else ctx.clearRect(0,0,canvas.width,canvas.height);
    }
    animate();
}

function fireMassiveConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const colors = ['#C0392B', '#E67E22', '#F1C40F', '#27AE60', '#FFF8F0'];
    
    for(let i=0; i<150; i++) {
        particles.push({
            x: canvas.width/2, y: canvas.height/2,
            r: Math.random() * 8 + 3,
            dx: Math.random() * 20 - 10,
            dy: Math.random() * -20 - 5,
            color: colors[Math.floor(Math.random() * colors.length)]
        });
    }
    
    function animate() {
        ctx.clearRect(0,0,canvas.width,canvas.height);
        let active = false;
        particles.forEach(p => {
            p.x += p.dx;
            p.y += p.dy;
            p.dy += 0.2; // gravity
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
            ctx.fillStyle = p.color;
            ctx.fill();
            if(p.y < canvas.height) active = true;
        });
        if(active) requestAnimationFrame(animate);
        else ctx.clearRect(0,0,canvas.width,canvas.height);
    }
    animate();
}

// --- Track Order Modal Logic ---
function openTrackModal() {
    const modal = document.getElementById('track-modal');
    modal.classList.remove('hidden');
    modal.classList.add('active');
    
    // Animate the route path active stroke
    gsap.fromTo("#route-path-active", 
        { strokeDashoffset: 1000 },
        { strokeDashoffset: 0, duration: 8, ease: "power1.inOut" }
    );
    
    // Animate the scooter along the path
    gsap.to("#scooter-obj", {
        motionPath: {
            path: "#route-path",
            align: "#route-path",
            alignOrigin: [0.5, 0.5],
            autoRotate: false
        },
        duration: 8,
        ease: "power1.inOut",
        onUpdate: function() {
            const progress = this.progress();
            const statusText = document.getElementById('live-status-text');
            const etaText = document.getElementById('live-eta');
            
            if(progress < 0.2) {
                statusText.innerText = "Heading to Restaurant... 🏍️";
            } else if (progress < 0.4) {
                statusText.innerText = "Picking up your order... 🍔";
                etaText.innerText = "18 mins";
            } else if (progress < 0.8) {
                statusText.innerText = "On the way to you! 🚀";
                etaText.innerText = "10 mins";
            } else if (progress > 0.95) {
                statusText.innerText = "Arrived! Please collect your order 🎉";
                etaText.innerText = "Arrived";
            }
        }
    });
}

function closeTrackModal() {
    const modal = document.getElementById('track-modal');
    modal.classList.remove('active');
    setTimeout(() => {
        modal.classList.add('hidden');
        // Reset animations
        gsap.killTweensOf("#route-path-active");
        gsap.killTweensOf("#scooter-obj");
    }, 300);
}

// Render dynamic checkout summary
function renderCheckoutSummary() {
    const cartItems = JSON.parse(localStorage.getItem('burger_cart')) || [];
    const summaryItemsDiv = document.querySelector('.summary-items');
    const totalSpan = document.querySelector('.total-price');
    
    if(!summaryItemsDiv || !totalSpan) return;
    
    summaryItemsDiv.innerHTML = '';
    let subtotal = 0;
    
    if(cartItems.length === 0) {
        summaryItemsDiv.innerHTML = '<div class="s-item">Cart is empty</div>';
        totalSpan.innerText = '₹0';
        return;
    }
    
    cartItems.forEach(item => {
        let q = item.qty || 1;
        subtotal += item.price * q;
        summaryItemsDiv.innerHTML += `<div class="s-item"><span class="thumb">🍔</span> <span style="flex:1; text-align:left; margin:0 10px;">${item.name} x${q}</span> <span style="font-weight:600;">₹${item.price * q}</span></div>`;
    });
    
    let delivery = subtotal >= 499 ? 0 : 40;
    let total = subtotal + delivery;
    
    if (delivery > 0) {
        summaryItemsDiv.innerHTML += `<div class="s-item" style="color: #666; font-size: 0.9em;"><span class="thumb">🛵</span> <span style="flex:1; text-align:left; margin:0 10px;">Delivery</span> <span>₹${delivery}</span></div>`;
    } else {
        summaryItemsDiv.innerHTML += `<div class="s-item" style="color: #27AE60; font-size: 0.9em;"><span class="thumb">🛵</span> <span style="flex:1; text-align:left; margin:0 10px;">Delivery</span> <span>FREE</span></div>`;
    }
    
    totalSpan.innerText = '₹' + total;
}
