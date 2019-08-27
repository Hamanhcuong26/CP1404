"""
Replace the contents of this module docstring with your own details
Name: Ha Manh Cuong
Date started: 15/8/2019
GitHub URL: https://github.com/Hamanhcuong26/CP1404
"""

from operator import itemgetter


def print_menu():
    menu_str = """
    Travel Tracker 1.0 - by <Ha Manh Cuong>
    Menu:
    A - List of places
    B - Complete visited place
    C - Add new places
    Q - Quit
"""
    print(menu_str)

def get_input(valid_input):
    user_input = input(">>>").lower()
    if user_input not in valid_input:
        print("Invalid menu choice, please choose again")
    return user_input

def place_list():
    places_list.sort(key=itemgetter(2, 0))
    count = 0
    for row in places_list:
        count += 1
        print("{}. {} {} ({}) {}".format(count, row[0], row[1], row[2], row[3]))

def visited_places():
    places_list.sort(key=itemgetter(2,0))
    count = 0
    for row in places_list:
        count += 1
        print("{}. {} {} ({}) {}".format(count, row[0], row[1], row[2], row[3]))
    else:
       print("No unvisited places")

def loading_places():
    file_pointer = open("places.csv", "r")
    for each in file_pointer:
        places_list.append(each.replace("\n", "").split(","))
    file_pointer.close()




places_list = []
loading_places()


def add_places():
    new_place_name = input("Enter New Place Name")
    while len(new_place_name) <= 1:
        print("ERROR! REQUIRES MORE THAN 2 CHARACTER")
        add_places()

    new_country = input("\nEnter New Country\n")
    while len(new_country) <= 1:
        print("ERROR! REQUIRES MORE THAN 2 CHARACTER")
        add_places()

    new_priority = input("\nEnter New Priority\n")

    new_status = input("\nEnter status\n")
    if new_status != {"v", "n"}:
        print("Please re-input appropriate option")
    else:
        new_status = input("\nEnter status\n")

    result_1 = [new_place_name, new_country, new_priority, new_status]
    places_list.append(result_1)

    print("{} from {} with priority ({}) {} added to place list".format(new_place_name, new_country, new_priority, new_status))

def quit_place():
    out_file = open("places.csv", "w")
    for each in places_list:
        out_file.write(str(each) + "\n")
    out_file.close()

while True:
    print_menu()
    user_choice = get_input(["a", "b", "c", "d", "q"])
    if user_choice == "q":
        print("Goodbye! See you next time!")
        print(places_list)
        quit_place()
        break
    elif user_choice == "a":
        place_list()
    elif user_choice == "b":
        visited_places()
    elif user_choice == "c":
        add_places()