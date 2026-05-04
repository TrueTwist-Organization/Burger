
# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

user_css = """
/* --- Clean Menu Styling --- */
:root {
    --primary-color: #E85A1F; /* Adapted to match theme */
    --background-color: transparent;
    --text-dark: #333;
    --text-light: #666;
    --shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.menu-container {
    display: flex;
    flex-direction: row;
    gap: 30px;
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
    justify-content: center;
    flex-wrap: wrap;
    position: relative;
    z-index: 5;
}

.burger-card {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: var(--shadow);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    width: calc(33% - 20px);
    min-width: 280px;
    max-width: 320px;
}

.burger-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.burger-image-placeholder {
    height: 220px;
    background-color: #f5f5f5;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding: 20px;
}

.burger-image-placeholder img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.burger-card:hover .burger-image-placeholder img {
    transform: scale(1.1) rotate(2deg);
}

.burger-details {
    padding: 20px;
    flex-grow: 1;
}

.burger-title {
    font-size: 1.6em;
    color: var(--text-dark);
    margin-top: 0;
    margin-bottom: 10px;
    font-family: 'Playfair Display', serif;
}

.burger-description {
    font-size: 0.95em;
    color: var(--text-light);
    margin-bottom: 15px;
    line-height: 1.5;
}

.burger-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.price {
    font-size: 1.5em;
    font-weight: 900;
    color: var(--primary-color);
}

.card-footer {
    padding: 20px;
    border-top: 1px solid #eee;
    text-align: right;
}

.add-button {
    background-color: var(--primary-color);
    color: white;
    border: none;
    padding: 12px 30px;
    font-size: 1.1em;
    font-weight: 700;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
    width: 100%;
}

.add-button:hover {
    background-color: #C0392B;
    transform: translateY(-2px);
}

.add-button:active {
    transform: translateY(0);
}
"""

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + "\n" + user_css)

print("Updated CSS.")
