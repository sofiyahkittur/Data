#Define the menu of the restaurant

menu = {
    'Cappuccino': 5,
    'Americano' : 4,
    'Affogato' : 6,
    'Latte' : 4,
    'Fresh Juice' : 4,
    'Sandwich' : 4,
    'Cookies' : 2,
}

#Greet
print("Welcome to Coffee & More")
print("Cappuccino: $5\nAmericano: $4\nAffogato: $6\nLatte: $4\nFresh Juice: $4\nSandwich: $4\nCookies: $2")

order_total = 0
#5 + 4 = 9

item_1 = input("Enter the nam of the item you want to order = ")

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"Ordered item {item_1} is not available")
    
another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input ("Enter the name of your second order")
    if item_2 in menu:
        order_total += menu[item_2]
    print(f"Item{item_2} has been added to order")
else:
    print(f"Ordered item {item_2} is not available")
    
print(f"The total amount of items to pay is {order_total}")
