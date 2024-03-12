packs_pens = int(input())
packs_markers = int(input())
cleaning_solution = int(input())
discount = int(input())

pens_price = packs_pens * 5.80
markers_price = packs_markers * 7.20
solution_price = cleaning_solution * 1.20
price_before_discount = pens_price + markers_price + solution_price
money_needed = price_before_discount - (price_before_discount * (discount / 100))

print(money_needed)
