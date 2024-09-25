import cv2
import os
import re

def get_new_output_folder(base_folder):
    """Generates a new output folder name if 'processed_images' already exists."""
    output_folder = base_folder
    counter = 1
    
    # check if the folder exists, and if it does, increment the counter and create a new folder name
    while os.path.exists(output_folder):
        output_folder = f"{base_folder}_{counter}"
        counter += 1
    
    os.makedirs(output_folder)
    return output_folder

def process_and_save_images(image_folder, output_folder_base, width, height, reverse_order=True):
    # get the final output folder name, either processed_images or processed_images_X
    output_folder = get_new_output_folder(output_folder_base)

    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mpo'))]
    
    if not image_files:
        print("No image files found in the directory.")
        return

    # sort images based on numeric part of filename, either ascending or descending
    image_files.sort(key=lambda x: int(re.search(r'\d+', x).group()), reverse=reverse_order)

    def resize_with_padding(image, target_width, target_height):
        h, w = image.shape[:2]
        aspect_ratio = w / h

        if w / target_width > h / target_height:
            new_w = target_width
            new_h = int(new_w / aspect_ratio)
        else:
            new_h = target_height
            new_w = int(new_h * aspect_ratio)

        resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

        delta_w = target_width - new_w
        delta_h = target_height - new_h
        top, bottom = delta_h // 2, delta_h - (delta_h // 2)
        left, right = delta_w // 2, delta_w - (delta_w // 2)

        canvas = cv2.copyMakeBorder(
            resized_image,
            top, bottom, left, right,
            cv2.BORDER_CONSTANT,
            value=[0, 0, 0]  # black padding
        )

        return canvas

    for i, image_file in enumerate(image_files):
        img_path = os.path.join(image_folder, image_file)
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Failed to load image: {img_path}. Skipping...")
            continue
        
        print(f"Processing: {img_path} | Original size: {img.shape}")
        
        # resize image while maintaining aspect ratio and adding black padding
        img_resized_padded = resize_with_padding(img, width, height)
        
        print(f"Resized size: {img_resized_padded.shape}")
        
        # save the processed image only
        output_path = os.path.join(output_folder, f"processed_{i:03d}_{image_file}")
        cv2.imwrite(output_path, img_resized_padded)
        print(f"Saved processed image to: {output_path}")

    print(f"All images processed and saved in: {output_folder}")

if __name__ == "__main__":
    image_folder = "./images"  # replace with your image folder
    output_folder_base = "./processed_images"  # base folder name
    width = 1920
    height = 1080
    reverse_order = False  # change to False for forward order
    process_and_save_images(image_folder, output_folder_base, width, height, reverse_order)