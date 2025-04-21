input_str = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in input_str:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")
