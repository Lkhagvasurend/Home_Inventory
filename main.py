from src.inventory_item import InventoryItem
import json
import os

inventory = None

while True:
    selected_menu = input("""
1. Start a new inventory
2. Read inventory from file
3. Save inventory to file
4. Add items to active inventory
5. Search inventory
6. Display inventory
7. Exit\n""")
    if selected_menu.isnumeric():
        selected_menu = int(selected_menu)
        if selected_menu == 1:
            inventory = []
            print("Inventory created")
        elif selected_menu == 2:
            if os.path.exists("data/inventory.json"):
                with open("data/inventory.json", "r") as file:
                    dict_inventory = json.load(file)
                inventory_item = [InventoryItem(name, item["price"], item["quantity"]) for name, item in dict_inventory.items()]
                if inventory is None:
                    inventory = []
                inventory.extend(inventory_item)
                print("Inventories read")
            else:
                print("JSON file does not exist")
        elif selected_menu == 3:
            dict_inventory = {item.name: {"price": item.price, "quantity": item.quantity} for item in inventory}
            json.dump(dict_inventory, open("data/inventory.json", "w"))
            print("Saved inventory to file")
        elif selected_menu == 4:
            if inventory is not None:
                name = input("Provide name")
                price = input("Provide price")
                quantity = input("Provide quantity")
                new_item = InventoryItem(name, price, quantity)
                inventory.append(new_item)
            else:
                print("Please create an inventory")
        elif selected_menu == 5:
            name = input("Search item by name")
            found_item = [item for item in inventory if item.name == name]
            if len(found_item) != 0:
                print("Name:", found_item[0].name, "\nPrice:", found_item[0].price, "\nQuantity:", found_item[0].quantity)
            else:
                print("Not found")
        elif selected_menu == 6:
            if inventory is None or inventory == []:
                print("Inventory empty")
            else:
                for item in inventory:
                    print("Name:", item.name, "Price:", item.price, "Quantity:", item.quantity)
        elif selected_menu == 7:
            break
        else:
            print("Select from 1-6")
    else:
        print("Select from 1-6")