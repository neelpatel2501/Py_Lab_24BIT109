input_str = input("Enter a string: ")
lowercase = ""
uppercase = ""
toggle = ""
for char in input_str:
    if 'A' <= char <= 'Z':
        lowercase += chr(ord(char) + 32)
        uppercase += char
        toggle += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        uppercase += chr(ord(char) - 32)
        lowercase += char
        toggle += chr(ord(char) - 32)
    else:
        lowercase += char
        uppercase += char
        toggle += char
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Toggled case:", toggle)
