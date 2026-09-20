/* ========================================
   ROHAN CODEKAGE — PORTFOLIO SCRIPTS
   ======================================== */

(function() {
  'use strict';

  // --- DOM Elements ---
  const cursor = document.getElementById('cursor');
  const cursorFollower = document.getElementById('cursorFollower');
  const nav = document.getElementById('nav');
  const navToggle = document.getElementById('navToggle');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileLinks = document.querySelectorAll('.mobile-menu__link');
  const typewriter = document.getElementById('typewriter');
  const terminalOutput = document.getElementById('terminalOutput');
  const filterBtns = document.querySelectorAll('.work__filter-btn');
  const projects = document.querySelectorAll('.project');
  const reveals = document.querySelectorAll('.reveal');
  const contactForm = document.getElementById('contactForm');
  const navLinks = document.querySelectorAll('.nav__link');

  // --- Custom Cursor ---
  let mouseX = 0, mouseY = 0;
  let followerX = 0, followerY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursor.style.transform = `translate(${mouseX - 4}px, ${mouseY - 4}px)`;
  });

  function animateFollower() {
    followerX += (mouseX - followerX) * 0.12;
    followerY += (mouseY - followerY) * 0.12;
    cursorFollower.style.transform = `translate(${followerX - 16}px, ${followerY - 16}px)`;
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  // Hover effect on interactive elements
  const hoverTargets = document.querySelectorAll('a, button, .project__card, .ailab__card, .stack__category, .achievement, .building__card, .exploring__item, .github__repo, .beyond__card, .company-card, .leadership__card, .founder-mode__node--role, .certificate-card');
  hoverTargets.forEach(el => {
    el.addEventListener('mouseenter', () => cursorFollower.classList.add('hovering'));
    el.addEventListener('mouseleave', () => cursorFollower.classList.remove('hovering'));
  });

  // --- Navigation ---
  let lastScrollY = 0;
  let ticking = false;

  function handleScroll() {
    const currentScrollY = window.scrollY;

    if (currentScrollY > 100) {
      if (currentScrollY > lastScrollY) {
        nav.classList.add('nav--hidden');
      } else {
        nav.classList.remove('nav--hidden');
      }
    } else {
      nav.classList.remove('nav--hidden');
    }

    lastScrollY = currentScrollY;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(handleScroll);
      ticking = true;
    }
  });

  // Mobile Menu Toggle
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

  // Active nav link based on scroll
  function updateActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 200;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateActiveNav);

  // --- Terminal Typewriter ---
  const terminalLines = [
    { type: 'command', text: 'whoami' },
    { type: 'output', lines: ['', '  rohan-codekage', ''] },
    { type: 'output', lines: ['  > building ideas', '  > learning systems', '  > exploring AI', '  > shipping projects', ''] },
  ];

  function typeTerminal() {
    let lineIndex = 0;
    let charIndex = 0;

    function typeCommand() {
      if (lineIndex >= terminalLines.length) return;

      const line = terminalLines[lineIndex];

      if (line.type === 'command') {
        if (charIndex < line.text.length) {
          typewriter.textContent += line.text[charIndex];
          charIndex++;
          setTimeout(typeCommand, 80 + Math.random() * 60);
        } else {
          typewriter.style.display = 'none';
          lineIndex++;
          charIndex = 0;
          setTimeout(typeOutput, 300);
        }
      }
    }

    function typeOutput() {
      if (lineIndex >= terminalLines.length) return;

      const line = terminalLines[lineIndex];

      if (line.type === 'output') {
        let lineCharIndex = 0;

        function typeLine() {
          if (lineCharIndex < line.lines.length) {
            const div = document.createElement('div');
            div.className = 'terminal__output-line';
            div.innerHTML = '<span>' + line.lines[lineCharIndex] + '</span>';
            terminalOutput.appendChild(div);
            lineCharIndex++;
            setTimeout(typeLine, 100);
          } else {
            lineIndex++;
            if (lineIndex < terminalLines.length) {
              setTimeout(typeOutput, 200);
            }
          }
        }

        typeLine();
      }
    }

    typeCommand();
  }

  // Start typewriter after a delay
  setTimeout(typeTerminal, 1000);

  // --- Scroll Reveal ---
  function revealOnScroll() {
    reveals.forEach(el => {
      const rect = el.getBoundingClientRect();
      const windowHeight = window.innerHeight;

      if (rect.top < windowHeight * 0.88) {
        el.classList.add('visible');
      }
    });
  }

  window.addEventListener('scroll', revealOnScroll);
  window.addEventListener('load', revealOnScroll);
  // Initial check
  setTimeout(revealOnScroll, 100);

  // --- Project Filtering ---
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;

      // Update active button
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Filter projects
      projects.forEach(project => {
        const category = project.dataset.category;

        if (filter === 'all' || category.includes(filter)) {
          project.classList.remove('hidden');
          project.style.opacity = '0';
          project.style.transform = 'translateY(20px)';

          setTimeout(() => {
            project.style.transition = 'opacity 0.5s, transform 0.5s';
            project.style.opacity = '1';
            project.style.transform = 'translateY(0)';
          }, 50);
        } else {
          project.style.opacity = '0';
          project.style.transform = 'translateY(20px)';
          setTimeout(() => {
            project.classList.add('hidden');
          }, 400);
        }
      });
    });
  });

  // --- Contact Form ---
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const formData = new FormData(contactForm);
      const name = formData.get('name');
      const email = formData.get('email');
      const message = formData.get('message');

      // Simple validation
      if (!name || !email || !message) return;

      // Show success feedback
      const btn = contactForm.querySelector('.btn');
      const originalText = btn.textContent;
      btn.textContent = 'Message Sent!';
      btn.style.background = '#27c93f';

      setTimeout(() => {
        btn.textContent = originalText;
        btn.style.background = '';
        contactForm.reset();
      }, 3000);
    });
  }

  // --- Smooth Scroll for Anchor Links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        const offsetTop = target.offsetTop - 80;
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- Parallax subtle effect on hero grid ---
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const heroGrid = document.querySelector('.hero__grid');
    if (heroGrid && scrolled < window.innerHeight) {
      heroGrid.style.transform = `translateY(${scrolled * 0.3}px)`;
    }
  });

  // --- Timeline animation on scroll ---
  const timelineItems = document.querySelectorAll('.timeline__item');
  function animateTimeline() {
    timelineItems.forEach((item, index) => {
      const rect = item.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.85) {
        item.style.transition = `opacity 0.6s ${index * 0.1}s, transform 0.6s ${index * 0.1}s`;
        item.classList.add('visible');
      }
    });
  }

  window.addEventListener('scroll', animateTimeline);

  // --- Keyboard Navigation Support ---
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
      navToggle.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    }
  });

  // --- Page visibility for performance ---
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      document.body.style.animationPlayState = 'paused';
    } else {
      document.body.style.animationPlayState = 'running';
    }
  });

  // --- Founder Mode Interaction ---
  const founderBranches = document.querySelectorAll('.founder-mode__branch');
  founderBranches.forEach(branch => {
    const roleNode = branch.querySelector('.founder-mode__node--role');
    roleNode.addEventListener('click', () => {
      const isActive = branch.classList.contains('active');
      // Close all branches first
      founderBranches.forEach(b => b.classList.remove('active'));
      // Toggle the clicked one
      if (!isActive) {
        branch.classList.add('active');
      }
    });
  });

  // Close founder mode branches when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.founder-mode__branch')) {
      founderBranches.forEach(b => b.classList.remove('active'));
    }
  });

})();
