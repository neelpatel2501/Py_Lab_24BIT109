num = int(input("Enter a number (0-19): "))
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
if 0 <= num <= 19:
    print(words[num])
else:
    print("Invalid number")