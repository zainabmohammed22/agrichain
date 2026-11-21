project = "AgriChain"
version = "0.1"
description = "Food stock tracking (sample data)"
print("Project:", project, "| Version:", version)
print("Description:", description)
 
stock_kg = 120       # dates in stock (sample)
daily_use_kg = 30    # used per day (sample)
days_left = stock_kg // daily_use_kg
print("Item: Dates | Stock (kg):", stock_kg)
print("Days left:", days_left)
if days_left < 7:
    print("Status: Reorder needed")
else:
    print("Status: Stock is OK")
