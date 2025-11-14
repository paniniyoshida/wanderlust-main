from PIL import Image
import os

input_path = "static/images/home_banner.jpg"
output_path = "static/images/home_banner_resized.jpg"

image = Image.open(input_path)

width, height = image.size
target_width = 600
target_height = int(height * (target_width / width))
image = image.resize((target_width, target_height), Image.LANCZOS)

crop_size = min(target_width, target_height)
image = image.crop((0, 0, crop_size, crop_size))

image.save(output_path, quality=85)
print(f"Resized and cropped image saved to {output_path}")

os.remove(input_path)
os.rename(output_path, input_path)
print("Original image replaced with resized version")