import numpy as np
# AgriChain: stock in tons - Wheat, Rice, Dates, Milk, Sugar (sample)
stock_tons = np.array([500, 420, 150, 650, 800])
print("Stock (tons):", stock_tons)
print("Average stock:", np.mean(stock_tons))
print("Highest stock:", np.max(stock_tons))
print("Lowest stock:", np.min(stock_tons))