
// FLOATING BURGER UNIVERSE LOGIC

document.addEventListener('DOMContentLoaded', () => {
    // 1. Entrance Animations for Letters
    const titleContainer = document.getElementById('u-title');
    if(titleContainer) {
        const text = "EXPLORE OUR MENU";
        titleContainer.innerHTML = '';
        text.split('').forEach((char, i) => {
            if(char === ' ') {
                titleContainer.innerHTML += '<span style="width: 15px;"></span>';
            } else {
                const span = document.createElement('span');
                span.className = 'char';
                span.innerText = char;
                span.style.animation = `dropWord 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) ${i * 0.04}s forwards`;
                titleContainer.appendChild(span);
            }
        });
        titleContainer.innerHTML += '<span class="floating-burger-title">🍔</span>';
        
        // Draw brush stroke after text
        setTimeout(() => {
            const path = document.querySelector('.brush-stroke path');
            if(path) {
                path.style.transition = 'stroke-dashoffset 1.2s ease';
                path.style.strokeDashoffset = '0';
            }
        }, text.length * 40 + 500);
    }
    
    // 2. Entrance Animation for Cards
    const cards = document.querySelectorAll('.u-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                cards.forEach((card, i) => {
                    setTimeout(() => {
                        card.style.opacity = '1';
                        // Keep the alternating rotation logic by removing transform override after fade in
                        // Actually better to handle via CSS class
                        card.classList.add('animate-in');
                    }, i * 120);
                });
                observer.disconnect();
            }
        });
    });
    
    const universeSec = document.getElementById('menu');
    if(universeSec) observer.observe(universeSec);

    // 3. Horizontal Scroll dragging
    const slider = document.querySelector('.universe-cards-container');
    let isDown = false;
    let startX;
    let scrollLeft;

    if(slider) {
        slider.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - slider.offsetLeft;
            scrollLeft = slider.scrollLeft;
        });
        slider.addEventListener('mouseleave', () => { isDown = false; });
        slider.addEventListener('mouseup', () => { isDown = false; });
        slider.addEventListener('mousemove', (e) => {
            if(!isDown) return;
            e.preventDefault();
            const x = e.pageX - slider.offsetLeft;
            const walk = (x - startX) * 2; // scroll-fast
            slider.scrollLeft = scrollLeft - walk;
        });
    }

    // 4. Custom Cursor
    const cursor = document.getElementById('u-cursor');
    if(universeSec && cursor) {
        universeSec.addEventListener('mousemove', (e) => {
            cursor.style.display = 'block';
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
            
            // Trail
            if(Math.random() > 0.5) {
                const trail = document.createElement('div');
                trail.className = 'u-cursor-trail';
                trail.style.left = e.clientX + 'px';
                trail.style.top = e.clientY + 'px';
                document.body.appendChild(trail);
                setTimeout(() => trail.remove(), 500);
            }
        });
        universeSec.addEventListener('mouseleave', () => {
            cursor.style.display = 'none';
        });
        
        // Buttons hover
        document.querySelectorAll('.u-btn-cart, .u-view-more').forEach(btn => {
            btn.addEventListener('mouseenter', () => {
                cursor.innerHTML = '👆';
                cursor.style.textShadow = '0 0 10px red';
            });
            btn.addEventListener('mouseleave', () => {
                cursor.innerHTML = '🍔';
                cursor.style.textShadow = 'none';
            });
        });
    }
});

// Slot machine price effect
function rollPrice(element, finalPrice) {
    if(element.dataset.rolling === 'true') return;
    element.dataset.rolling = 'true';
    
    let ticks = 0;
    const interval = setInterval(() => {
        element.innerText = Math.floor(Math.random() * 900) + 100;
        ticks++;
        if(ticks > 10) {
            clearInterval(interval);
            element.innerText = finalPrice;
            setTimeout(() => { element.dataset.rolling = 'false'; }, 1000);
        }
    }, 50);
}

