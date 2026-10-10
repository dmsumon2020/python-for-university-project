cups_sold = 200 

def update_sales(): 
    cups_sold = 250 
    print("Local cups sold:", cups_sold) 
    print("Global cups sold:", globals()["cups_sold"]) 

update_sales() 

daily_orders = [120, 150, 180, 90, 200] 

daily_revenues = list(map(lambda cups: cups * 5, daily_orders)) 

highest_daily_sales = max(daily_orders) 

print("Daily revenues:", daily_revenues) 

print("Highest daily sales:", highest_daily_sales)
