ONE_WORK_PLACE = 70 * 120
UNUSABLE_DESK_SPACE = 3
HALLWAY = 100

room_length = float(input()) * 100   #to convert them in cm we multiply by 100
room_width = float(input()) * 100 - HALLWAY # 1m = 100cm

work_places_per_row = room_width // 70
work_places_per_column = room_length // 120
work_places_capacity = work_places_per_row * work_places_per_column - 3

print("%.d" % work_places_capacity)