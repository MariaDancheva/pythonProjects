from math import pi

circular_radios = float(input())

area = pi * circular_radios * circular_radios
circumference = 2 * pi * circular_radios

print("%.2f" % area)
print("%.2f" % circumference)