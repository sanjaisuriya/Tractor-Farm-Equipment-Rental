with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Add bundle-img-wrapper and payment-card styles if not present
extra_styles = '''
/* Bundle Card Image Wrapper */
.bundle-card .bundle-img-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 1rem;
  background-color: rgba(0, 0, 0, 0.04);
}

.bundle-card .bundle-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.bundle-card:hover .bundle-img-wrapper img {
  transform: scale(1.05);
}

/* Payment Method Cards */
.payment-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.payment-card:hover {
  transform: translateY(-4px);
  border-color: var(--color-agri);
  box-shadow: 0 10px 24px rgba(23, 61, 43, 0.08);
}
'''

if '.bundle-card .bundle-img-wrapper' not in text:
    text += '\n' + extra_styles.strip() + '\n'
    with open('css/pages/pricing.css', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added extra styles to pricing.css")
else:
    print("Styles already present in pricing.css")
