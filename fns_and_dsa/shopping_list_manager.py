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


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            # Display the shopping list
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()