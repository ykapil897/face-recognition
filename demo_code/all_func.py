import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from skimage.feature import hog
import os
import cv2


def extract_features(image):
    print("before hog")
    # Compute HOG features and visualization
    features, hog_image = hog(image, orientations=9, 
                                pixels_per_cell=(8, 8),
                                cells_per_block=(2, 2), 
                                visualize=True, transform_sqrt=True)
    print("after hog")
    print(f"features {np.array(features).shape}")
    return np.array(features), np.array(hog_image)

def prepare_data(image):
    features, hog_image = extract_features(image)
    # Normalize features
    print("returned correctly")
    return features, hog_image


def resize_images(image):
    """
    Resize a list of images to 125x94 pixels with 3 channels using PyTorch.
    
    Args:
    - images (list): List of images to resize.
    
    Returns:
    - resized_images (list): List of resized images as PyTorch tensors.
    """
    # Define the transformation
    transform = transforms.Compose([
        transforms.Resize((125, 94), interpolation=Image.BILINEAR),
        transforms.ToTensor(),
    ])
    
    image_pil = Image.fromarray(np.uint8(image))
    resized_image = transform(image_pil)
    return resized_image

def convert_to_grayscale(image):
    # Convert PIL Image to OpenCV format if needed
    if not isinstance(image, np.ndarray):
        image = np.array(image).reshape(125, 94, 3)
        print(type(image))
        print(image.shape)

    # Check if the image is not grayscale
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        print("yes")
        print(image.shape)
    else:
        print("no")

    return image

def read_labels_from_file(file_path, label):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return None

    # Read the file and store each line as an item in a list
    with open(file_path, 'r') as file:
        strings_list = [line.strip() for line in file.readlines()]

    return strings_list[label]



