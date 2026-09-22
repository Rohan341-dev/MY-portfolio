/* ========================================
   ROHAN CODEKAGE — DIGITAL WORKSPACE
   Interactive Layer
   ======================================== */

(function() {
  'use strict';

  // --- DOM ---
  const cursor = document.getElementById('cursor');
  const cursorRing = document.getElementById('cursorRing');
  const loader = document.getElementById('loader');
  const nav = document.getElementById('nav');
  const navToggle = document.getElementById('navToggle');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileLinks = document.querySelectorAll('.mobile-menu__link');
  const navLinks = document.querySelectorAll('[data-nav]');
  const contactForm = document.getElementById('contactForm');

  // --- LOADER ---
  window.addEventListener('load', () => {
    setTimeout(() => {
      loader.classList.add('hidden');
    }, 600);
  });

  // --- CUSTOM CURSOR ---
  let mx = 0, my = 0, rx = 0, ry = 0;

  document.addEventListener('mousemove', (e) => {
    mx = e.clientX;
    my = e.clientY;
    cursor.style.transform = `translate(${mx - 3}px, ${my - 3}px)`;
  });

  function animateCursor() {
    rx += (mx - rx) * 0.1;
    ry += (my - ry) * 0.1;
    cursorRing.style.transform = `translate(${rx - 14}px, ${ry - 14}px)`;
    requestAnimationFrame(animateCursor);
  }
  animateCursor();

  // Hover expand
  const hoverEls = document.querySelectorAll('a, button, .project__eco-item, .builder-map__node--area, .lab__entry, .notes__card, .now__item, .milestone, .certificate');
  hoverEls.forEach(el => {
    el.addEventListener('mouseenter', () => cursorRing.classList.add('expand'));
    el.addEventListener('mouseleave', () => cursorRing.classList.remove('expand'));
  });

  // --- NAVIGATION ---
  let lastY = 0;
  let ticking = false;

  function onScroll() {
    const y = window.scrollY;
    if (y > 80) {
      nav.classList.toggle('nav--hidden', y > lastY);
    } else {
      nav.classList.remove('nav--hidden');
    }
    lastY = y;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  });

  // Active nav
  function updateNav() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 200;
    sections.forEach(section => {
      const top = section.offsetTop;
      const h = section.offsetHeight;
      const id = section.getAttribute('id');
      if (scrollPos >= top && scrollPos < top + h) {
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === '#' + id);
        });
      }
    });
  }
  window.addEventListener('scroll', updateNav);

  // Mobile toggle
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  });

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  // Escape closes menu
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
      navToggle.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    }
  });

  // --- SMOOTH SCROLL ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 72,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- SCROLL REVEAL ---
  function revealOnScroll() {
    document.querySelectorAll('.reveal').forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.88) {
        el.classList.add('visible');
      }
    });
  }
  window.addEventListener('scroll', revealOnScroll);
  window.addEventListener('load', revealOnScroll);
  setTimeout(revealOnScroll, 100);

  // --- BUILDER MAP INTERACTION ---
  const builderBranches = document.querySelectorAll('.builder-map__branch');
  builderBranches.forEach(branch => {
    const node = branch.querySelector('.builder-map__node--area');
    node.addEventListener('click', () => {
      const wasActive = branch.classList.contains('active');
      builderBranches.forEach(b => b.classList.remove('active'));
      if (!wasActive) branch.classList.add('active');
    });
  });
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.builder-map__branch')) {
      builderBranches.forEach(b => b.classList.remove('active'));
    }
  });

  // --- FOUNDER MODE SWITCH ---
  const modeBtns = document.querySelectorAll('.founder-mode__btn');
  const modePanels = document.querySelectorAll('.founder-mode__panel');

  modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.dataset.mode;
      modeBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      modePanels.forEach(panel => {
        panel.classList.toggle('active', panel.dataset.panel === mode);
      });
    });
  });

  // --- HERO PARALLAX ---
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    const heroStatement = document.querySelector('.hero__statement');
    if (heroStatement && y < window.innerHeight) {
      heroStatement.style.transform = `translateY(${y * 0.08}px)`;
      heroStatement.style.opacity = 1 - (y / window.innerHeight) * 0.6;
    }
  });

  // --- TIMELINE ANIMATION ---
  const timelineItems = document.querySelectorAll('.timeline__item');
  function animateTimeline() {
    timelineItems.forEach((item, i) => {
      const rect = item.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.85) {
        item.style.transition = `opacity 0.6s ${i * 0.08}s, transform 0.6s ${i * 0.08}s`;
        item.classList.add('visible');
      }
    });
  }
  window.addEventListener('scroll', animateTimeline);

  // --- CONTACT FORM ---
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('.btn');
      const orig = btn.textContent;
      btn.textContent = 'Sent!';
      btn.style.background = '#27c93f';
      setTimeout(() => {
        btn.textContent = orig;
        btn.style.background = '';
        contactForm.reset();
      }, 2500);
    });
  }

  // --- PAGE VISIBILITY ---
  document.addEventListener('visibilitychange', () => {
    document.body.style.animationPlayState = document.hidden ? 'paused' : 'running';
  });

})();