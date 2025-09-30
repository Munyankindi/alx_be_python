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
            item_name = input("enter the Name of the item: ")
            shopping_list.append(item_name)
        elif choice == '2':
            remove_item = input("enter the name of the item to remove: ")
            for item in shopping_list:
                if remove_item == item:
                    shopping_list.remove(item)
        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
