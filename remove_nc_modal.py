with open('index.html', 'r') as f:
    html = f.read()

# Find the start of the nc-modal
if '<div id="nc-modal">' in html:
    # Everything before the modal
    html = html.split('    <!-- NEW CARTOON MODAL -->')[0]
    if '<div id="nc-modal">' in html: # Fallback if comment is missing
        html = html.split('    <div id="nc-modal">')[0]
    
    # ensure it ends with body and html
    html = html.strip()
    if not html.endswith('</body>\n</html>'):
        if html.endswith('</body>'):
            html += '\n</html>'
        elif html.endswith('</html>'):
            # It already has html but missing body? Just to be safe:
            pass
        else:
            html += '\n</body>\n</html>'

with open('index.html', 'w') as f:
    f.write(html)
