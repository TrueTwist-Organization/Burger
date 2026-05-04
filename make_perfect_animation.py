import re

with open("index.html", "r") as f:
    html = f.read()

# Find the static section
static_section_match = re.search(r'<!-- STATIC INGREDIENTS SECTION \(RESPONSIVE\) -->.*?</section>', html, re.DOTALL)
static_section_html = static_section_match.group(0)

# Remove the static section from the bottom
html = html.replace(static_section_html, "")

# Find the old sec-exploded
old_sec_match = re.search(r'<!-- Fixed Burger Container \(Center\) -->.*?<!-- Section 3: Menu -->', html, re.DOTALL)
old_sec_html = old_sec_match.group(0)

# Replace old sec-exploded with the static section
new_html = html.replace(old_sec_html, static_section_html + "\n\n    <!-- Section 3: Menu -->")

with open("index.html", "w") as f:
    f.write(new_html)

# Now update script.js
with open("script.js", "r") as f:
    js = f.read()

# Remove all old GSAP code related to burger-container
js = re.sub(r'const burgerContainer = document\.getElementById\(\'burger-container\'\);.*?// Wait for images to load before setting up ScrollTrigger', '// Wait for images to load before setting up ScrollTrigger', js, flags=re.DOTALL)

# Update the static section generation to include GSAP animation
old_js_gen = """            labelWrapper.innerHTML = `
                <div class="static-line"></div>
                <span class="static-num">${num}</span>
                <span class="static-sep">|</span>
                <span class="static-name">${item.name}</span>
            `;
            textCol.appendChild(labelWrapper);
        });
    }
});"""

new_js_gen = """            labelWrapper.innerHTML = `
                <div class="static-line"></div>
                <span class="static-num">${num}</span>
                <span class="static-sep">|</span>
                <span class="static-name">${item.name}</span>
            `;
            textCol.appendChild(labelWrapper);
        });

        // Add GSAP Animation for this new section
        const imgs = gsap.utils.toArray('.static-layer-img');
        const labels = gsap.utils.toArray('.static-layer-label');

        // Initial assembled state
        gsap.set(imgs, { top: "50%" });
        gsap.set(labels, { opacity: 0, x: 30 });

        const tl = gsap.timeline({
            scrollTrigger: {
                trigger: "#static-ingredients",
                start: "top top",
                end: "+=350%",
                scrub: 1,
                pin: true
            }
        });

        // Explode sequentially
        imgs.forEach((img, i) => {
            const targetTop = (i / (imgs.length - 1)) * 100 + "%";
            tl.to(img, { top: targetTop, duration: 1 }, i)
              .to(labels[i], { opacity: 1, x: 0, duration: 1 }, i);
        });

        // Hold
        tl.to({}, { duration: 1.5 });

        // Reassemble into full burger
        tl.to(labels, { opacity: 0, x: 30, duration: 0.5 })
          .to(imgs, { top: "50%", duration: 1 }, "<");
    }
});"""

js = js.replace(old_js_gen, new_js_gen)

with open("script.js", "w") as f:
    f.write(js)

print("Updated perfectly!")
