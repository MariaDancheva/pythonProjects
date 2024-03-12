pages_in_current_book = int(input())
pages_read_per_hour = int(input())
number_days_to_finish_it = int(input())

hours_needed_to_finish = pages_in_current_book // pages_read_per_hour
hours_per_day = hours_needed_to_finish // number_days_to_finish_it

print(hours_per_day)