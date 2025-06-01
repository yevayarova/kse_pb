import random
import string

def generate_password(length=12, allow_symbols=False):
 
    base_characters = string.ascii_letters + string.digits
    if allow_symbols:
        base_characters += string.punctuation
    password_chars = []
    for znak in range(length):
        random_znak = random.choice(base_characters)
        password_chars.append(random_znak)

    password = ''.join(password_chars)

    return password

print(generate_password(length=12, allow_symbols=True))