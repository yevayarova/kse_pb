def is_valid_price(value):
    return isinstance(value, (int, float)) and value > 0

def is_valid_quantity(value):
    return isinstance(value, int) and value >= 0

def format_currency(amount):
    return f"{amount:.2f} грн"