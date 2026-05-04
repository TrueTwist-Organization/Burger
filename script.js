gsap.registerPlugin(ScrollTrigger, TextPlugin);

window.scrollTo(0, 0);

// Get all layers
const l1 = document.getElementById('layer-1'); // Top Bun
const l2 = document.getElementById('layer-2'); // Lettuce
const l3 = document.getElementById('layer-3'); // Tomatoes
const l4 = document.getElementById('layer-4'); // Onions
const l5 = document.getElementById('layer-5'); // Pickles
const l6 = document.getElementById('layer-6'); // Cheese
const l7 = document.getElementById('layer-7'); // Patty
const l8 = document.getElementById('layer-8'); // Bottom Bun
window.addEventListener('scroll', () => {
    let current = '';
    
    const sections = document.querySelectorAll('section[id]');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= (sectionTop - sectionHeight / 3)) {
            current = section.getAttribute('id');
        }
    });

    const navLinks = document.querySelectorAll('.nav-link');
    if (current && navLinks.length > 0) {
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') && link.getAttribute('href').includes('#' + current)) {
                link.classList.add('active');
            }
        });
        updateNavIndicator();
    }
});

function updateNavIndicator() {
    const indicator = document.querySelector('.nav-indicator');
    const activeLink = document.querySelector('.nav-link.active');
    
    if (activeLink && indicator) {
        indicator.style.width = activeLink.offsetWidth + 'px';
        indicator.style.left = activeLink.offsetLeft + 'px';
        indicator.style.opacity = '1';
    } else if (indicator) {
        indicator.style.opacity = '0';
    }
}

// Initial position
setTimeout(updateNavIndicator, 100);
window.addEventListener('resize', updateNavIndicator);



