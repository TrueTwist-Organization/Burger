with open("script.js", "r") as f:
    js = f.read()

# Add the animation code before window.addEventListener("load")
bun_animation = """
function animateTopBunEntrance() {
    const burgerContainer = document.getElementById('burger-container');
    const layer1 = document.getElementById('layer-1');
    if (!burgerContainer || !layer1) return;

    // Hide the actual top bun initially
    gsap.set(layer1, { opacity: 0, scale: 0 });

    const numBuns = 20;
    const smallBuns = [];

    // Create small buns
    for (let i = 0; i < numBuns; i++) {
        const bun = document.createElement('img');
        bun.src = 'static_layer1_topbun.png';
        bun.style.position = 'absolute';
        bun.style.width = '80px';
        bun.style.zIndex = '100';
        bun.style.pointerEvents = 'none';
        
        // Random starting positions far away from center
        const angle = Math.random() * Math.PI * 2;
        const radius = 800 + Math.random() * 500;
        const startX = Math.cos(angle) * radius;
        const startY = Math.sin(angle) * radius - 500; // offset a bit higher

        // The center of the top bun inside burger-container
        // burger-container is 600x900. Top bun is near top, let's say y: -200, x: 0 (relative to center since it's an image filling the container)
        // Actually, layer1 is a full size image filling the container, its visual center is near the top.
        
        // Let's just place them randomly in the container
        gsap.set(bun, {
            x: startX,
            y: startY,
            rotation: Math.random() * 360,
            opacity: 0,
            scale: Math.random() * 0.5 + 0.5
        });

        burgerContainer.appendChild(bun);
        smallBuns.push(bun);
    }

    // Animate them flying in
    const tl = gsap.timeline();
    
    tl.to(smallBuns, {
        opacity: 1,
        duration: 0.3,
        stagger: 0.02
    })
    .to(smallBuns, {
        x: 0,
        y: -300, // Approximate visual center of the top bun in the full container
        rotation: 0,
        scale: 0.2,
        duration: 1,
        ease: "power3.in",
        stagger: {
            amount: 0.5,
            from: "random"
        }
    }, "-=0.3")
    .to(smallBuns, {
        opacity: 0,
        duration: 0.1
    })
    .to(layer1, {
        opacity: 1,
        scale: 1,
        duration: 0.8,
        ease: "elastic.out(1, 0.5)",
        onComplete: () => {
            smallBuns.forEach(b => b.remove());
        }
    }, "-=0.1");
}

animateTopBunEntrance();

"""

# Insert before window.addEventListener("load"
js = js.replace('// Wait for images to load before setting up ScrollTrigger', bun_animation + '\n// Wait for images to load before setting up ScrollTrigger')

with open("script.js", "w") as f:
    f.write(js)

print("Added top bun convergence animation!")
