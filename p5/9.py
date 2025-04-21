list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4, 6]
list3 = [x for x in list1 if x not in list2]
print("List 1:", list1)
print("List 2:", list2)
print("List 3 (Only in List1):", list3)
