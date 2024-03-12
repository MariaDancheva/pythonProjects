nylon_needed = int(input()) + 2
paint_needed = int(input())
diluent_needed = int(input())
working_hours = int(input())

paint_needed += paint_needed * 0.1
nylon_price = nylon_needed * 1.50
paint_price = paint_needed * 14.50
diluent_price = diluent_needed * 5.00
materials_price = paint_price + nylon_price + diluent_price + 0.40
workers_payment_per_hour = materials_price * 0.30
workers_total_payment = workers_payment_per_hour * working_hours
total_expenses = materials_price + workers_total_payment

print(total_expenses)