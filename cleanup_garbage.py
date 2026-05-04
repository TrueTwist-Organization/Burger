with open('index.html', 'r') as f:
    lines = f.readlines()

# Find the line index where <!-- Avatar --> starts around the bottom
avatar_index = -1
for i, line in enumerate(lines):
    if line.strip() == '<!-- Avatar -->':
        # Let's verify it's the one after the footer scripts
        if i > 1000:
            avatar_index = i
            break

if avatar_index != -1:
    lines = lines[:avatar_index]

html = ''.join(lines).strip()
if not html.endswith('</html>'):
    if html.endswith('</body>'):
        html += '\n</html>'
    else:
        html += '\n</body>\n</html>'

with open('index.html', 'w') as f:
    f.write(html)
