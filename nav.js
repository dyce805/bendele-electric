/**
 * Bendele Electric - Main Navigation Script
 * Handles mobile menu toggle functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    const mobileToggle = document.querySelector('.nav__mobile-toggle');
    const navMenu = document.querySelector('.nav__menu');
    
    if (mobileToggle && navMenu) {
        // Toggle mobile menu
        mobileToggle.addEventListener('click', function() {
            const isOpen = navMenu.classList.toggle('nav__menu--open');
            mobileToggle.classList.toggle('nav__mobile-toggle--active', isOpen);
            
            // Update aria-expanded for accessibility
            mobileToggle.setAttribute('aria-expanded', isOpen);
            
            // Update icon (hamburger to X)
            const icon = mobileToggle.querySelector('.nav__mobile-icon');
            if (icon) {
                if (isOpen) {
                    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>';
                } else {
                    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
                }
            }
        });
        
        // Close menu when clicking a link
        navMenu.querySelectorAll('.nav__link, .nav__cta').forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('nav__menu--open');
                mobileToggle.classList.remove('nav__mobile-toggle--active');
                mobileToggle.setAttribute('aria-expanded', 'false');
                
                const icon = mobileToggle.querySelector('.nav__mobile-icon');
                if (icon) {
                    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
                }
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('nav__menu--open');
                mobileToggle.classList.remove('nav__mobile-toggle--active');
                mobileToggle.setAttribute('aria-expanded', 'false');
                
                const icon = mobileToggle.querySelector('.nav__mobile-icon');
                if (icon) {
                    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
                }
            }
        });
    }
});
