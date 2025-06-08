from data_folder.data import get_data, load_data


        
        
file_path = "kse_pb\practice_10\data_folder\cinema_halls.json"        
        
def create_hall(file_path):
    halls = get_data(file_path)
    new_hall_name = input("What is the name for new hall?")
    if new_hall_name in halls:
        print("Hall with this name already exist")
    else:
        num_rows = int(input("Enter number of rows: "))
        num_columns = int(input("Enter number of colums: "))
        new_hall_dict = {new_hall_name: []}
        for i in range(1, num_rows+1):
            for j in range(1,num_columns+1):
                seat_dict = {f"{i}-{j}": False}
                new_hall_dict[new_hall_name].append(seat_dict)
        halls.update(new_hall_dict)
    load_data(halls, file_path)


def show_empty_seats(file_path):
    halls = get_data(file_path)
    hall_name = input("Hall name? ")
    if hall_name not in halls:
        print("Hall is not existed")
    else:
        selected_hall = halls[hall_name]
        #2print(selected_hall)
        empty_seats = []
        for seat in selected_hall:
            for key, value in seat.items():
                if value is False:
                    empty_seats.append(key)
        print("Empty seats:", empty_seats)
        return empty_seats
        

    


while True:
    try:
        user_choice = int(input ("Enter your choice"))
    except Exception as e:
        print(e)
        user_choice = None
    if user_choice == 0:
        break
    elif user_choice == 1: 
        print ("You choose to add hall")
        create_hall(file_path)
    elif user_choice == 2:
        print("You choose to show empty seats")
        show_empty_seats(file_path)
    elif user_choice == 3: 
        print("You choose to book a seat")
    
    elif user_choice == 4:
        print("You choose to decline a reservation")















# from data import get_data, load_data  # переконайся, що ці функції імпортовані правильно

# def create_hall(file_path):
#     halls = get_data(file_path)
#     new_hall_name = input("What is the name for new hall? ")

#     if new_hall_name in halls:
#         print("Hall with this name already exists")
#     else:
#         num_rows = int(input("Enter number of rows: "))
#         num_columns = int(input("Enter number of columns: "))

#         new_hall_dict = {new_hall_name: []}
        
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 seat_id = f"{i}-{j}"  # правильний формат
#                 seat_dict = {seat_id: False}
#                 new_hall_dict[new_hall_name].append(seat_dict)

#         halls.update(new_hall_dict)
#         load_data(halls, file_path)
#         print(f"Hall '{new_hall_name}' created and saved successfully.")
# create_hall("kse_pb\practice_10\data_folder\cinema_halls.json")