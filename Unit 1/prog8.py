# ============================================
# Program: Café Order and Sales Management
# Description: Digitizes menu pricing, calculates totals,
#              and prints formatted customer receipts.
# ============================================

# Define fixed menu prices using a dictionary mapping item names to float prices
MENU = {
    "cappuccino": 5.00,
    "espresso": 3.00,
    "latte": 4.50,
    "muffin": 3.50,
}

# 1. Accept User Inputs
customer_name = input("Enter customer name: ").strip()
item_requested = input("Enter menu item: ").strip().lower()

# Validate quantity input to handle invalid integers gracefully
try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    print("Invalid quantity entered. Defaulting to 1.")
    quantity = 1

# Initialize running total
total_cost = 0.0

# 2. Process Order and Calculate Total Cost
if item_requested in MENU:
    unit_price = MENU[item_requested]

    # Calculate item subtotal using multiplication arithmetic operator (*)
    subtotal = unit_price * quantity

    # Accumulate total cost using Add AND assignment operator (+=)
    total_cost += subtotal

    # Display formatted purchase summary using formatted string literals (f-strings)
    # Specifying :.2f ensures monetary values are rounded to two decimal places
    print(
        f"\nCustomer {customer_name.capitalize()} is buying {quantity} "
        f"cup(s) of {item_requested}. Total cost: ${total_cost:.2f}"
    )
else:
    print(
        f"\nSorry, '{item_requested}' is not available on the menu."
    )