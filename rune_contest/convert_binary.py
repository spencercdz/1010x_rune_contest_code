from PIL import Image
import numpy as np

def color_image_to_grayscale_array(image_path, size=(500, 500)):
    """
    Converts a color image to a grayscale array with pixel values ranging from 0 to 255.
    
    Args:
        image_path (str): Path to the input image.
        size (tuple): Desired size of the output image (width, height).
    
    Returns:
        numpy.ndarray: A 2D array of grayscale pixel values (0–255).
    """
    # Open the image
    img = Image.open(image_path)
    
    # Resize the image to the specified size
    img = img.resize(size)

    # Convert the image to grayscale
    img = img.convert('L')  # 'L' mode means grayscale
    
    # Convert the grayscale image into a numpy array
    grayscale_array = np.array(img)
    
    return grayscale_array

# Link image path
image_path = "shower.jpg"
grayscale_array = color_image_to_grayscale_array(image_path)

# Function to save the grayscale array to a file without the ellipses
def save_grayscale_array_as_python_list(grayscale_array, filename):
    """
    Saves the grayscale array as a Python list in a text file.
    
    Args:
        grayscale_array (numpy.ndarray): The 2D array of grayscale pixel values.
        filename (str): The name of the output file.
    """
    # Convert the array to a string representation without truncation
    array_str = np.array2string(grayscale_array, separator=',', threshold=np.inf)
    
    # Open the file in write mode
    with open(filename, 'w') as f:
        # Write the array string representation into the file
        f.write(array_str)

# Execute conversion
print("Array shape:", grayscale_array.shape)  # Print array
save_grayscale_array_as_python_list(grayscale_array, 'grayscale_rune.txt')
