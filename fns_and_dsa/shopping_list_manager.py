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
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                item = input("Enter the item to add:  ")
                
                shopping_list.append(item)
                print(f"{item} has been added to the shopping list and the updated shopping list is {shopping_list}")
            elif choice == 2:
                item = input("Enter the item name to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from the shopping list.")
                else:
                    print(f"{item} not found in the shopping list.")
            elif choice == 3:
                if len(shopping_list) == 0:
                    print("The shopping list is currently empty.") 
                else:
                    print(f"The shopping list is {shopping_list}")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Valueerror:
            print("You have entered an invalid input.")
    
           
if __name__ == "__main__":
    main()
