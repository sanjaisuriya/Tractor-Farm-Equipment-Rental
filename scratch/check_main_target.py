with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = """  // Contact Form Handling (Page 10)
  const contactForm = document.getElementById('tractorContactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {"""

print("Found target in main.js?", target in js)
