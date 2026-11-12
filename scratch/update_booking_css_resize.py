with open('css/pages/booking.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'resize: none' not in css:
    css += "\n/* Disable Textarea Resize Handle */\n.form-textarea, textarea {\n  resize: none !important;\n}\n"
    with open('css/pages/booking.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added to booking.css")
