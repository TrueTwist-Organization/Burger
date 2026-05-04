import os

css_code = """
/* --- STATIC INGREDIENTS RESPONSIVE SECTION --- */
.static-ingredients-section {
    width: 100%;
    min-height: 100vh;
    background-color: #FF5722;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 100px 20px;
    box-sizing: border-box;
    position: relative;
    z-index: 10;
}

.static-ingredients-container {
    display: flex;
    flex-direction: row;
    width: 100%;
    max-width: 1000px;
    height: 800px;
    position: relative;
}

.ingredients-img-col {
    flex: 1;
    position: relative;
    height: 100%;
}

.static-layer-img {
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80%;
    display: flex;
    justify-content: center;
}

.static-layer-img img {
    max-width: 100%;
    /* No max-height so they scale naturally and stay proportional */
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 15px 20px rgba(0,0,0,0.4));
}

.ingredients-text-col {
    flex: 1;
    position: relative;
    height: 100%;
}

.static-layer-label {
    position: absolute;
    left: 0;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
    color: white;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.5rem;
    letter-spacing: 2px;
    white-space: nowrap;
    text-transform: uppercase;
}

.static-line {
    width: 60px;
    height: 2px;
    background-color: white;
    margin-right: 20px;
    position: relative;
}

.static-line::before {
    content: '';
    position: absolute;
    left: -4px;
    top: -4px;
    width: 10px;
    height: 10px;
    background: white;
    border-radius: 50%;
}

.static-num {
    color: #FFD54F;
}

.static-sep {
    color: #FFD54F;
    margin: 0 10px;
    font-weight: 300;
}

.static-name {
    color: white;
    font-weight: bold;
}

@media (max-width: 768px) {
    .static-ingredients-container {
        flex-direction: column;
        height: auto;
        gap: 60px;
    }
    
    .ingredients-img-col, .ingredients-text-col {
        height: 600px;
        width: 100%;
    }
    
    .static-layer-label {
        left: 50%;
        transform: translate(-50%, -50%);
    }
    
    .static-line {
        display: none;
    }
}
"""

with open("style.css", "a") as f:
    f.write(css_code)

js_code = """

// --- STATIC INGREDIENTS SECTION JS ---
document.addEventListener("DOMContentLoaded", () => {
    const staticIngredients = [
        { name: "TOP BUN", img: "static_layer1_topbun.png" },
        { name: "LETTUCE", img: "static_layer2_lettuce.png" },
        { name: "TOMATO SLICES", img: "static_layer3_tomatoes.png" },
        { name: "ONION RINGS", img: "static_layer4_onions.png" },
        { name: "PICKLE SLICES", img: "static_layer5_pickles.png" },
        { name: "CHEESE SLICE", img: "static_layer6_cheese.png" },
        { name: "GRILLED PATTY", img: "static_layer7_patty.png" },
        { name: "BOTTOM BUN", img: "static_layer8_bottombun.png" }
    ];

    const imgCol = document.getElementById('ingredients-img-col');
    const textCol = document.getElementById('ingredients-text-col');

    if(imgCol && textCol) {
        staticIngredients.forEach((item, index) => {
            // Equal spacing calculation
            const percentage = (index / (staticIngredients.length - 1)) * 100;

            // Render Image
            const imgWrapper = document.createElement('div');
            imgWrapper.className = 'static-layer-img';
            imgWrapper.style.top = percentage + '%';
            imgWrapper.innerHTML = `<img src="${item.img}" alt="${item.name}">`;
            imgCol.appendChild(imgWrapper);

            // Render Label
            const num = String(index + 1).padStart(2, '0');
            const labelWrapper = document.createElement('div');
            labelWrapper.className = 'static-layer-label';
            labelWrapper.style.top = percentage + '%';
            labelWrapper.innerHTML = `
                <div class="static-line"></div>
                <span class="static-num">${num}</span>
                <span class="static-sep">|</span>
                <span class="static-name">${item.name}</span>
            `;
            textCol.appendChild(labelWrapper);
        });
    }
});
"""

with open("script.js", "a") as f:
    f.write(js_code)

print("Injected CSS and JS successfully.")
