import csv

import_file = "import.csv"
export_file = "export.csv"
billing_file = "billing.csv"

class Owner:
    @staticmethod
    def create_inventory():
        with open(import_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Item", "Quantity", "Price"])
            n = int(input("Enter number of items: "))
            for _ in range(n):
                item = input("Enter item name: ")
                qty = int(input(f"Enter quantity for {item}: "))
                price = float(input(f"Enter price for {item}: "))
                writer.writerow([item, qty, price])
        print("Inventory created successfully.")

    @staticmethod
    def read_inventory():
        with open(import_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    @staticmethod
    def update_inventory():
        with open(import_file, "r") as file:
            reader = csv.reader(file)
            inventory = list(reader)

        header = inventory[0]
        data = inventory[1:]
        item_name = input("Enter the item to update: ")
        found = False

        for row in data:
            if row[0] == item_name:
                row[1] = str(int(input(f"Enter new quantity for {item_name}: ")))
                row[2] = str(float(input(f"Enter new price for {item_name}: ")))
                found = True
                break

        if found:
            with open(import_file, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(data)
            print("Inventory updated.")
        else:
            print("Item not found.")

    @staticmethod
    def delete_inventory():
        with open(import_file, "r") as file:
            reader = csv.reader(file)
            inventory = list(reader)

        header = inventory[0]
        data = inventory[1:]
        item_name = input("Enter the item to delete: ")

        updated_data = [row for row in data if row[0] != item_name]

        with open(import_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(updated_data)

        print("Item deleted successfully.")

class Dealer:
    @staticmethod
    def export_inventory():
        with open(import_file, "r") as infile, open(export_file, "w", newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)
        print("Inventory exported successfully.")

class Customer:
    @staticmethod
    def view_inventory():
        with open(export_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    @staticmethod
    def place_order():
        with open(export_file, "r") as file:
            reader = csv.reader(file)
            inventory = list(reader)

        header = inventory[0]
        data = inventory[1:]
        order = []
        total_cost = 0

        n = int(input("Enter number of items to order: "))
        for _ in range(n):
            item_name = input("Enter item name: ")
            quantity = int(input(f"Enter quantity for {item_name}: "))
            found = False

            for row in data:
                if row[0] == item_name and int(row[1]) >= quantity:
                    row[1] = str(int(row[1]) - quantity)
                    cost = float(row[2]) * quantity
                    total_cost += cost
                    order.append([item_name, quantity, cost])
                    found = True
                    break

            if not found:
                print(f"{item_name} is not available or insufficient stock.")

        with open(billing_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Item", "Quantity", "Total Price"])
            writer.writerows(order)
            writer.writerow(["Total Cost", "", total_cost])

        with open(export_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

        print("Order placed. Bill generated.")
        print("Updated inventory saved in export.csv.")

if __name__ == "__main__":
    while True:
        print("\n1. Owner Operations")
        print("2. Dealer Operations")
        print("3. Customer Operations")
        print("4. Exit")
        choice = int(input("Enter your role: "))

        if choice == 1:
            print("\n1. Create Inventory\n2. Read Inventory\n3. Update Inventory\n4. Delete Inventory")
            sub_choice = int(input("Choose operation: "))
            if sub_choice == 1:
                Owner.create_inventory()
            elif sub_choice == 2:
                Owner.read_inventory()
            elif sub_choice == 3:
                Owner.update_inventory()
            elif sub_choice == 4:
                Owner.delete_inventory()
            else:
                print("Invalid operation.")
        elif choice == 2:
            Dealer.export_inventory()
        elif choice == 3:
            print("\n1. View Inventory\n2. Place Order")
            sub_choice = int(input("Choose operation: "))
            if sub_choice == 1:
                Customer.view_inventory()
            elif sub_choice == 2:
                Customer.place_order()
            else:
                print("Invalid operation.")
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
