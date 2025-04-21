t = (1, 2, 3)
lst = list(t)
lst[1] = 99
t = tuple(lst)
print("Modified tuple:", t)
