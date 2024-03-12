GREEN_PAINT_LITER = 3.4
RED_PAINT_LITER = 4.3
DOOR = 1.2 * 2
WINDOWS = (1.5 * 1.5) * 2 #for both sides

house_height = float(input())
house_length = float(input())
roof_height = float(input())

front_back_area = (house_height * house_height) * 2 - DOOR
sides_area = (house_length * house_height) * 2
house_base = front_back_area + sides_area - WINDOWS
green_paint_needed = house_base / GREEN_PAINT_LITER

roof_triangle =  house_height * roof_height / 2
roof_area = sides_area + roof_triangle * 2
red_paint_needed = roof_area / RED_PAINT_LITER

print("%.2f" % green_paint_needed)
print("%.2f" % red_paint_needed)