from random import randint, choice
import numpy as np
import battle

items = []
def intro_level():
    global items  # Declare 'items' as a global variable inside the function
    print("Welcome to the Dungeon Adventure Game!")
    print("You find yourself in a dark dungeon filled with mysteries and dangers.")
    print("Your objective is to navigate through the dungeon, collect treasures, defeat monsters, "
          "and ultimately defeat the final boss.")
    print("Here's your starting map:")

    # Generating the initial map
    char = '.'
    tab = np.array(([char] * 100))
    tab = np.reshape(tab, (10, 10))

    # Adding walls
    walls = '~'
    for i in range(10):
        tab[0, i] = walls
        tab[i, 0] = walls
        tab[9, i] = walls
        tab[i, 9] = walls

    # Adding items to the global 'items' list
    item = 'I'
    tab[randint(1, 8), randint(1, 8)] = item
    tab[randint(1, 8), randint(1, 8)] = item

    # Placing the player
    spawn_point = 'P'
    player_pos = [randint(1, 8), randint(1, 8)]
    tab[player_pos[0], player_pos[1]] = spawn_point

    # Placing the boss
    boss = 'B'
    tab[randint(1, 8), randint(1, 8)] = boss

    # Displaying the map
    print(tab)

    # Player control loop
    while True:
        move = input("Enter your move (up, down, left, right): ").lower()
        if (move == 'up' or move == 'w') and player_pos[0] > 1:
            tab[player_pos[0], player_pos[1]] = '~'
            player_pos[0] -= 1
            if tab[player_pos[0], player_pos[1]] == 'I':
                print("You found an item!")
                items.append(choice(['Sword', 'Shield', 'Potion']))
                print("Your items:", items)
            if tab[player_pos[0], player_pos[1]] == 'B':
                battle.intro_battle()
                break
            tab[player_pos[0], player_pos[1]] = spawn_point
        elif (move == 'down' or move == 's') and player_pos[0] < 8:
            tab[player_pos[0], player_pos[1]] = '~'
            player_pos[0] += 1
            if tab[player_pos[0], player_pos[1]] == 'I':
                print("You found an item!")
                items.append(choice(['Sword', 'Shield', 'Potion']))
                print("Your items:", items)
            if tab[player_pos[0], player_pos[1]] == 'B':
                battle.intro_battle()
                break
            tab[player_pos[0], player_pos[1]] = spawn_point
        elif (move == 'left' or move == 'a') and player_pos[1] > 1:
            tab[player_pos[0], player_pos[1]] = '~'
            player_pos[1] -= 1
            if tab[player_pos[0], player_pos[1]] == 'I':
                print("You found an item!")
                items.append(choice(['Sword', 'Shield', 'Potion']))
                print("Your items:", items)
            if tab[player_pos[0], player_pos[1]] == 'B':
                battle.intro_battle()
                break
            tab[player_pos[0], player_pos[1]] = spawn_point
        elif (move == 'right' or move == 'd') and player_pos[1] < 8:
            tab[player_pos[0], player_pos[1]] = '~'
            player_pos[1] += 1
            if tab[player_pos[0], player_pos[1]] == 'I':
                print("You found an item!")
                items.append(choice(['Sword', 'Shield', 'Potion']))
                print("Your items:", items)
            if tab[player_pos[0], player_pos[1]] == 'B':
                battle.intro_battle()
                break
            tab[player_pos[0], player_pos[1]] = spawn_point

        else:
            print("Invalid move. Try again.")
            continue

        print(tab)

