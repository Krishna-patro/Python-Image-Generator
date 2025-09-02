from PIL import Image
import numpy as np

def create_digital_image(width=400, height=300):
    """
    Creates a simple digital image with a gradient pattern.
    """
    try:
        image_array = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                red = int((x / width) * 255)
                blue = int((y / height) * 255)
                image_array[y, x] = [red, 0, blue]

        img = Image.fromarray(image_array, 'RGB')
        img.save("my_generated_image.png")
        print("Image created successfully as 'my_generated_image.png'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_digital_image()
