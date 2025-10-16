import random
import os
from bubble_sort import bubble_sort
# from insertion_sort import insertion_sort

numbers = [random.randint(1, 100) for x in range(10)]


def clear_console():

    # Clears the console screen based on the operating system.
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


def main_menu():

    while True:
        print(
            "[-] 0.Exit \n"
            "[-] 1.bubble sort \n"
            "[-] 2.insertion sort \n"
            "[-] 3.selection sort")
        try:
            # user inputs option #
            selection = int(input("please select an option:"))



        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid")

        if selection == 1:
            clear_console()

            print(f"Unsorted values:{numbers}")
            print(f"sorted values {bubble_sort(numbers)}")

        elif selection == 2:
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {insertion_sort(numbers)}")

main_menu()
