import os
import re
import shutil

posts_dir = "/home/sams3pi0l/Documents/Obsidian Vault/picoCtf/blogs/"
attachments_dir = "/home/sams3pi0l/Documents/Obsidian Vault/"
static_images_dir = "/media/sams3pi0l/Hari/Projects/HariBlog/static/images/"

REPO_NAME = "hariblog"   # IMPORTANT for GitHub Pages project sites

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # detect Obsidian embedded images [[image.png]]
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)

        for image in images:
            web_path = f"/{REPO_NAME}/images/{image.replace(' ', '%20')}"

            markdown_image = f"![Image Description]({web_path})"
            content = content.replace(f"[[{image}]]", markdown_image)

            # copy the image
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        with open(filepath, "w") as file:
            file.write(content)

print("DONE — images updated + copied correctly.")
