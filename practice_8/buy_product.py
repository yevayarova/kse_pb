from utils import is_valid_quantity, format_currency

def buy_product(inventory, transactions, name, quantity, seller_id):
    if name not in inventory or inventory[name]["quantity"] < quantity:
        print("Товар відсутній або недостатня кількість!")
        return 0.0
    
    total = inventory[name]["price"] * quantity
    inventory[name]["quantity"] -= quantity
    transaction = {
        "name": name,
        "quantity": quantity,
        "total": total,
        "seller_id": seller_id
    }
    transactions.append(transaction)
    print(f"Покупка {name}, {quantity} шт., сума: {format_currency(total)}")
    return total

def print_check(transactions, n=1):
    if len(transactions) < n:
        print("Транзакції відсутні.")
        return
    t = transactions[-n]
    print("--- Чек ---")
    print(f"Товар: {t['name']}")
    print(f"Кількість: {t['quantity']}")
    print(f"Сума: {format_currency(t['total'])}")
    print(f"ID продавця: {t['seller_id']}")
    print("-------------")
