document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Word by Word text reveal setup
    const revealTexts = document.querySelectorAll('.reveal-text');
    revealTexts.forEach(p => {
        const words = p.innerText.split(' ');
        p.innerHTML = '';
        words.forEach((word, index) => {
            const span = document.createElement('span');
            span.innerText = word;
            span.style.transitionDelay = `${index * 0.03}s`;
            p.appendChild(span);
            p.appendChild(document.createTextNode(' '));
        });
    });

    // 2. Intersection Observer for standard reveals
    const observerOptions = {
        threshold: 0.2,
        rootMargin: "0px 0px -50px 0px"
    };

    const storyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                
                // If it's a chapter, trigger text reveal
                if (entry.target.classList.contains('story-chapter')) {
                    entry.target.querySelector('.reveal-text').classList.add('is-revealed');
                }

                // If it's the timeline, trigger line draw
                if (entry.target.id === 'timeline-trigger') {
                    setTimeout(() => {
                        document.getElementById('timeline-fill').style.width = '100%';
                    }, 500); // delay until container animates in
                }
            }
        });
    }, observerOptions);

    document.querySelectorAll('.io-trigger').forEach(el => {
        storyObserver.observe(el);
    });

    // 3. Stats Counter Logic
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const numberElements = entry.target.querySelectorAll('.stat-number');
                numberElements.forEach(el => {
                    const target = parseFloat(el.getAttribute('data-target'));
                    const decimals = parseInt(el.getAttribute('data-decimals')) || 0;
                    const duration = 2000; // 2 seconds
                    const start = 0;
                    let startTime = null;

                    function animate(currentTime) {
                        if (!startTime) startTime = currentTime;
                        const progress = Math.min((currentTime - startTime) / duration, 1);
                        // Easing out function
                        const easeProgress = 1 - Math.pow(1 - progress, 3);
                        const currentVal = start + (target - start) * easeProgress;
                        
                        if (decimals > 0) {
                            el.innerText = currentVal.toFixed(decimals);
                        } else {
                            // Add commas for large numbers
                            el.innerText = Math.floor(currentVal).toLocaleString();
                        }

                        if (progress < 1) {
                            requestAnimationFrame(animate);
                        } else {
                            if (decimals > 0) el.innerText = target.toFixed(decimals);
                            else el.innerText = target.toLocaleString();
                        }
                    }
                    requestAnimationFrame(animate);
                });
                // Unobserve after running once
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const statsRow = document.getElementById('stats-counter-trigger');
    if (statsRow) statsObserver.observe(statsRow);

    // 4. Chef Interactions
    const chefWrapper = document.getElementById('story-chef');
    const chefBubble = document.getElementById('chef-speech');
    
    if (chefWrapper && chefBubble) {
        chefWrapper.addEventListener('click', () => {
            chefBubble.classList.add('show');
            setTimeout(() => {
                chefBubble.classList.remove('show');
            }, 3000);
        });
    }

    // 5. Parallax Effects
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        const storySection = document.getElementById('story');
        
        if (!storySection) return;
        
        const rect = storySection.getBoundingClientRect();
        
        // Only run parallax if section is in viewport
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            const relativeY = rect.top; // Negative when scrolling past
            
            // Blobs move slightly
            const blobOrange = document.querySelector('.blob-orange');
            const blobRed = document.querySelector('.blob-red');
            if (blobOrange) blobOrange.style.transform = `translateY(${relativeY * -0.1}px)`;
            if (blobRed) blobRed.style.transform = `translateY(${relativeY * -0.15}px)`;
            
            // Chef floats slightly slower than scroll
            if (chefWrapper) {
                chefWrapper.style.transform = `translateY(${relativeY * -0.05}px)`;
            }
            
            // Watermark rotates based on scroll
            const watermark = document.querySelector('.story-watermark img');
            if (watermark) {
                watermark.style.transform = `rotate(${relativeY * 0.05}deg)`;
            }
        }
    });

    // 6. Chapter Hover Micro-interactions
    const chapters = document.querySelectorAll('.story-chapter');
    chapters.forEach(chapter => {
        chapter.addEventListener('mouseenter', () => {
            const icon = chapter.querySelector('.chapter-icon');
            if(icon) {
                icon.style.transform = 'scale(1.2) translateY(-10px) rotate(5deg)';
                setTimeout(() => {
                    if(chapter.matches(':hover')) {
                         icon.style.transform = 'scale(1.1) translateY(-5px) rotate(0deg)';
                    }
                }, 300);
            }
        });
        chapter.addEventListener('mouseleave', () => {
            const icon = chapter.querySelector('.chapter-icon');
            if(icon) {
                icon.style.transform = 'scale(1) translateY(0) rotate(0deg)';
            }
        });
    });
});
