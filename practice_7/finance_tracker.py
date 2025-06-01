def add_transaction(transactions, amount, transaction_type, category):
    transaction = {
        'amount': amount,
        'type': transaction_type,
        'category': category
    }
    transactions.append(transaction)

def get_balance(transactions):
    income = 0
    expenses = 0
    for trynk in transactions:
        if trynk['type'] == 'дохід':
            income += trynk['amount']
        elif trynk['type'] == 'витрата':
            expenses += trynk['amount']
    return income - expenses

transactions = []
add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "вкрали")
add_transaction(transactions, 1500, "витрата", "транспорт")

print(get_balance(transactions))
