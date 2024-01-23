from random import randint
import time
import os

def cha():
    print("\n\n\n\n\nLets start by writing your name !\n")
    name = str(input(">  "))

    invalid_car = ["!", "@", "#", "$", "%", "?", '&', '*', '(' , ')', '_', '=', '+', ':', ';', '"']

    for letter in name:
        if letter in invalid_car:
            if_invalid = False
            
            while if_invalid == False:
                print("Invalid name, choose another one ")
                name = input(">  ")
                if_invalid = True

    name = name[0].upper() + name[1:].lower()

    print("\nChoose your apptitude:\n1: Luckier\n2: Stronger\n3: Heavier\n")
    choice = int(input(">  "))

    while choice < 1 or choice > 3:
        print("Invalid choice, choose again")
        choice = int(input(">  "))

    if choice == 1:
        choice = "Luckier"
    elif choice == 2:
        choice = "Stronger"
    else:
        choice = "Heavier"

    return name, choice


def tutorial():
    os.system('cls')
    os.system('clear')
    time.sleep(2)
    print("Stranger - Hey...")
    time.sleep(2)
    print(f"Stranger - Wake up {name} !")
    time.sleep(2)
    print(f"{name} - Ahhhh ..")
    time.sleep(3)
    print(f"{name} - What is that ?")
    time.sleep(2)




name, boost = cha()
tuto = int(input("\n\nIs it your first time playing ?\n1: Yes\n2: No, skip the tutorial\n>  "))

while tuto < 1 or tuto > 2:
    tuto = int("\nSelect a valid option >  ")

if tuto == 1:
    tutorial()
else:
    os.system('cls')
    os.system('clear')