// Wait for images to load before setting up ScrollTrigger
window.addEventListener("load", () => {
    
    // Assembled state (tightly packed to look solid)
    const assembledState = {
        l1: { y: 120, scale: 0.95, rotation: 0 },
        l2: { y: 90, scale: 0.98, rotation: 0 },
        l3: { y: 60, scale: 1, rotation: 0 },
        l4: { y: 30, scale: 1, rotation: 0 },
        l5: { y: -10, scale: 0.98, rotation: 0 },
        l6: { y: -40, scale: 0.97, rotation: 0 },
        l7: { y: -70, scale: 0.96, rotation: 0 },
        l8: { y: -100, scale: 0.95, rotation: 0 }
    };

    const isMobile = window.innerWidth <= 900;
    const heroScale = isMobile ? 0.6 : 1;

    // Define elements BEFORE using them
    const l1 = document.getElementById('layer-1');
    const l2 = document.getElementById('layer-2');
    const l3 = document.getElementById('layer-3');
    const l4 = document.getElementById('layer-4');
    const l5 = document.getElementById('layer-5');
    const l6 = document.getElementById('layer-6');
    const l7 = document.getElementById('layer-7');
    const l8 = document.getElementById('layer-8');

    // Squish the hero burger and center it
    if(l1 && l2 && l3 && l4 && l5 && l6 && l7 && l8) {
        gsap.set("#burger-container", { xPercent: -50, x: 0, scale: heroScale });
        gsap.set(l1, assembledState.l1);
        gsap.set(l2, assembledState.l2);
        gsap.set(l3, assembledState.l3);
        gsap.set(l4, assembledState.l4);
        gsap.set(l5, assembledState.l5);
        gsap.set(l6, assembledState.l6);
        gsap.set(l7, assembledState.l7);
        gsap.set(l8, assembledState.l8);
    }

    // Hero Animation Timeline (Removed because middle burger is hidden)
    /*
    const tl_hero = gsap.timeline();
    // ...
    */

    // Timeline 1: Landing Transition
    const tl_transition = gsap.timeline({
        scrollTrigger: {
            trigger: ".sec-landing",
            start: "top top",
            end: "bottom top",
            scrub: 1
        }
    });

    tl_transition.to("#burger-container", {
        scale: 0.5,
        yPercent: -10,
        duration: 1
    });


    // Step 2: Explode (New Horizontal Layout)
    const tl_explode = gsap.timeline({
        scrollTrigger: {
            trigger: ".sec-exploded",
            start: "top top",
            end: "+=800%", // 8 slides
            scrub: 1,
            pin: true
        }
    });

    const layerInfo = [
        { num: "01", name: "TOP BUN", desc: "Golden sesame seed bun, freshly baked daily." },
        { num: "02", name: "LETTUCE", desc: "Crisp iceberg lettuce for that perfect crunch." },
        { num: "03", name: "TOMATOES", desc: "Fresh, juicy farm-picked tomato slices." },
        { num: "04", name: "ONION RINGS", desc: "Sweet and crunchy red onion rings." },
        { num: "05", name: "PICKLES", desc: "Tangy dill pickles for a zesty kick." },
        { num: "06", name: "CHEESE", desc: "Melted cheddar cheese slice." },
        { num: "07", name: "GRILLED PATTY", desc: "100% pure beef patty, flame-grilled to perfection." },
        { num: "08", name: "BOTTOM BUN", desc: "Soft bottom bun toasted with our secret sauce." }
    ];

    const leftContainer = document.getElementById('exploded-left');
    const particles = {};
    const mainImages = {};
    const scatterTargets = {};

    // Generate DOM for Left Container
    for(let i=1; i<=8; i++) {
        const layerKey = `l${i}`;
        particles[layerKey] = [];
        scatterTargets[layerKey] = [];
        const originalSrc = document.getElementById(`layer-${i}`).src;
        
        // The main finalized layer image
        const mainImg = document.createElement('img');
        mainImg.src = originalSrc;
        mainImg.className = 'burger-layer';
        mainImg.style.position = 'absolute';
        mainImg.style.top = '50%';
        mainImg.style.left = '50%';
        mainImg.style.transform = 'translate(-50%, -50%)';
        mainImg.style.width = '80%';
        mainImg.style.height = '80%';
        mainImg.style.objectFit = 'contain';
        mainImg.style.opacity = '0'; // Initially hidden
        mainImg.style.filter = 'drop-shadow(0px 15px 25px rgba(0, 0, 0, 0.3))';
        mainImg.style.zIndex = 9 - i; // Top Bun (1) gets z-index 8, Bottom Bun (8) gets 1
        leftContainer.appendChild(mainImg);
        mainImages[layerKey] = mainImg;

        // The particles for this layer
        for(let j=0; j<5; j++) {
            const p = document.createElement('img');
            p.src = originalSrc;
            p.style.position = 'absolute';
            p.style.top = '50%';
            p.style.left = '50%';
            p.style.width = '80%';
            p.style.height = '80%';
            p.style.objectFit = 'contain';
            p.style.opacity = '0'; // Initially hidden
            p.style.pointerEvents = 'none';
            p.style.transformOrigin = 'center';
            p.style.zIndex = 9 - i;
            leftContainer.appendChild(p);
            particles[layerKey].push(p);

            // Random initial scatter position (off-screen or edges)
            const angle = (Math.PI * 2 * j) / 5 + (Math.random() * 0.5);
            const radius = 600 + Math.random() * 200; 
            scatterTargets[layerKey].push({
                x: Math.cos(angle) * radius,
                y: Math.sin(angle) * radius,
                rotation: (Math.random() - 0.5) * 360,
                scale: 0.3 + Math.random() * 0.3
            });
        }
    }

    // STEPS 1 to 8: ASSEMBLE ONE BY ONE IN THE CENTER
    for(let i=1; i<=8; i++) {
        const startTime = i - 1; // 0, 1, 2...
        const layerKey = `l${i}`;
        const info = layerInfo[i-1];

        // Ensure current particles start at scattered position
        particles[layerKey].forEach((p, idx) => {
            gsap.set(p, { 
                x: scatterTargets[layerKey][idx].x, 
                y: scatterTargets[layerKey][idx].y, 
                xPercent: -50,
                yPercent: -50,
                rotation: scatterTargets[layerKey][idx].rotation, 
                scale: scatterTargets[layerKey][idx].scale,
                opacity: 0
            });
        });

        // 1. Layers keep adding up (no fade-out of previous layer)

        // 2. Text update animation
        tl_explode.to(["#exp-num", "#exp-name", "#exp-desc"], { opacity: 0, y: -20, duration: 0.2 }, startTime)
                  .set("#exp-num", { innerHTML: info.num }, startTime + 0.2)
                  .set("#exp-name", { innerHTML: info.name }, startTime + 0.2)
                  .set("#exp-desc", { innerHTML: info.desc }, startTime + 0.2)
                  .to(["#exp-num", "#exp-name", "#exp-desc"], { opacity: 1, y: 0, duration: 0.3 }, startTime + 0.2);

        // Progress Dots
        const dots = document.querySelectorAll('.exp-dot');
        tl_explode.to(dots[i-1], { backgroundColor: "#E85A1F", scale: 1.3, duration: 0.1 }, startTime + 0.2);
        if(i > 1) {
            tl_explode.to(dots[i-2], { backgroundColor: "#E0D4C3", scale: 1, duration: 0.1 }, startTime + 0.2);
        }

        // 3. Particles fly into center
        const flyDuration = i === 1 ? 0.1 : 0.6; // Top bun flies in almost instantly
        const crossfadeStart = i === 1 ? 0.15 : 0.7; // Crossfade happens earlier for Top Bun

        particles[layerKey].forEach((p, idx) => {
            tl_explode.to(p, { opacity: 1, duration: 0.05 }, startTime);
            tl_explode.to(p, {
                x: 0, y: 0, xPercent: -50, yPercent: -50,
                rotation: 0,
                scale: 1,
                duration: flyDuration,
                ease: "power2.out"
            }, startTime);
        });

        // 4. Crossfade particles to crisp main image at center
        tl_explode.to(particles[layerKey], { opacity: 0, duration: 0.1 }, startTime + crossfadeStart);
        gsap.set(mainImages[layerKey], { x: 0, y: 0, xPercent: -50, yPercent: -50, rotation: 0, scale: 1 });
        tl_explode.to(mainImages[layerKey], { opacity: 1, duration: 0.1 }, startTime + crossfadeStart);
    }


});
window.addEventListener("load", () => {
    // Timeline 2: Menu Items Fly In
    const tl2 = gsap.timeline({
        scrollTrigger: {
            trigger: ".sec-menu-universe",
            start: "top 20%", // Start much later to avoid early fadeout
            toggleActions: "play none play reverse" // Play on enter from both directions
        }
    });

    tl2.to(document.body, { backgroundColor: "#F5ECD7", duration: 1 }, 0)
       .to("#burger-container", { opacity: 0, duration: 0.5 }, 0) // Fade out burger when entering menu
       .fromTo(".u-card", 
           { opacity: 0, y: 150 }, 
           { opacity: 1, y: 0, stagger: 0.1, duration: 1, ease: "back.out(1.5)" }, 0.2)
       .fromTo(".btn-explore", 
           { opacity: 0, scale: 0.8 }, 
           { opacity: 1, scale: 1, duration: 0.5 }, 1);
           
    // Re-calculate positions instantly on resize
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            ScrollTrigger.refresh();
        }, 200);
    });
});

