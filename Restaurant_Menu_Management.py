def add(menu, item):
    if item in menu:
        return f"'{item}' is already on the menu."
    else:
        menu.append(item)
        return f"'{item}' has been added to the menu."

def remove_items(menu, item):
    if item not in menu:
        return f"'{item}' is not in the menu."
    else:
        menu.remove(item)
        return f"'{item}' has been removed from the menu."

def check(menu, item):
    if item not in menu:
        return f"{item} is not available."
    else:
        return f"{item} is available."

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = input("Enter the item to add: ").strip()
while not add_item:
    add_item = input("Item cannot be empty. Please enter the item to add: ").strip()

remove_item = input("Enter the item to remove: ").strip()
while not remove_item:
    remove_item = input("Item cannot be empty. Please enter the item to remove: ").strip()

check_item = input("Enter the item to check: ").strip()
while not check_item:
    check_item = input("Item cannot be empty. Please enter the item to check: ").strip()

add_result = add(initial_menu, add_item)
remove_result = remove_items(initial_menu, remove_item)
availability_result = check(initial_menu, check_item)

print("\nUpdated menu:", initial_menu)
print(add_result)
print(remove_result)
print(availability_result)
