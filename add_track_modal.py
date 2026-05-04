import re

with open("checkout.html", "r") as f:
    html = f.read()

# Add onclick to button
old_btn = r'<button class="btn btn-primary btn-bounce" style="animation-delay: 1s">TRACK ORDER</button>'
new_btn = r'<button class="btn btn-primary btn-bounce" style="animation-delay: 1s" onclick="openTrackModal()">TRACK ORDER</button>'
html = re.sub(old_btn, new_btn, html)

track_modal_html = """
    <!-- Track Order Modal -->
    <div id="track-modal" class="track-modal-overlay hidden">
        <div class="track-modal-content slide-up-card">
            <span class="close-track-btn" onclick="closeTrackModal()"><i class="fa-solid fa-xmark"></i></span>
            <h2 style="font-family: 'Playfair Display', serif; color: #E85A1F; margin-bottom: 20px;">Live Tracking 📍</h2>
            
            <div class="map-placeholder-large">
                <!-- An animated SVG road -->
                <svg viewBox="0 0 400 200" class="road-svg">
                    <path id="route-path" fill="none" stroke="#ddd" stroke-width="8" stroke-dasharray="15 15" stroke-linecap="round" d="M 40 100 Q 150 20 250 120 T 360 100"/>
                    <path id="route-path-active" fill="none" stroke="#E85A1F" stroke-width="8" stroke-dasharray="1000" stroke-dashoffset="1000" stroke-linecap="round" d="M 40 100 Q 150 20 250 120 T 360 100"/>
                    
                    <circle cx="40" cy="100" r="12" fill="#FFC107" stroke="white" stroke-width="4"/>
                    <text x="25" y="140" font-size="14" font-weight="bold" fill="#555">Store</text>
                    
                    <circle cx="360" cy="100" r="12" fill="#4CAF50" stroke="white" stroke-width="4"/>
                    <text x="340" y="140" font-size="14" font-weight="bold" fill="#555">Home</text>
                    
                    <foreignObject id="scooter-obj" x="15" y="65" width="50" height="50">
                        <div style="font-size: 35px; filter: drop-shadow(0px 5px 5px rgba(0,0,0,0.3));">🛵</div>
                    </foreignObject>
                </svg>
            </div>
            
            <div class="status-texts">
                <h3 id="live-status-text" style="color: #333; margin-top: 10px;">Heading to Restaurant...</h3>
                <div class="track-eta-box">
                    <i class="fa-regular fa-clock"></i> <span>Arriving in <strong id="live-eta">25 mins</strong></span>
                </div>
            </div>
            
            <div class="delivery-partner">
                <div class="dp-avatar">👦</div>
                <div class="dp-info">
                    <h4 style="margin: 0; color: #333;">Rahul Singh</h4>
                    <p style="margin: 5px 0 0; color: #777; font-size: 0.9rem;">⭐ 4.8 • Delivery Partner</p>
                </div>
                <button class="call-btn"><i class="fa-solid fa-phone"></i></button>
            </div>
        </div>
    </div>

    <!-- Global Confetti Canvas -->"""

html = html.replace('    <!-- Global Confetti Canvas -->', track_modal_html)

with open("checkout.html", "w") as f:
    f.write(html)

# Now update checkout.css
with open("checkout.css", "a") as f:
    f.write("""
/* --- Track Modal Styles --- */
.track-modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(5px);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
}
.track-modal-overlay.active {
    opacity: 1;
    pointer-events: all;
}
.track-modal-content {
    background: #FFF8E1;
    width: 90%;
    max-width: 500px;
    border-radius: 20px;
    padding: 30px;
    position: relative;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    transform: translateY(50px);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.track-modal-overlay.active .track-modal-content {
    transform: translateY(0);
}
.close-track-btn {
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 1.5rem;
    color: #999;
    cursor: pointer;
    transition: color 0.3s;
}
.close-track-btn:hover {
    color: #E85A1F;
}
.map-placeholder-large {
    background: #e8f4f8;
    border-radius: 15px;
    overflow: hidden;
    position: relative;
    border: 2px solid #daeef5;
    margin-bottom: 20px;
}
.road-svg {
    width: 100%;
    height: auto;
    display: block;
}
.track-eta-box {
    display: inline-block;
    background: #E85A1F;
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    font-weight: 500;
    margin-top: 10px;
    box-shadow: 0 5px 15px rgba(232, 90, 31, 0.3);
}
.delivery-partner {
    display: flex;
    align-items: center;
    background: white;
    padding: 15px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    border: 1px solid #eee;
}
.dp-avatar {
    width: 50px;
    height: 50px;
    background: #f0f0f0;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.8rem;
    margin-right: 15px;
    border: 2px solid #FFC107;
}
.dp-info {
    flex: 1;
}
.call-btn {
    background: #4CAF50;
    color: white;
    border: none;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    font-size: 1.2rem;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(76, 175, 80, 0.3);
    transition: transform 0.2s, box-shadow 0.2s;
}
.call-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 20px rgba(76, 175, 80, 0.4);
}
""")

print("Updated HTML and CSS")
