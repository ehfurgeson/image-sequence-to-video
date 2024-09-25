import os
import re
from moviepy.editor import ImageSequenceClip

def get_new_output_video(base_video_name):
    """Generates a new output video name if 'output_videoX.mp4' already exists."""
    output_video = base_video_name
    counter = 1

    base_name, extension = os.path.splitext(base_video_name)
    
    # check if the file exists, and if it does, increment the counter and create a new video file name
    while os.path.exists(output_video):
        output_video = f"{base_name}{counter}{extension}"
        counter += 1

    return output_video

def create_video_from_images(image_folder, output_video_base, duration_per_image):
    # collect all jpg, jpeg, and png images
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("No image files found in the directory.")
        return

    print(f"Found images: {image_files}")

    # filter for images with the specified naming convention
    image_files = [img for img in image_files if re.search(r'processed_(\d{3})_IMG_\d{4}', img)]

    if not image_files:
        print("No valid numeric image files found in the directory.")
        return

    # sort images based on the numeric part of the filename
    image_files.sort(key=lambda x: int(re.search(r'(\d{3})', x).group()))

    print(f"Filtered and sorted images: {image_files}")

    # create full paths for the images
    image_paths = [os.path.join(image_folder, img) for img in image_files]

    # create a video clip from the images
    clip = ImageSequenceClip(image_paths, fps=1/duration_per_image)

    # get the new output video file name (with incrementing numbers)
    output_video = get_new_output_video(output_video_base)

    # write the video file
    clip.write_videofile(output_video, codec='libx264')
    print(f"Video created successfully! Saved as {output_video}")

if __name__ == "__main__":
    image_folder = "./processed_images_1"  # replace with your image folder
    output_video_base = "output_video.mp4"  # base name for your output video
    duration_per_image = 0.18  # adjust how long each image should be shown
    create_video_from_images(image_folder, output_video_base, duration_per_image)