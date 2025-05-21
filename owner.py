storage = []

def owner():
    for i in range(5):
        items=input("enter items:")
        storage.append(items)
def customer():
    if storage:
        print("Available items:", storage)
    else:
        print("Storage is empty.")

def buy_item():
    item = input("Customer: Enter the item you want to buy: ").strip()
    if item in storage:
        storage.remove(item)
        print(item,"Delivered to customer")
    else:
        print("Sorry, item not available.")

def main():
    while True:
        print("\nOptions:\n1. Owner: Add items\n2. Customer: Show items\n3. Customer: Buy item\n4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            owner()
        elif choice == '2':
            customer()
        elif choice == '3':
            buy_item()
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()

