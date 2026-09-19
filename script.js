// Initialize Discord profile
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('discord-name').textContent = 'sharky03493';
    document.getElementById('discord-status').textContent = '@sharky03493';
    document.getElementById('discord-badges').innerHTML = '<i class="fa-brands fa-discord" style="color: #5865F2;"></i>';
    document.getElementById('discord-avatar').src = 'https://cdn.discordapp.com/avatars/1446177881997967460/f1ddea83fe57989a1d4394d66c7ea3e4.webp?size=256';
});

// Header scroll effect
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.pageYOffset > 50);
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        const target = document.querySelector(targetId);
        if (target) {
            e.preventDefault();
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - header.offsetHeight - 20;
            window.scrollTo({ top: targetPosition, behavior: 'smooth' });
        }
    });
});

// Active nav link highlighting
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    link.classList.toggle('active', href === currentPage || (currentPage === '' && href === 'index.html'));
});

// Copy Discord username on click
document.addEventListener('click', (e) => {
    const target = e.target.closest('.discord-tag, .discord-name-row');
    if (target && target.textContent.includes('sharky03493')) {
        navigator.clipboard.writeText('sharky03493').then(() => {
            const originalText = target.textContent;
            target.textContent = 'Copied!';
            target.style.color = '#10b981';
            setTimeout(() => { target.textContent = originalText; target.style.color = ''; }, 1500);
        });
    }
});

// Keyboard navigation
document.addEventListener('keydown', (e) => { if (e.key === 'Tab') document.body.classList.add('keyboard-nav'); });
document.addEventListener('mousedown', () => document.body.classList.remove('keyboard-nav'));

// Add webneko.net cursor cat
const script = document.createElement('script');
script.src = 'https://webneko.net/api/cat.js';
script.async = true;
document.body.appendChild(script);