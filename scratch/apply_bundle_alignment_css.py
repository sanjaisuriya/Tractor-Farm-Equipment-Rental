with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

bundle_extra_css = """
/* Bundle Cards Strict Alignment */
.bundle-title {
  min-height: 52px;
  display: flex;
  align-items: flex-start;
}

.bundle-included {
  min-height: 44px;
  display: flex;
  align-items: flex-start;
}

.bundle-price-block {
  min-height: 68px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.bundle-features {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex: 1 1 auto;
}

.bundle-features li {
  min-height: 32px;
  display: flex;
  align-items: flex-start;
}
"""

if '.bundle-title' not in css:
    css += "\n" + bundle_extra_css
    with open('css/pages/pricing.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added bundle alignment CSS to pricing.css")
else:
    print("Already exists in pricing.css")
