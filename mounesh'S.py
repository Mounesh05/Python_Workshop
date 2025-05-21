storage = []
delivered_items = []
def owner():
    for i in range(5):
        item = input("Enter the item: ").strip().upper()
        storage.append(item)
    print("Items added to storage.")

def customer():
    a = input("To check listed items enter YES/NO: ").strip().upper()  
    if a == "YES":
        print(storage)
    else:
        print("Don't come to this website if you are not interested.")
def buy_item():
    item = input("Enter the item you want to buy from the list: ").strip().upper()
    if item in storage:
        storage.remove(item)
        delivered_items.append(item)
        print(item, "delivered to customer!")
    else:
        print("when u have seen the listed item select from that list only")

def main():
    while True:
        print("\nWelcome to AM Logistics")
        print("1. Owner - Add items")
        print("2. Customer - View items")
        print("3. Buy an item")
        print("4. View Delivered Items")
        print("5. Exit")
        
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            owner()
        elif choice == 2:
            customer()
        elif choice == 3:
            buy_item()
        elif choice == 4:
            print("Delivered Items:", delivered_items)
        elif choice == 5:
            print("Exiting Website")
            break
        else:
            print("WHEN YOU KNOW THERE ARE 5 OPTION CHOOSE FROM THOSE 5 OPTION,DON'T PUT YOUR IMAGINARY NUMBER")

# Run the main function
main()