with open('universe.css', 'r') as f:
    css = f.read()

# Fix layout
css = css.replace('.sec-menu-universe {', '.sec-menu-universe {\n    display: block !important;\n    flex-direction: column;')

# Add missing keyframes and classes
append_css = """
@keyframes dropWord {
    0% { transform: translateY(-50px); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
}

.u-card.animate-in {
    opacity: 1 !important;
}
"""

if "dropWord" not in css:
    css += append_css

with open('universe.css', 'w') as f:
    f.write(css)

print("Fixed universe.css layout and missing animations.")
