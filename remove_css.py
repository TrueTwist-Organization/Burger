
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pattern = "/* --- Clean Menu Styling --- */"
if pattern in css:
    cleaned_css = css.split(pattern)[0]
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(cleaned_css)
    print("Removed Clean Menu Styling.")
else:
    print("Pattern not found.")
