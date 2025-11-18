import os
import re
import shutil

posts_dir = "/media/sams3pi0l/Hari/Projects/HariBlog/content/posts/blogs/"
attachments_dir = "/home/sams3pi0l/Documents/Obsidian Vault/"
static_images_dir = "/media/sams3pi0l/Hari/Projects/HariBlog/static/images/"

REPO_NAME = "hariblog"   # IMPORTANT for GitHub Pages project site

# Supported image extensions
IMAGE_EXTENSIONS = r"(?:png|jpg|jpeg|gif|webp|bmp|svg)"

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Find embedded images in Obsidian format: ![[image.png]]
        images = re.findall(rf'\[\[([^]]*\.{IMAGE_EXTENSIONS})\]\]', content, re.IGNORECASE)

        for image in images:
            # Replace space with %20 in URLs
            markdown_image = f"![Image Description](/{REPO_NAME}/images/{image.replace(' ', '%20')})"

            # Replace the embed syntax with markdown syntax
            content = content.replace(f"[[{image}]]", markdown_image)

            # Full path to the source image in the vault
            image_source = os.path.join(attachments_dir, image)

            # Copy if it exists
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Save updated markdown back to file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

