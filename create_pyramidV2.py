import math

def every_decimal(a):
    a = str("{:.200f}".format(a)).split("0000")[0]
    return a

class Pyramid:
    def __init__(self, base_length, height, num_sides):
        self.base_length = base_length
        self.height = height
        self.num_sides = num_sides

    def volume(self):
        return (1 / 3) * self.base_length ** 2 * self.height

    def surface_area(self):
        base_area = self.base_length ** 2
        side_area = self.base_length * self.num_sides * self.height / 2
        return base_area + side_area

def calculate_blocks_for_pyramid(pyramid, block_length, block_width, block_height):
    # Calculate the volume of one block
    block_volume = block_length * block_width * block_height

    # Calculate the total surface area of the pyramid
    pyramid_surface_area = pyramid.surface_area()

    # Calculate the number of blocks required
    num_blocks = pyramid_surface_area / block_volume

    return num_blocks

# Get user input for pyramid dimensions
base_length = float(input("Enter the base length of the pyramid (in meters): "))
height = float(input("Enter the height of the pyramid (in meters): "))
num_sides = int(input("Enter the number of sides of the pyramid: "))

# Validate user input
if base_length <= 0 or height <= 0 or num_sides <= 0:
    print("Invalid input. Dimensions must be greater than zero.")
else:
    # Define the dimensions of one block (in meters)
    block_length = float(input("Enter the length of one block (in meters): "))
    block_width = float(input("Enter the width of one block (in meters): "))
    block_height = float(input("Enter the height of one block (in meters): "))

    # Create an instance of a pyramid with user-provided dimensions
    user_pyramid = Pyramid(base_length, height, num_sides)

    # Calculate the number of blocks needed
    blocks_needed = calculate_blocks_for_pyramid(user_pyramid, block_length, block_width, block_height)

    # Calculate the slope angle
    slope_angle_degrees = math.degrees(math.atan(user_pyramid.height / (user_pyramid.base_length / 2)))

    # Display the results
    print("Number of Blocks Needed:", every_decimal(blocks_needed))
    print("Pyramid Volume:", every_decimal(user_pyramid.volume()))
    print("Pyramid Slope Angle (degrees):", every_decimal(slope_angle_degrees))
