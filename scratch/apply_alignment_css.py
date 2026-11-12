with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace or append the alignment CSS rules
alignment_css = """
/* --- Pricing Card Perfect Alignment System --- */
.pricing-card {
  background: var(--bg-card);
  border-radius: var(--radius-xl);
  border: 2px solid var(--border-color);
  padding: 1.5rem;
  transition: var(--transition);
  position: relative;
  display: flex;
  flex-direction: column;
  height: 100%;
}

@media (min-width: 1024px) {
  .pricing-card {
    padding: 1.75rem;
  }
}

.pricing-card.featured {
  border: 2px solid var(--color-agri);
  box-shadow: 0 10px 30px rgba(52, 122, 69, 0.15);
}

.pricing-card-header {
  display: flex;
  flex-direction: column;
  min-height: 110px;
  margin-bottom: 0.75rem;
}

.pricing-card-desc {
  font-size: 0.75rem;
  line-height: 1.35rem;
  min-height: 54px;
}

.pricing-price-block {
  min-height: 80px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  margin-bottom: 1.25rem;
  padding-bottom: 1.25rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}

.dark .pricing-price-block {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.pricing-price-note {
  font-size: 0.6875rem; /* 11px */
  line-height: 1.15rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 0.25rem;
  display: block;
}

.pricing-features {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  margin-bottom: 1.5rem;
  flex: 1 1 auto;
}

.pricing-features li {
  min-height: 38px;
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  font-size: 0.75rem;
  line-height: 1.25rem;
}

.pricing-features li i {
  margin-top: 2px;
  flex-shrink: 0;
}

/* Bundle Cards Alignment */
.bundle-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.bundle-card h3 {
  min-height: 48px;
}

.bundle-card .bundle-included {
  min-height: 40px;
}
"""

# Check if .pricing-card-header is already in css
if '.pricing-card-header' not in css:
    css = css + "\n" + alignment_css
    with open('css/pages/pricing.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added alignment_css to css/pages/pricing.css")
else:
    print("Already present in css")
