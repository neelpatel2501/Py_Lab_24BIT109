data = [(), (1, 2), (), (3,), (4, 5, 6), ()]
filtered = [t for t in data if t]
print("After removing empty tuples:", filtered)
