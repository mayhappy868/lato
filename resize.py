import os
import glob
from PIL import Image

# Configuration
# You can change this path if you want to run it on a specific folder
workspace_dir = r'.' 
# Set your desired target width (1600px is good for high-res screens without being too large)
target_width = 1600

def resize_images():
    # Find all png images in the directory and subdirectories
    png_files = glob.glob(os.path.join(workspace_dir, '**', '*.png'), recursive=True)
    count = 0

    print(f"Searching for PNG files in {os.path.abspath(workspace_dir)}...")
    
    for file_path in png_files:
        try:
            with Image.open(file_path) as img:
                original_width, original_height = img.size
                
                # Skip images that are already smaller than the target width to prevent blurriness from upscaling
                if original_width <= target_width:
                    print(f'Skipped {os.path.basename(file_path)}: {original_width}x{original_height} (already smaller than or equal to target)')
                    continue
                
                # Calculate the new height keeping the aspect ratio
                aspect_ratio = original_height / original_width
                target_height = int(target_width * aspect_ratio)
                
                # Resize with high-quality Lanczos filter
                resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                
                # Overwrite the original file
                resized_img.save(file_path, optimize=True)
                print(f'Resized {os.path.basename(file_path)}: {original_width}x{original_height} -> {target_width}x{target_height}')
                count += 1
        except Exception as e:
            print(f'Error processing {file_path}: {e}')

    print(f'\nSuccessfully resized {count} images to {target_width}px width.')

if __name__ == "__main__":
    resize_images()
