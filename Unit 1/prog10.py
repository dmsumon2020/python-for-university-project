# Café menu using a basic dictionary
menu = {
    "cappuccino": 5.00,
    "coffee": 3.00,
    "sandwich": 7.00
}

# Availability tracking
cappuccino_available = True
coffee_available = True
sandwich_available = False

customer_name = input("Enter your name: ")
item_name = input("Enter the menu item: ").lower()
quantity = int(input("Enter quantity: "))

if item_name == "cappuccino":
    if cappuccino_available:
        price = menu["cappuccino"]
        total_cost = price * quantity
        print(f"Customer {customer_name} is buying {quantity} {item_name}. Total cost: ${total_cost:.2f}")
    else:
        print(f"Sorry, {item_name} is currently unavailable.")

elif item_name == "coffee":
    if coffee_available:
        price = menu["coffee"]
        total_cost = price * quantity
        print(f"Customer {customer_name} is buying {quantity} {item_name}. Total cost: ${total_cost:.2f}")
    else:
        print(f"Sorry, {item_name} is currently unavailable.")

elif item_name == "sandwich":
    if sandwich_available:
        price = menu["sandwich"]
        total_cost = price * quantity
        print(f"Customer {customer_name} is buying {quantity} {item_name}. Total cost: ${total_cost:.2f}")
    else:
        print(f"Sorry, {item_name} is currently unavailable.")

else:
    print("Sorry, that menu item is not on the menu.")