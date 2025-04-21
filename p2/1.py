a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest:", a)
    print("Smallest:", b)
elif b > a:
    print("Largest:", b)
    print("Smallest:", a)
else:
    print("Both numbers are equal.")
