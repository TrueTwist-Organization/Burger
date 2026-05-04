import glob
import re

html_files = glob.glob('*_burger.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Let's just use string replacement or simpler regex without invalid escapes.
    # The block we want to remove:
    # // 3. Chef "eats" the burger
    # .to(".main-burger-img", { ... })
    
    pattern3 = r'\s*// 3\. Chef "eats" the burger\s*\.to\("\.main-burger-img", \{.*?ease: "back\.in\(2\)"\s*\}\)'
    html = re.sub(pattern3, '', html, flags=re.DOTALL)
    
    pattern6 = r'\s*// 6\. Fresh burger drops down!\s*\.set\("\.main-burger-img", \{.*?ease: "bounce\.out"\s*\}\);?'
    html = re.sub(pattern6, '', html, flags=re.DOTALL)
    
    # We removed step 6, so step 5 now ends the chain, it needs a semicolon
    # Step 5: .to(["#naughty-chef", "#chef-speech"], { ... ease: "power2.in" }, "+=2")
    # Wait, the actual code has `}, "+=2")` or just `})`
    # Let's fix the end of the timeline
    html = re.sub(r'\}, "\+=2"\)\s*\}\);', r'}, "+=2");\n        });', html)
    html = re.sub(r'ease: "power2\.in"\s*\}\)\s*\}\);', r'ease: "power2.in"\n            });\n        });', html)
    
    # If it ends with `}, "+=2")` followed by `</script>`, it might miss a semicolon, which JS allows but is better to have
    html = re.sub(r'\}, "\+=2"\)\s*</script>', r'}, "+=2");\n    </script>', html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Kept the original burger on screen!")
