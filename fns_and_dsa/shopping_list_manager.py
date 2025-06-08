shopping_list = []

def add_item(item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    print(f"Added '{item}' to the shopping list.")

def remove_item(item):
    """Remove an item from the shopping list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

def view_list():
    if shopping_list:
        print("Shopping List:")
        for  item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")