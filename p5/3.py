import random
nums = [random.randint(1, 30) for _ in range(50)]
unique_nums = list(set(nums))
print("Original List:", nums)
print("Without Duplicates:", unique_nums)
