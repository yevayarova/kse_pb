from utils import is_valid_price, is_valid_quantity

def add_product(inventory, name, price, quantity):
    if not is_valid_price(price) or not is_valid_quantity(quantity):
        return "Невірна ціна або кількість!"
        
    
    if name in inventory:
        inventory[name]["quantity"] += quantity
    else:
        inventory[name] = {"price": price, "quantity": quantity}
    print(f"Товар '{name}' додано/оновлено.")