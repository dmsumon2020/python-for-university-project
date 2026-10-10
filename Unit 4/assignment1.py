cups_sold = 200 

def update_sales(): 
        cups_sold = 250 
        print("Local cups sold:", cups_sold) 
        print("Global cups sold:", globals()["cups_sold"]) 
        
update_sales()
