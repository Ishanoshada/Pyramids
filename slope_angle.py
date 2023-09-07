import math

def every_decimal(a):
    a = str("{:.150f}".format(a)).split("0000")[0]
    return a
   
    

def slope_angle(height,base_length):
 slope_angle_degrees = math.degrees(math.atan(height / (base_length / 2)))
 return every_decimal(slope_angle_degrees)

