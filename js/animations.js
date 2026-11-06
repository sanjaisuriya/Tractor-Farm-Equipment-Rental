/**
 * Tractor & Farm Equipment Rental - Animations & Counters
 */

document.addEventListener('DOMContentLoaded', () => {
  // Intersection Observer for scroll reveal
  const reveals = document.querySelectorAll('.reveal-on-scroll');
  if ('IntersectionObserver' in window && reveals.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -50px 0px'
    });

    reveals.forEach(el => observer.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('revealed'));
  }

  // Animated Number Counters
  const counters = document.querySelectorAll('.counter-value');
  if ('IntersectionObserver' in window && counters.length > 0) {
    const counterObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(c => counterObserver.observe(c));
  } else {
    counters.forEach(c => {
      const target = c.getAttribute('data-target') || c.innerText;
      c.innerText = target;
    });
  }
});

function animateCounter(el) {
  const targetStr = el.getAttribute('data-target') || el.innerText;
  const isPercent = targetStr.includes('%');
  const isPlus = targetStr.includes('+');
  const target = parseFloat(targetStr.replace(/[^0-9.]/g, ''));
  const duration = 1800;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out cubic
    const easeProgress = 1 - Math.pow(1 - progress, 3);
    const currentVal = (target * easeProgress).toFixed(target % 1 === 0 ? 0 : 1);

    el.innerText = currentVal + (isPercent ? '%' : '') + (isPlus ? '+' : '');

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      el.innerText = targetStr;
    }
  }

  requestAnimationFrame(update);
}
