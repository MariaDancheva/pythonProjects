yearly_tax = int(input())

basketball_shoes = yearly_tax * 0.6
basketball_jersey = basketball_shoes * 0.8
basketball_ball = basketball_jersey / 4
basketball_accessories = basketball_ball / 5

total_money_needed = yearly_tax + basketball_accessories + basketball_ball + basketball_jersey + basketball_shoes

print(total_money_needed)