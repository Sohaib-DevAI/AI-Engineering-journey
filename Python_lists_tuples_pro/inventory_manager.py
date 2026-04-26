def add_item():
    inventory = []
    brand_identity = ("Ellaf Fashion", "Pakistan")
    print(f"Welcome to {brand_identity[0]} {brand_identity[1]} Inventory Manager!")
    total_sales = 0
    while True:
        print("\nOptions: 1. Add Item 2. View Inventory 3. Sort 4. Top Stock 5. Remove Out of Stock 6. \nstats 7. clear 8. Search_Brand 9.Info 10. Lock 11. Exit")
        user_choice = input("Choose an option: (1-11) ")
        if user_choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            inventory.append((item_name, item_price))
            print(f"Added {item_name} at ${item_price:.2f} to inventory.")
        elif user_choice == '2':
            if not inventory:
                print("Inventory is empty.")
            else:
                for idx, (name, price) in enumerate(inventory, 1):
                    print(f"{idx}. {name} - ${price:.2f}")
        elif user_choice == '3':
            inventory.sort(key=lambda x: x[1])
            print("Inventory sorted by price.")
        elif user_choice == '4':
            top_item = inventory[:3]
            print("--Top 3 stock items--")
            for item in top_item:
                print(f"Premium Item: {item[0]}")
        elif user_choice == '5':
            out_of_stock = input("Enter out of stock brand name: ")
            for item in inventory:
                if item[0] == out_of_stock:
                    inventory.remove(item)
                    print(f"Removed {out_of_stock} from inventory.")
        elif user_choice == '6':
            if inventory:
                total_sales = sum(price for _, price in inventory)
                print(f"Total sales value: ${total_sales:.2f}")
            else:
                print("No items in inventory to calculate sales.")
        elif user_choice == '7':
            inventory.clear()
            print("Inventory cleared.")
        elif user_choice == '8':
            search_brand = input("Enter brand name to search: ")
            found_items = [item for item in inventory if item[0] == search_brand]
            if found_items:
                print(f"Items found for {search_brand}:")
                for item in found_items:
                    print(f"{item[0]} - ${item[1]:.2f}")
            else:
                print(f"No items found for {search_brand}.")
        elif user_choice == '9':
            print(f"Business Location: {brand_identity[1]}")
            print(f"Owner: Sohaib khan | Brand: {brand_identity[0]}")
        elif user_choice == '10':
            print("Inventory locked. No further changes allowed.")
            break
        elif user_choice == '11':
            print("Exiting Inventory Manager. Goodbye!")
            break
if __name__ == "__main__":
    add_item()

