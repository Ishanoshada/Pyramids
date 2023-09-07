import math

def every_decimal(a):
    a = str("{:.4f}".format(a))
    return a

def slope_angle(height, base_length):
    slope_angle_degrees = math.degrees(math.atan(height / (base_length / 2)))
    return every_decimal(slope_angle_degrees)

class Pyramid:
    def __init__(self, base_length, height):
        self.base_length = base_length
        self.height = height

    def volume(self):
        return (1 / 3) * self.base_length ** 2 * self.height

    def surface_area(self):
        base_area = self.base_length ** 2
        side_area = self.base_length * (2 * self.height)
        return base_area + side_area

# Create an instance of a pyramid
my_pyramid = Pyramid(230.4, 146.6)

# Calculate and print its volume, surface area, and slope angle
print("Pyramid Base Length:", my_pyramid.base_length)
print("Pyramid Height:", my_pyramid.height)
print("Pyramid Volume:", my_pyramid.volume())
print("Pyramid Surface Area:", my_pyramid.surface_area())
print("Pyramid Slope Angle:", slope_angle(my_pyramid.height, my_pyramid.base_length))
