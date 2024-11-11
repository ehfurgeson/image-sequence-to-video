# image-sequence-to-video
Turns an image sequence into a video while automatically resizing images and maintaining aspect ratio
    
## Overview
    
This Python project processes a collection of images by resizing them while maintaining their aspect ratio and adding black padding to fit a specified resolution. After processing, the images are compiled into a video sequence. The project leverages OpenCV for image manipulation and MoviePy for creating videos from the processed images.
    
## Features
    
- **Image Preprocessing**: Resizes images to a given resolution while maintaining their aspect ratio and adds black padding to fit.
- **Video Creation**: Combines processed images into a video with a specified duration per frame.
- **Dynamic Naming**: Automatically creates unique output directories and video filenames to avoid overwriting existing files.
    
## Requirements
    
- Python 3.7+
- Required libraries:
- OpenCV (`cv2`)
- MoviePy
- Re (for regular expressions)
- OS (for file management)
    
    To install the required libraries, run:
    
    ```bash
    pip install opencv-python moviepy
    ```
    
    ## Usage
    
    ### Image Preprocessing
    
    This script resizes and processes images from a specified folder, ensuring they are padded and saved in a new folder. 
    
    ```python
    python image_preprocessor.py
    ```
    
    Parameters:
    
    - `image_folder`: Path to the folder containing the images.
    - `output_folder_base`: Base name for the folder to store processed images.
    - `width`, `height`: Target dimensions for the images.
    - `reverse_order`: Boolean flag to reverse the order of image processing.
    
    ### Video Creation
    
    Once the images are processed, this script compiles them into a video sequence.
    
    ```python
    python create_video.py
    ```
    
    Parameters:
    
    - `image_folder`: Folder containing the processed images.
    - `output_video_base`: Base name for the output video file.
    - `duration_per_image`: How long each image should be shown in the video.
    
    ## Example
    
    1. **Image Preprocessing**
    
    ```bash
    python image_preprocessor.py --image_folder ./images --output_folder_base ./processed_images --width 1920 --height 1080
    ```
    
    2. **Video Creation**
    
    ```bash
    python create_video.py --image_folder ./processed_images --output_video_base output_video.mp4 --duration_per_image 0.18
    ```
    
    ## File Structure
    
    ```
    .
    ├── image_preprocessor.py
    ├── video_creator.py
    ├── images/
    │   └── [your image files]
    └── processed_images/
        └── [processed image files]
    ```
    
    ## License
    
    This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as needed. 
    
