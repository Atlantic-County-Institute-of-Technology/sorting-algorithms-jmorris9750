import random
import os
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

def find_numbers():
    try:
        find_range = int(input("how many numbers would you like in the list? :"))
        find_min = int(input("what's the lowest number you'd like? :"))
        find_max = int(input("what's the highest number you'd like? :"))

    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("invalid")

def options(find_min,find_max,find_range):

    numbers = [random.randint(find_min, find_max) for x in range(find_range)]
    try:
        print(
            "[-] 0.Exit \n"
            "[-] 1.bubble sort \n"
            "[-] 2.insertion sort \n"
            "[-] 3.selection sort")
        # user inputs option #
        selection = int(input("please select an option:"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if selection == 1:
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {bubble_sort(numbers)}")

        elif selection == 2:
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {insertion_sort(numbers)}")

        elif selection == 3:
            print(f"Unsorted values:{numbers}")
            print(f"sorted values {selection_sort(numbers)}")

    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("invalid")

def main_menu():

    while True:
        try:
            find_range = int(input("how many numbers would you like in the list? :"))
            find_min = int(input("what's the lowest number you'd like? :"))
            find_max = int(input("what's the highest number you'd like? :"))
            options(find_min,find_max,find_range)
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid")

        try:
            print(
                "0. Yes \n"
                "1. No \n")


main_menu()
