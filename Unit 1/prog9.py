# Café order program

customer_name = input("Enter customer name: ")
menu_item = input("Enter menu item: ").lower()
quantity = int(input("Enter quantity: "))

# Fixed menu prices
prices = {
    "cappuccino": 5.00,
    "coffee": 3.00,
    "tea": 2.50
}

# Calculate and display the order
if menu_item in prices:
    price = prices[menu_item]
    total_cost = price * quantity

    print(
        f"Customer {customer_name} is buying {quantity} "
        f"cups of {menu_item}. Total cost: ${total_cost:.2f}"
    )
else:
    print(f"Sorry, {menu_item} is not available on the menu.")