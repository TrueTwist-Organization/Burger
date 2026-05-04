with open("style.css", "a") as f:
    f.write("""

/* --- COMPREHENSIVE MOBILE RESPONSIVENESS --- */
@media (max-width: 900px) {
    /* Header & Nav */
    header {
        flex-direction: column;
        padding: 10px 20px;
        gap: 15px;
    }
    nav {
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px !important;
    }
    .nav-link {
        font-size: 0.9rem;
    }
    .icons {
        position: absolute;
        top: 15px;
        right: 20px;
    }

    /* Landing Section */
    .sec-landing h1 {
        font-size: 3rem !important;
        margin-top: 20px;
    }
    .sec-landing p {
        font-size: 1rem !important;
        padding: 0 10px;
    }
    .hero-ctas {
        flex-direction: column;
        gap: 10px;
        align-items: center;
    }
    .burger-container {
        transform: translateX(-50%) scale(0.6) !important;
        bottom: -50px !important;
    }
    .chef-1 {
        width: 150px !important;
        right: -20px !important;
    }

    /* Product Pages */
    h1 {
        font-size: 2.5rem !important;
    }
    #naughty-chef {
        width: 200px !important;
        right: -20px !important;
        bottom: -20px !important;
    }
    #chef-speech {
        font-size: 1rem !important;
        padding: 10px !important;
        right: 0px !important;
        top: -50px !important;
    }

    /* Menu Universe */
    .menu-universe-title {
        font-size: 3rem !important;
    }
    .u-card {
        min-width: 250px !important;
        height: 380px !important;
    }
    .u-img-wrapper {
        height: 160px !important;
    }
    
    /* Cart Modal */
    .cart-flip-container {
        width: 95% !important;
        height: 90vh !important;
        max-height: 700px !important;
    }
}

@media (max-width: 480px) {
    .sec-landing h1 {
        font-size: 2.2rem !important;
    }
    .burger-container {
        transform: translateX(-50%) scale(0.5) !important;
        bottom: 0px !important;
    }
    .u-card {
        min-width: 220px !important;
        height: 350px !important;
    }
    #naughty-chef {
        width: 150px !important;
    }
    #chef-speech {
        font-size: 0.8rem !important;
        top: -40px !important;
    }
}
""")

print("Mobile responsiveness added to style.css!")
