svg_light = """<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none'>
  <rect x='3' y='4' width='18' height='18' rx='2.5' stroke='#334155' stroke-width='2'></rect>
  <path d='M3 4h18v5H3z' fill='#334155'></path>
  <path d='M8 2v3M16 2v3' stroke='#334155' stroke-width='2' stroke-linecap='round'></path>
</svg>"""

svg_dark = """<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none'>
  <rect x='3' y='4' width='18' height='18' rx='2.5' stroke='#FFFFFF' stroke-width='2'></rect>
  <path d='M3 4h18v5H3z' fill='#FFFFFF'></path>
  <path d='M8 2v3M16 2v3' stroke='#FFFFFF' stroke-width='2' stroke-linecap='round'></path>
</svg>"""

with open("test_cal_light.svg", "w") as f:
    f.write(svg_light)
with open("test_cal_dark.svg", "w") as f:
    f.write(svg_dark)
print("Saved SVGs")
