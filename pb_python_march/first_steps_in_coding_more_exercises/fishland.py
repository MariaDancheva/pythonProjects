MUSSELS_PRICE_KG = 7.5

price_mackerel_kg = float(input())
price_sprat_kg = float(input())
belted_bonito_weight = float(input())
scad_weight = float(input())
mussels = float (input()) * MUSSELS_PRICE_KG

price_belted_bonito_kg = price_mackerel_kg * 1.6
price_scad_kg = price_sprat_kg * 1.8

total_price_scad = price_scad_kg *scad_weight
total_price_belted_bonito = belted_bonito_weight * price_belted_bonito_kg
bill = total_price_scad + total_price_belted_bonito + mussels

print("%.2f" % bill)