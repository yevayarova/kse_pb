def show_inventory(inventory):
    print("--- Облік товарів ---")
    for name, data in inventory.items():
        print(f"{name}: {data['quantity']} шт. за {data['price']} грн")