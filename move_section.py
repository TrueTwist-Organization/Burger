import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to extract the sec-story-new block.
# Let's use regex to find the start and end.
# It starts with: <!-- Section 3: Our Story (Cinematic Redesign) -->
# and ends with: </section> before <!-- Section 3: Menu -->

start_marker = "<!-- Section 3: Our Story (Cinematic Redesign) -->"
end_marker = "<!-- Section 3: Menu -->"

if start_marker in html and end_marker in html:
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    
    story_section = html[start_idx:end_idx]
    
    # Remove it from the original place
    html_without_story = html[:start_idx] + html[end_idx:]
    
    # Now find where to insert it. The user wants it AFTER the menu section.
    # The menu section is <!-- FLOATING BURGER UNIVERSE MENU -->
    # and ends right before <!-- Login / Signup Modal --> or <!-- Footer -->
    
    insert_marker = "<!-- Footer -->"
    if insert_marker in html_without_story:
        insert_idx = html_without_story.find(insert_marker)
        
        # Insert the story section before the footer
        final_html = html_without_story[:insert_idx] + story_section + "\n" + html_without_story[insert_idx:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Successfully moved Our Story section to the bottom.")
    else:
        print("Could not find insert marker.")
else:
    print("Could not find start or end markers.")
