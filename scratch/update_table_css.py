with open('css/pages/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_table_rules = """.pricing-table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.pricing-table th,
.pricing-table td {
  white-space: nowrap;
}

@media (max-width: 640px) {
  .pricing-table th:first-child,
  .pricing-table td:first-child {
    position: sticky;
    left: 0;
    background: var(--bg-card);
    z-index: 1;
  }
}"""

new_table_rules = """.pricing-table-container {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.pricing-table {
  width: 100%;
  border-collapse: collapse;
}

.pricing-table th,
.pricing-table td {
  vertical-align: middle !important;
}

.pricing-table th {
  white-space: nowrap !important;
  font-size: 0.75rem !important;
  letter-spacing: 0.05em !important;
  font-weight: 700 !important;
}

.pricing-table td {
  vertical-align: middle !important;
  font-size: 0.8125rem;
}

.pricing-table td.align-middle {
  vertical-align: middle !important;
}

@media (max-width: 640px) {
  .pricing-table th:first-child,
  .pricing-table td:first-child {
    position: sticky;
    left: 0;
    background: var(--bg-card);
    z-index: 1;
  }
}"""

css = css.replace(old_table_rules, new_table_rules)

with open('css/pages/pricing.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated table CSS rules in css/pages/pricing.css successfully!")
