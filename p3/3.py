str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if str2 in str1:
    print(f"'{str2}' is present in '{str1}'")
else:
    print(f"'{str2}' is not present in '{str1}'")
