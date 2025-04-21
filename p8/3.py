names = set()

print("Enter 5 names:")
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.add(name)

print("Names after adding 5:", names)

old_name = input("Enter the name you want to modify: ")
if old_name in names:
    new_name = input(f"Enter the new name to replace '{old_name}': ")
    names.remove(old_name)
    names.add(new_name)
else:
    print(f"Name '{old_name}' not found.")

print("Names after modification:", names)

for i in range(2):
    del_name = input(f"Enter name {i+1} to delete: ")
    if del_name in names:
        names.remove(del_name)
    else:
        print(f"Name '{del_name}' not found.")

print("Final names in the set:", names)
