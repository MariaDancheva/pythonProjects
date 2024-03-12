aquarium_length = int(input())
aquarium_width = int(input())
aquarium_height = int(input())
occupied_space_percentage = float(input()) / 100

full_capacity = (aquarium_length * aquarium_width * aquarium_height) / 1000 #to transform it from cubic cm to meters
capacity = (full_capacity - full_capacity * occupied_space_percentage)

print(capacity)