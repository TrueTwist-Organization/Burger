// ━━━ CONTACT UNIVERSE JS ━━━

document.addEventListener('DOMContentLoaded', () => {
    
    // --- Typewriter and Header Animations ---
    const contactTitle = document.getElementById('c-form-title');
    if (contactTitle) {
        const titleText = "GET IN TOUCH";
        contactTitle.innerHTML = '';
        titleText.split('').forEach((char, i) => {
            if (char === ' ') {
                contactTitle.innerHTML += '&nbsp;';
            } else {
                const span = document.createElement('span');
                span.className = 'char';
                span.innerText = char;
                contactTitle.appendChild(span);
            }
        });
    }

    // Scroll Trigger Entrance Animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                
                // Left Panel
                const leftPanel = document.querySelector('.c-left-panel');
                if(leftPanel) {
                    leftPanel.style.transition = 'all 0.8s cubic-bezier(0.34,1.56,0.64,1)';
                    leftPanel.style.opacity = '1';
                    leftPanel.style.transform = 'translateX(0) rotate(0deg)';
                    
                    // Socials stagger
                    setTimeout(() => {
                        document.querySelectorAll('.c-social-btn').forEach((btn, i) => {
                            setTimeout(() => {
                                btn.style.opacity = '1';
                                btn.style.transform = 'translateY(0)';
                            }, i * 100);
                        });
                    }, 500);
                }

                // Right Panel
                const rightPanel = document.querySelector('.c-right-panel');
                if(rightPanel) {
                    rightPanel.style.transition = 'all 0.8s 0.2s cubic-bezier(0.34,1.56,0.64,1)';
                    rightPanel.style.opacity = '1';
                    rightPanel.style.transform = 'translateX(0) rotate(0deg)';

                    // Drop letters
                    setTimeout(() => {
                        const chars = document.querySelectorAll('.c-form-title .char');
                        chars.forEach((char, i) => {
                            char.style.animation = `dropWord 0.5s cubic-bezier(0.34,1.56,0.64,1) ${i * 0.05}s forwards`;
                        });
                        document.querySelector('.c-form-burger').style.animation = `dropWord 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.6s forwards`;
                    }, 500);

                    // Type subtext
                    setTimeout(() => {
                        typewriter('c-form-subtext', "We'd love to hear from you! 🍔", 50);
                    }, 1000);

                    // Fade in inputs staggered
                    setTimeout(() => {
                        document.querySelectorAll('.c-input-group').forEach((grp, i) => {
                            grp.style.transition = 'all 0.5s ease';
                            grp.style.transitionDelay = `${i * 0.1}s`;
                            grp.style.opacity = '1';
                            grp.style.transform = 'translateY(0)';
                        });
                        
                        const btn = document.getElementById('c-btn-submit');
                        if(btn) {
                            btn.style.transition = 'all 0.6s cubic-bezier(0.34,1.56,0.64,1)';
                            btn.style.transitionDelay = '0.4s';
                            btn.style.opacity = '1';
                            btn.style.transform = 'translateY(0)';
                        }
                    }, 600);
                }
                
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    const contactSec = document.getElementById('contact');
    if (contactSec) observer.observe(contactSec);


    // --- Input Validation & Interactions ---
    const nameInput = document.getElementById('c-name');
    const emailInput = document.getElementById('c-email');
    const msgInput = document.getElementById('c-message');

    if (nameInput) {
        nameInput.addEventListener('input', () => {
            const grp = nameInput.closest('.c-input-group');
            if (nameInput.value.trim().length > 2) {
                grp.classList.remove('error');
                grp.classList.add('valid');
            } else {
                grp.classList.remove('valid');
            }
        });
    }

    if (emailInput) {
        emailInput.addEventListener('input', () => {
            const grp = emailInput.closest('.c-input-group');
            const err = document.getElementById('c-email-err');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            
            if (emailInput.value.trim() === '') {
                grp.classList.remove('error', 'valid');
            } else if (emailRegex.test(emailInput.value.trim())) {
                grp.classList.remove('error');
                grp.classList.add('valid');
            } else {
                grp.classList.remove('valid');
                grp.classList.add('error');
                err.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Hmm, check that email 🤔';
            }
        });
        
        emailInput.addEventListener('paste', () => {
            setTimeout(() => {
                const grp = emailInput.closest('.c-input-group');
                if(grp.classList.contains('valid')) {
                    const tooltip = document.createElement('div');
                    tooltip.innerText = "Pasted! ✓";
                    tooltip.style.position = 'absolute';
                    tooltip.style.top = '-25px';
                    tooltip.style.right = '0';
                    tooltip.style.background = '#E67E22';
                    tooltip.style.color = 'white';
                    tooltip.style.padding = '2px 8px';
                    tooltip.style.borderRadius = '4px';
                    tooltip.style.fontSize = '11px';
                    tooltip.style.animation = 'fadeUp 1s forwards';
                    grp.appendChild(tooltip);
                    setTimeout(() => tooltip.remove(), 1000);
                }
            }, 50);
        });
    }

    if (msgInput) {
        const charCount = document.getElementById('c-char-current');
        const charWrap = document.querySelector('.c-char-count');
        
        msgInput.addEventListener('input', () => {
            const grp = msgInput.closest('.c-input-group');
            const len = msgInput.value.length;
            charCount.innerText = len;
            
            if (len > 0) {
                grp.classList.remove('error');
            }
            
            if (len >= 450) charWrap.className = 'c-char-count limit';
            else if (len >= 400) charWrap.className = 'c-char-count warning';
            else charWrap.className = 'c-char-count';
        });
    }


    // --- Form Submit Sequence ---
    const form = document.getElementById('burger-contact-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            let isValid = true;
            
            // Validate all
            const inputs = [nameInput, emailInput, msgInput];
            inputs.forEach(input => {
                const grp = input.closest('.c-input-group');
                if (!input.value.trim()) {
                    grp.classList.add('error', 'shake');
                    setTimeout(() => grp.classList.remove('shake'), 500);
                    isValid = false;
                }
            });

            if(!isValid) {
                showContactToast("Please fill all fields! 🙏");
                return;
            }
            
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if(!emailRegex.test(emailInput.value.trim())) {
                emailInput.closest('.c-input-group').classList.add('error', 'shake');
                setTimeout(() => emailInput.closest('.c-input-group').classList.remove('shake'), 500);
                return;
            }

            // Success Sequence!
            const btn = document.getElementById('c-btn-submit');
            
            // Stage 1: Compress & Ripple
            btn.style.transform = 'scale(0.95)';
            setTimeout(() => { btn.style.transform = ''; }, 150);

            // Stage 2: Loading
            btn.classList.add('loading');
            
            // Mock API delay
            setTimeout(() => {
                // Stage 3: Fly
                btn.classList.remove('loading');
                btn.classList.add('flying');
                
                setTimeout(() => {
                    // Stage 4: Checkmark
                    btn.classList.remove('flying');
                    btn.classList.add('success');
                    
                    // Stage 5: Celebration & Overlay
                    setTimeout(() => {
                        createConfetti(btn);
                        
                        setTimeout(() => {
                            document.getElementById('c-success-overlay').classList.add('active');
                            typewriter('c-success-subtext', "Expected reply within 2 hours 🚀", 40);
                        }, 500);

                    }, 400);

                }, 600); // plane fly duration

            }, 1500); // mock sending duration

        });
    }

});

