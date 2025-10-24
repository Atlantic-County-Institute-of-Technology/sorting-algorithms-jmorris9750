import random
import os
import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def loading_screen(sort_type):
    print(f"{sort_type}...")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{sort_type}..")
    time.sleep(0.35)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{sort_type}.")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{sort_type}")
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Done!")


# allows the user to pick how they want their list sorted
def options(find_min, find_max, find_range):
    numbers = [random.randint(find_min, find_max) for x in range(find_range)]
    try:
        print(
            "[-] 0.Back \n"
            "[-] 1.bubble sort \n"
            "[-] 2.insertion sort \n"
            "[-] 3.selection sort")
        # user inputs option #
        selection = int(input("please select an option:"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if selection == 1:
            loading_screen("Bubbling")
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {bubble_sort(numbers)}")

        elif selection == 2:
            loading_screen("Inserting")
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {insertion_sort(numbers)}")

        elif selection == 3:
            loading_screen("selecting")
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {selection_sort(numbers)}")

    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("invalid")


def main_menu():
    main_con = True
    while main_con:
        try:
            # allows the user to chose the range, max number, and minimum number for the list
            find_range = int(input("how many numbers would you like in the list? :"))
            find_min = int(input("what's the lowest number you'd like? :"))
            find_max = int(input("what's the highest number you'd like? :"))
            os.system('cls' if os.name == 'nt' else 'clear')

            # if the user picks a negative number, it makes them chose again
            if find_range > -1:
                options(find_min, find_max, find_range)

            else:
                print("range needs to be a positive number")

        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid")

        try:
            print(
                "\n"
                "0. Yes \n"
                "1. No \n")

            # allows the user to chose whether they want another sort or not
            try_again = int(input("do you want another sort? :"))

            # exits the code if they do not want another sort
            if try_again == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Then leave.")
                main_con = False

            # repeats the code if they want another sort
            elif try_again == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                main_menu()

        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid")


main_menu()
