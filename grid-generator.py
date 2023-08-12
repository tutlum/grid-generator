from PIL import Image
import sys

def split_and_stick(image_path, n, m, spacing, background_color, ratio = 0):
    # Open the image
    image = Image.open(image_path)
    
    # Get the width and height of the image
    width, height = image.size
    
    # Calculate the width and height of each grid cell
    cell_width = width / n
    cell_height = height / m

    if (ratio != 0):
        ratio = height / width
    
    # Create a new image to store the result
    result_width = width + (n - 1) * spacing
    result_height = int(height + (m - 1) * spacing*ratio)
    result = Image.new('RGB', (result_width, result_height), background_color)
    
    # Iterate over each grid cell and paste it into the result image
    for i in range(n):
        for j in range(m):
            left = int(i * cell_width)
            upper = int(j * cell_height)
            right = left + cell_width
            lower = upper + cell_height
            
            cell = image.crop((left, upper, right, lower))
            result.paste(cell, (left+i*spacing, int(upper+j*spacing*ratio)))
    
    return result

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <image_path> <horizontal_cells> <vertical_cells> <spacing> [<spacing_ratio>]")
        sys.exit(1)

    input_image_path = sys.argv[1]
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    spacing = int(sys.argv[4])
    ratio = 0
    if len(sys.argv) == 6:
        ratio = int(sys.argv[5])
    #input_image_path = "input_image.jpg"  # Replace with your image path
    #n = 3  # Number of columns in the grid
    #m = 2  # Number of rows in the grid
    #spacing = 10  # Spacing between image parts
    
    background_color = (255, 255, 255)  # White background color
    
    output_image = split_and_stick(input_image_path, n, m, spacing, background_color, ratio)
    output_image.save(f"output_image_{n}x{m}-s{spacing}.jpg")  # Save the result
