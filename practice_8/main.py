from data import inventory
from add_product import add_product
from buy_product import buy_product, print_check
from inventory import show_inventory
from sellers import sellers, calculate_bonus

transactions = []

while True:
    print("Натисніть 1 - Додати товар\ 2 - Купити товар\ 3 - Переглянути облік\ 0 - Вийти з меню")
    action = input("Ваш вибір: ")

    if action == '1':
        name = input("Назва товару: ")
        price = float(input("Ціна: "))
        quantity = int(input("Кількість: "))
        add_product(inventory, name, price, quantity)

    elif action == '2':
        name = input("Назва товару: ")
        quantity = int(input("Кількість: "))
        seller_id = int(input("ID продавця: "))
        buy_product(inventory, transactions, name, quantity, seller_id)

    elif action == '3':
        show_inventory(inventory)

    elif action == '0':
        break

    else:
        print("Щось ви не те нвтиснули. Давайте знову, валідні варіанти:!")

bonuses = calculate_bonus(transactions)
print("\n--- Бонуси продавців ---")
for seller_id, bonus in bonuses.items():
    print(f"{sellers[seller_id]}: {bonus:.2f} грн")