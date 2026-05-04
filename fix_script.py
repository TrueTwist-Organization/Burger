import re

with open("script.js", "r") as f:
    js = f.read()

# 1. Fix tl_transition (remove opacity: 0)
old_transition = """    tl_transition.to("#burger-container", {
        scale: 0.8,
        yPercent: -10,
        opacity: 0,
        duration: 1
    });"""
new_transition = """    tl_transition.to("#burger-container", {
        scale: 0.8,
        yPercent: -10,
        duration: 1
    });"""
js = js.replace(old_transition, new_transition)

# 2. Add tl_explode before window.addEventListener("load", () => { // Timeline 2
tl_explode_code = """
    // Step 2: Explode
    const tl_explode = gsap.timeline({
        scrollTrigger: {
            trigger: ".sec-exploded",
            start: "top top",
            end: "+=200%", // pin for longer
            scrub: 1,
            pin: true
        }
    });

    const l1 = "#layer-1";
    const l2 = "#layer-2";
    const l3 = "#layer-3";
    const l4 = "#layer-4";
    const l5 = "#layer-5";
    const l6 = "#layer-6";
    const l7 = "#layer-7";
    const l8 = "#layer-8";

    // Exploded state
    const explodedState = {
        l1: { yPercent: -180, scale: 1.1, rotation: 10 },
        l2: { yPercent: -130, scale: 1.05, rotation: -5 },
        l3: { yPercent: -80, scale: 1, rotation: 5 },
        l4: { yPercent: -30, scale: 1, rotation: -3 },
        l5: { yPercent: 20, scale: 1, rotation: 3 },
        l6: { yPercent: 70, scale: 1.02, rotation: -2 },
        l7: { yPercent: 120, scale: 1.05, rotation: 0 },
        l8: { yPercent: 170, scale: 1.1, rotation: -5 }
    };

    // Assembled state
    const assembledState = {
        l1: { yPercent: 28, scale: 0.95, rotation: 0 },
        l2: { yPercent: 12, scale: 0.98, rotation: 0 },
        l3: { yPercent: 6, scale: 1, rotation: 0 },
        l4: { yPercent: -4, scale: 1, rotation: 0 },
        l5: { yPercent: -8, scale: 0.98, rotation: 0 },
        l6: { yPercent: -14, scale: 0.97, rotation: 0 },
        l7: { yPercent: -20, scale: 0.96, rotation: 0 },
        l8: { yPercent: -28, scale: 0.95, rotation: 0 }
    };

    // Initial state (squished)
    gsap.set(l1, assembledState.l1);
    gsap.set(l2, assembledState.l2);
    gsap.set(l3, assembledState.l3);
    gsap.set(l4, assembledState.l4);
    gsap.set(l5, assembledState.l5);
    gsap.set(l6, assembledState.l6);
    gsap.set(l7, assembledState.l7);
    gsap.set(l8, assembledState.l8);

    // The animation:
    tl_explode.to("#burger-container", {
        x: "-20vw", // move left
        duration: 1
    }, 0)
    .to(l1, { ...explodedState.l1, duration: 1 }, 0)
    .to(l2, { ...explodedState.l2, duration: 1 }, 0)
    .to(l3, { ...explodedState.l3, duration: 1 }, 0)
    .to(l4, { ...explodedState.l4, duration: 1 }, 0)
    .to(l5, { ...explodedState.l5, duration: 1 }, 0)
    .to(l6, { ...explodedState.l6, duration: 1 }, 0)
    .to(l7, { ...explodedState.l7, duration: 1 }, 0)
    .to(l8, { ...explodedState.l8, duration: 1 }, 0)
    .to("#attractive-text", { opacity: 1, x: 0, duration: 1 }, 0);

    // Step 3: Reassemble
    tl_explode.to("#attractive-text", { opacity: 0, x: 30, duration: 0.5 })
       .to(l1, { ...assembledState.l1, duration: 1 }, "<")
       .to(l2, { ...assembledState.l2, duration: 1 }, "<")
       .to(l3, { ...assembledState.l3, duration: 1 }, "<")
       .to(l4, { ...assembledState.l4, duration: 1 }, "<")
       .to(l5, { ...assembledState.l5, duration: 1 }, "<")
       .to(l6, { ...assembledState.l6, duration: 1 }, "<")
       .to(l7, { ...assembledState.l7, duration: 1 }, "<")
       .to(l8, { ...assembledState.l8, duration: 1 }, "<")
       .to("#burger-container", { x: "0vw", duration: 1 }, "<");
"""

if 'tl_explode' not in js:
    # Insert before the end of window load event that contains tl_transition
    # Wait, tl_transition is inside its own load event.
    # The end is "    });\n});"
    # We can just append it inside the first load event.
    replace_target = """    tl_transition.to("#burger-container", {
        scale: 0.8,
        yPercent: -10,
        duration: 1
    });"""
    js = js.replace(replace_target, replace_target + "\n" + tl_explode_code)

with open("script.js", "w") as f:
    f.write(js)

print("script.js fixed!")