function toggleMenu() {
    const hiddenItems = document.querySelectorAll('.hidden-item');
    const btn = document.getElementById('view-more-btn');
    const btnText = btn.querySelector('.vm-text') || btn;
    
    if (hiddenItems.length > 0) {
        // Show items
        hiddenItems.forEach(item => {
            item.classList.remove('hidden-item');
            item.classList.add('shown-item');
        });
        btnText.innerText = 'VIEW LESS';
    } else {
        // Hide items
        const shownItems = document.querySelectorAll('.shown-item');
        shownItems.forEach(item => {
            item.classList.add('hidden-item');
            item.classList.remove('shown-item');
        });
        btnText.innerText = 'VIEW MORE';
        // Scroll back to menu
        document.getElementById('menu').scrollIntoView({behavior: 'smooth'});
    }
}

// Drag Scroll for Menu Items
document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.menu-items');
    if (!slider) return;
    
    let isDown = false;
    let startX;
    let scrollLeft;

    slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.style.scrollSnapType = 'none'; // disable snap during drag
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });
    slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.style.scrollSnapType = 'x mandatory';
    });
    slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.style.scrollSnapType = 'x mandatory';
    });
    slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 2; // scroll-fast
        slider.scrollLeft = scrollLeft - walk;
    });
});
// Custom Add To Cart with Animations
window.addToCart = function(title, price) {
    const btn = event.currentTarget;
    if (btn.classList.contains('added')) return;
    
    // Create Ripple
    const circle = document.createElement('span');
    const diameter = Math.max(btn.clientWidth, btn.clientHeight);
    const radius = diameter / 2;
    
    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.clientX - btn.getBoundingClientRect().left - radius}px`;
    circle.style.top = `${event.clientY - btn.getBoundingClientRect().top - radius}px`;
    circle.classList.add('ripple');
    
    const ripple = btn.querySelector('.ripple');
    if (ripple) ripple.remove();
    btn.appendChild(circle);
    
    // Add Success State
    btn.classList.add('added');
    
    // Floating +1
    const floatText = document.createElement('div');
    floatText.innerText = '+1';
    floatText.classList.add('float-plus-one');
    floatText.style.left = `${event.clientX}px`;
    floatText.style.top = `${event.clientY - 20}px`;
    document.body.appendChild(floatText);
    
    setTimeout(() => { floatText.remove(); }, 1000);
    setTimeout(() => { btn.classList.remove('added'); }, 2000);
    
    // Call existing cart logic if it exists
    if (typeof cartItems !== 'undefined') {
        cartItems.push({ name: title, price: price });
        localStorage.setItem('burger_cart', JSON.stringify(cartItems));
        if (typeof updateCartDisplay === 'function') updateCartDisplay();
    }
}