// Helper: Typewriter
function typewriter(elementId, text, speed) {
    const el = document.getElementById(elementId);
    if(!el) return;
    el.innerHTML = '';
    let i = 0;
    function type() {
        if (i < text.length) {
            el.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    type();
}

// Helper: Toast
function showContactToast(msg) {
    const toast = document.getElementById('c-toast');
    if(!toast) return;
    toast.innerText = msg;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Helper: Confetti
function createConfetti(btn) {
    const colors = ['#E74C3C', '#E67E22', '#FFFDF8', '#27AE60'];
    const rect = btn.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    for (let i = 0; i < 30; i++) {
        const conf = document.createElement('div');
        conf.className = 'c-confetti';
        conf.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        // Random direction
        const angle = Math.random() * Math.PI * 2;
        const velocity = 50 + Math.random() * 100;
        const dx = Math.cos(angle) * velocity;
        const dy = Math.sin(angle) * velocity - 50; // bias upwards
        
        conf.style.setProperty('--dx', `${dx}px`);
        conf.style.setProperty('--dy', `${dy}px`);
        conf.style.left = `${centerX}px`;
        conf.style.top = `${centerY}px`;
        
        document.body.appendChild(conf);
        setTimeout(() => conf.remove(), 1000);
    }
}

// Reset Form
window.resetContactForm = function() {
    const overlay = document.getElementById('c-success-overlay');
    const form = document.getElementById('burger-contact-form');
    const btn = document.getElementById('c-btn-submit');
    
    // 3D Flip overlay away
    overlay.style.transition = 'all 0.6s cubic-bezier(0.25, 0.8, 0.25, 1)';
    overlay.style.transform = 'perspective(1000px) rotateY(90deg)';
    overlay.style.opacity = '0';
    
    setTimeout(() => {
        overlay.classList.remove('active');
        overlay.style.transform = '';
        
        form.reset();
        document.querySelectorAll('.c-input-group').forEach(grp => {
            grp.classList.remove('valid', 'error');
        });
        document.getElementById('c-char-current').innerText = '0';
        document.querySelector('.c-char-count').className = 'c-char-count';
        
        btn.classList.remove('success', 'loading', 'flying');
        document.getElementById('c-success-subtext').innerText = '';
    }, 600);
};

// Fun context menu
document.addEventListener('contextmenu', (e) => {
    if(e.target.closest('#c-form-panel')) {
        // Just a subtle easter egg console log since overriding context menu fully is intrusive
        console.log("🍔 Hungry? Try ordering instead of inspecting!");
    }
});
