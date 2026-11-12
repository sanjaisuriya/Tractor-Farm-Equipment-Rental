with open('js/pricing.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("Length of pricing.js:", len(js))
print("\nFirst 1000 chars:")
print(js[:1000])
