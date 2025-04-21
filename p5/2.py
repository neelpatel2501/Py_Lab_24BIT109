import random
nums = [random.randint(1, 10) for _ in range(20)]
print("List:", nums)
n = int(input("Enter number to search: "))
positions = [i for i, x in enumerate(nums) if x == n]
print("Positions:", positions)
