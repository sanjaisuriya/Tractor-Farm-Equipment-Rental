import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Inspect Section 4 table
m4 = re.search(r'Tractor Specifications & Price Matrix.*?</section>', text, re.DOTALL)
if m4:
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', m4.group(0), re.DOTALL)
    print(f"Section 4 Table has {len(rows)} rows:")
    for r in rows:
        cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.DOTALL)]
        if cells:
            print("  | ".join(cells))

# Inspect Section 5 table
print("\n--- Section 5 Implement Table ---")
m5 = re.search(r'Standalone Farm Implement & Machinery Attachment Rates.*?</section>', text, re.DOTALL)
if m5:
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', m5.group(0), re.DOTALL)
    print(f"Section 5 Table has {len(rows)} rows:")
    for r in rows:
        cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.DOTALL)]
        if cells:
            print("  | ".join(cells))
