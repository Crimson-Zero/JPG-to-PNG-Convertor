import sys
import os

from PIL import Image

jpeg_directory = sys.argv[1]
PNG_directory = sys.argv[2]
get_files = os.listdir(jpeg_directory)

image_array = []

for file in get_files:
    if "jpg" in file:
        image_array.append(file)


for image in image_array:
    name = image.split(".")[0]
    image_item = Image.open(image)
    image_item.save(f"{PNG_directory}/{name}.png")
