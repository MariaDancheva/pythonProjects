EURO = 1.94

vegetables_price_lv = float(input())
fruits_price_lv = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

income_vegetables_lv = total_kg_vegetables * vegetables_price_lv
income_fruits_lv = total_kg_fruits * fruits_price_lv
income_lv = income_fruits_lv + income_vegetables_lv
income_euro = income_lv / 1.94

print("%.2f" % income_euro)