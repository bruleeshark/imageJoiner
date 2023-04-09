import os
import random
from PIL import Image

logo_folder = "path/to/logo/folder"
bg_folder = "path/to/background/folder"
output_folder = "path/to/output/folder"

logo_files = os.listdir(logo_folder)
bg_files = os.listdir(bg_folder)

for bg_file in bg_files:
    # Choose a random logo and open both images
    logo_file = random.choice(logo_files)
    logo_path = os.path.join(logo_folder, logo_file)
    bg_path = os.path.join(bg_folder, bg_file)
    logo = Image.open(logo_path)
    bg = Image.open(bg_path)

    # Resize logo to fit in the center of background
    logo_size = min(bg.size[0], bg.size[1]) // 2
    logo = logo.resize((logo_size, logo_size))

    # Paste logo in center of background
    x = (bg.size[0] - logo.size[0]) // 2
    y = (bg.size[1] - logo.size[1]) // 2
    bg.paste(logo, (x, y), logo)

    # Save combined image
    output_file = logo_file.replace(".png", "") + "+" + bg_file
    output_path = os.path.join(output_folder, output_file)
    bg.save(output_path)
