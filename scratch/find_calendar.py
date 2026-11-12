import glob, re

for f in glob.glob("*.html") + glob.glob("css/*.css") + glob.glob("js/*.js"):
    with open(f, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines):
        if any(w in line.lower() for w in ["fa-calendar", "type=\"date\"", "type='date'", "calendar"]):
            print(f"{f}:{idx+1} {line.strip()[:100]}")
