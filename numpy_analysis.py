import numpy as np

products = ["Wheat", "Rice", "Dates", "Milk", "Sugar"]
weeks = ["Opening", "Week 1", "Week 2", "Week 3"]
stock = np.array([[500, 509, 518.8, 511.2],
                  [420, 420.8, 428.1, 426],
                  [300, 322.9, 279.1, 90.0],
                  [650, 638.1, 668.6, 672.2],
                  [800, 813.4, 809.7, 813.2]])

product_means = np.round(np.mean(stock, axis=1), 1)
print("Product averages:", product_means)
week3 = stock[:, 3]
print("Lowest:", products[np.argmin(week3)])
# Task 3: Products whose stock decreased since the opening
decreased = np.sum(stock[:, 3] < stock[:, 0])
print("Decreased:", decreased)

# Task 4: Total stock of all products in Week 3
total_week3 = np.sum(stock[:, 3])
print("Total Week 3:", total_week3)