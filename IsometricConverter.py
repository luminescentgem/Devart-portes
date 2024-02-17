from PIL import Image
import numpy as np

def convert_to_isometric(image_path):
    # Open an image using Pillow
    image = Image.open(image_path)
    img = np.array(image)

    # Get the dimensions of the original image
    height, width = img.shape[:2]

    # Define the amount of vertical shift for the isometric effect
    vertical_shift = width // 2 - 1

    # Create a new blank image array with increased height for the isometric effect
    new_height = height + vertical_shift
    new_img = np.zeros((new_height, width, 4), dtype=np.uint8)
    
    for y in range(new_height):
        for x in range(width):
            new_img[x, y] = img[x, y] if x < height and y < width else (0, 0, 0, 0)
            
    # Save the modified image
    new_img = Image.fromarray(new_img)
    new_img.save('isometric_' + image_path)

    # Display the original and modified images
    image.show()
    new_img.show()

convert_to_isometric('PorteBase.png')
