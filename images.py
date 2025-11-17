import os
import re
import shutil

# Paths
obsidian_posts = "/home/sams3pi0l/Documents/Obsidian Vault/picoCtf/blogs/"
attachments_dir = "/home/sams3pi0l/Documents/Obsidian Vault/"

hugo_posts = "/media/sams3pi0l/Hari/Projects/HariBlog/content/posts/"
hugo_images = "/media/sams3pi0l/Hari/Projects/HariBlog/static/images/"

for filename in os.listdir(obsidian_posts):
    if filename.endswith(".md"):
        src_md = os.path.join(obsidian_posts, filename)
        dest_md = os.path.join(hugo_posts, filename)

        # Copy markdown to Hugo
        shutil.copy(src_md, dest_md)

        # Process links in Hugo version
        with open(dest_md, "r") as f:
            content = f.read()

        # Find all Obsidian wikilinks
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)

        for image in images:
            # Convert to relative Hugo link
            hugo_markdown = f"![Image](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", hugo_markdown)

            # Copy image to static/images/
            src_img = os.path.join(attachments_dir, image)
            if os.path.exists(src_img):
                shutil.copy(src_img, hugo_images)

        with open(dest_md, "w") as f:
            f.write(content)

print("Done: Hugo posts updated, images copied.")
