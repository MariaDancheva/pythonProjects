deposit = float(input())
duration_of_deposit = int(input())
annual_interest_percentage = float(input())

money_at_the_end = deposit + duration_of_deposit*((deposit * annual_interest_percentage/100) / 12)

print(money_at_the_end)