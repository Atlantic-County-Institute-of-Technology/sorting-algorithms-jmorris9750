import random
import os
from bubble_sort import bubble_sort


numbers = [random.randint(1,100) for i in range(10)]



def main_menu():
    print(
        "[-] 0.Exit \n"
        "[-] 1.Add apples to count \n"
        "[-] 2.Make items \n"
        "[-] 3.reset your food and apples")
    try:
        # user inputs option #
        selection = int(input("please select an option:"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(numbers)
            #
            # outer_pass = 0
            # inner_pass = 0
            #
            print(f"sorted values {bubble_sort(numbers)}")

    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("invalid")
        main_menu()

main_menu()

# print(numbers)
# #
# # outer_pass = 0
# # inner_pass = 0
# #
# print(f"sorted values {bubble_sort(numbers)}")

