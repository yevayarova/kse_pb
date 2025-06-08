import hashlib
from data import users
from data import emails
name = 0

def registration(users):
    login = input ("Please enter your login")
    password = input ("Please enter your password")
    password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
    if login in users:
        print("Username is already taken")
    else:
        users.update({login: password_hash})

def login(users):
    name = input("Enter name") 
    password = input("Password")
    password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
    if name not in users:
        print("USer is not registered")
    else:
        if password_hash == users[name]:
            print("you are logged in")
            return True, name
    return False, None


def logout():
    return False
def send_email(users,emails):
    sender = name
    recipient = input("enter resipient")
    mail = input("enter some text")
    if recipient not in users:
        print( "Recipient is not registrated")
    else:
        emails.append({"'sender": sender, "recipient": recipient, "email": mail})

user_status = False 

while True:
    try:
        user_choice = int(input ("Enter your choice"))
    except Exception as e:
        print(e)
        user_choice = None
    if user_choice == 0:
        break

    elif user_choice == 1: 
        print ("registration")
        if user_status is False:
            registration(users)
        else:
            print("You are already logged in")

    elif user_choice == 2:
        if user_status is False:
            user_status = login(users)
            print ("login")
        else:
            print("You are already logged in")
    
    elif user_choice == 3: 
        if user_status is True:
            send_email(users,emails)
            print ("send_email")
        else:
            print("You are not logged in to send email")
    
    elif user_choice == 4:
        if user_status is True:
            user_status = logout()
            print ("logout")
        else:
            print("You are not logged in to logout")
        
    elif user_choice == 5:
        print(users)
    elif user_choice == 6:
        print(emails)

        