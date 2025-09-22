from PIL import Image
import os

# Paths
input_path = "static/images/home_banner.jpg"
output_path = "static/images/home_banner_resized.jpg"

# Open the image
image = Image.open(input_path)

# Resize to 600px width, maintaining aspect ratio
width, height = image.size
target_width = 600
target_height = int(height * (target_width / width))
image = image.resize((target_width, target_height), Image.LANCZOS)

# Crop to square (600x600), keeping the top
crop_size = min(target_width, target_height)  # Use width as square size
image = image.crop((0, 0, crop_size, crop_size))

# Save the resized and cropped image
image.save(output_path, quality=85)
print(f"Resized and cropped image saved to {output_path}")

# Replace original with resized image
os.remove(input_path)
os.rename(output_path, input_path)
print("Original image replaced with resized version")