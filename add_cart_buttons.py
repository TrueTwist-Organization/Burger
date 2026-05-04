import re

with open('index.html', 'r') as f:
    html = f.read()

# We need to insert a button right before </div> for each menu-card
# </a>
# </div>

def replacer(match):
    # match.group(1) is the burger title from <h3>...</h3>
    # match.group(2) is the price from <p>₹...</p>
    title = match.group(1)
    price = match.group(2)
    
    button_html = f'\n                <button class="btn-primary" style="margin-top:15px; width:100%; border:none; padding:10px; border-radius:5px; cursor:pointer;" onclick="addToCart(\'{title}\', \'₹{price}\')">Add to Cart</button>\n            </div>'
    
    return f'<h3>{title}</h3>\n                    <p style="color: #E85A1F; font-weight: bold; font-size: 1.2rem; margin-top: 10px;">₹{price}</p>\n                </a>{button_html}'

# Find <h3>(.*?)</h3>
# and <p ...>₹(.*?)</p>
# inside menu-card
html = re.sub(r'<h3>(.*?)</h3>\s*<p[^>]*>₹(.*?)</p>\s*</a>\s*</div>', replacer, html)

with open('index.html', 'w') as f:
    f.write(html)

print("Added cart buttons to index.html")
