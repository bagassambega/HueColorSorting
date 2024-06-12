import os.path

from PIL import Image, ImageDraw

def generate_image_from_rgb_matrix(rgb_matrix, box_size=100, output_path='color.png'):
    """
    Generate an image from a nxn RGB matrix where each box is box_size x box_size pixel box

    Parameters:
    - rgb_matrix (list of list of tuples): nxn matrix containing RGB tuples
    - box_size (int): The size of each box in pixels. Default is 100
    - output_path (str): The path to save the generated image. Default is 'color.png'
    """
    n = len(rgb_matrix)

    if os.path.exists(output_path):
        os.remove(output_path)

    # Create a new image
    image_size = n * box_size
    image = Image.new('RGB', (image_size, image_size), 'white')
    draw = ImageDraw.Draw(image)

    # Create the color boxes
    for i in range(n):
        for j in range(n):
            color = rgb_matrix[i][j]
            top_left = (j * box_size, i * box_size)
            bottom_right = ((j + 1) * box_size, (i + 1) * box_size)
            draw.rectangle([top_left, bottom_right], fill=color)

    # Save the image to a file
    image.save(output_path)
    print(f"Image saved to {output_path}")

def convert_image_to_rgb_matrix(file: str, size:int) -> list[list[tuple[int, int, int]]]:
    """
    Convert an image to a nxn RGB matrix where each box is nxn pixel box

    Parameters:
    - file (str): The path to the image file

    Returns:
    - list of list of tuples: nxn matrix containing RGB tuples
    """
    image = Image.open(file)
    image = image.convert('RGB')
    n = image.width // size
    rgb_matrix = [[image.getpixel((j * size, i * size)) for j in range(n)] for i in range(n)]
    return rgb_matrix


def is_same_matrix(matrix1, matrix2):
    """
    Check if two matrices are the same

    Parameters:
    - matrix1 (list of list of tuples): nxn matrix containing RGB tuples
    - matrix2 (list of list of tuples): nxn matrix containing RGB tuples

    Returns:
    - bool: True if the matrices are the same, False otherwise
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]): return False
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True


# Example of use
# rgb_matrix = [
#     [(255, 0, 0), (255, 60, 0), (255, 120, 10), (255, 206, 12)],
#     [(255, 0, 255), (0, 255, 255), (255, 255, 255), (255, 128, 128)],
#     [(128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0)],
#     [(0, 128, 128), (128, 0, 128), (192, 192, 192), (3, 227, 252)]
# ]