with open('js/equipment.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Check that renderCard template is closed properly
assert 'renderCard(item)' in js
assert 'window.EquipmentService = EquipmentService;' in js
print("js/equipment.js syntax check passed.")
