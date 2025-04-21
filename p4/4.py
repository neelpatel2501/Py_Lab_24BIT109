num = int(input("Enter a number: "))

# Prime Check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Perfect Number Check
def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Armstrong Number Check
def is_armstrong(n):
    num_str = str(n)
    length = len(num_str)
    total = sum(int(digit) ** length for digit in num_str)
    return total == n

# Palindrome Check
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Automorphic Check
def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

print("Prime:", is_prime(num))
print("Perfect:", is_perfect(num))
print("Armstrong:", is_armstrong(num))
print("Palindrome:", is_palindrome(num))
print("Automorphic:", is_automorphic(num))