// Add to Cart Magic
function showToast(message) {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 9999; display: flex; flex-direction: column; gap: 10px;';
        document.body.appendChild(container);
    }
    
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<i class="fa-solid fa-check-circle" style="color: #4CAF50; margin-right: 8px;"></i> ${message}`;
    toast.style.cssText = 'background: white; color: #333; padding: 15px 25px; border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-family: "Montserrat", sans-serif; font-weight: 600; font-size: 1rem; opacity: 0; transform: translateY(-20px); transition: all 0.3s ease; display: flex; align-items: center; border-left: 5px solid #4CAF50;';
    
    container.appendChild(toast);
    
    // Animate in
    requestAnimationFrame(() => {
        toast.style.opacity = '1';
        toast.style.transform = 'translateY(0)';
    });
    
    // Remove after 3 seconds
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(-20px)';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function addUniverseCart(btn, name, price) {
    if(btn.classList.contains('loading')) return;
    
    // Show popup immediately
    showToast(`${name} added to cart!`);
    
    // UI states
    btn.classList.add('clicked');
    setTimeout(() => btn.classList.remove('clicked'), 200);
    
    btn.classList.add('loading');
    
    // Flying Burger Logic
    const card = btn.closest('.u-card');
    const burgerImg = card.querySelector('.u-burger-img');
    const cartIcon = document.querySelector('.cart-icon') || document.querySelector('.fa-cart-shopping');
    
    if(burgerImg && cartIcon) {
        const startRect = burgerImg.getBoundingClientRect();
        const endRect = cartIcon.getBoundingClientRect();
        
        const flying = document.createElement('img');
        flying.src = burgerImg.src;
        flying.className = 'flying-burger';
        flying.style.left = startRect.left + 'px';
        flying.style.top = startRect.top + 'px';
        flying.style.width = startRect.width + 'px';
        document.body.appendChild(flying);
        
        // Animate parabolic arc using cubic-bezier for x and linear for y or vice versa
        // Actually simpler: CSS transitions
        setTimeout(() => {
            flying.style.left = endRect.left + 'px';
            flying.style.top = endRect.top + 'px';
            flying.style.width = '20px';
            flying.style.opacity = '0.5';
            flying.style.transform = 'rotate(360deg)';
        }, 50);
        
        setTimeout(() => {
            flying.remove();
            // Cart icon bounce
            cartIcon.style.transform = 'scale(1.5)';
            setTimeout(() => cartIcon.style.transform = 'scale(1)', 200);
            
            // Proceed to cart
            if (typeof addToCart === 'function') {
                addToCart(name, price); // original function
            }
        }, 1050);
    } else {
        if (typeof addToCart === 'function') {
            addToCart(name, price);
        }
    }
    
    // Button Success
    setTimeout(() => {
        btn.classList.remove('loading');
        btn.classList.add('success');
        btn.innerHTML = '<svg style="width:20px;height:20px" viewBox="0 0 24 24"><path fill="none" stroke="white" stroke-width="3" d="M5 13l4 4L19 7"/></svg> <span style="margin-left:5px">Added!</span>';
        
        setTimeout(() => {
            btn.classList.remove('success');
            btn.innerHTML = '<i class="fa-solid fa-cart-shopping u-btn-icon"></i><span class="u-btn-text">Add to Cart</span>';
        }, 2000);
    }, 800);
}

// 5. Scroll Universe Logic
let currentScrollPos = 0;
function scrollUniverse(direction) {
    const container = document.querySelector('.universe-cards-container');
    const track = document.querySelector('.marquee-track');
    if (!container || !track) return;

    // Stop marquee animation permanently when manual navigation starts
    track.style.animation = 'none';
    
    // Get card width + gap
    const card = track.querySelector('.u-card');
    const cardWidth = card ? card.offsetWidth + 40 : 360; 
    
    if (direction === 'left') {
        container.scrollBy({ left: -cardWidth, behavior: 'smooth' });
    } else {
        container.scrollBy({ left: cardWidth, behavior: 'smooth' });
    }
    
    // Show visual feedback on the buttons
    const btn = document.querySelector(`.u-${direction}`);
    if(btn) {
        btn.style.transform = `translateY(-50%) scale(0.9)`;
        setTimeout(() => btn.style.transform = `translateY(-50%) scale(1)`, 200);
    }
}
