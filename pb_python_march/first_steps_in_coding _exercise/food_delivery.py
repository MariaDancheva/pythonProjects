quantity_chicken_menu = int(input())
quantity_fish_menu = int(input())
quantity_vegetarian_menu = int(input())

price_chicken_menu = quantity_chicken_menu * 10.35
price_fish_menu = quantity_fish_menu * 12.4
price_vegetarian_menu = 8.15 * quantity_vegetarian_menu
price_menus_total = price_fish_menu + price_vegetarian_menu + price_chicken_menu
desert_price = price_menus_total * 0.2
total_price = price_menus_total + desert_price + 2.5

print(total_price)