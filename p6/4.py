menu = [("Pizza", 250), ("Burger", 150), ("Pasta", 180), ("Fries", 100)]
menu.sort(key=lambda x: x[1], reverse=True)
print("Sorted menu:", menu)
