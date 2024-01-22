from random import randint
import time

def cha():
    print("\n\n\nLets start by writing your name !\n")
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

    print("Choose your apptitude:\n1: Luckier\n2: Stronger\n3: Heavier\n")
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



name, boost = cha()

time.sleep(2)
print("Stranger - Hey...")
time.sleep(2)
print(f"Stranger - Wake up {name} !")
time.sleep(2)
print(f"{name} - Ahhhh ..")
time.sleep(3)
print(f"{name} - What is that ?")
time.sleep(2)










