main_string = input("Enter the main string: ")
remove_string = input("Enter the string to be removed: ")
if remove_string in main_string:
    result_string = main_string.replace(remove_string, "")
    print("String after removal:", result_string)
else:
    print(f"'{remove_string}' is not present in '{main_string}'")
