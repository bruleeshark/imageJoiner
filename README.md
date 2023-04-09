# imageJoiner
uses python and pillow to join two images called logo and background

Here's how the script works:

1. First, you specify the paths to the logo folder, background folder, and output folder.

2. The script uses the os.listdir function to get a list of files in each folder.

3. For each background image, the script chooses a random logo image, opens both images using Pillow's Image.open function, and resizes the logo image to fit in the center of the background image.

4. The script then uses Pillow's Image.paste function to paste the logo image onto the center of the background image.

5. Finally, the script saves the combined image with a filename that includes both the logo and background filenames.

Make sure to install the Pillow library using Poetry by adding it to your pyproject.toml file and running poetry install.
