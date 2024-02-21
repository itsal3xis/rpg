from random import randint
from random import choice
import numpy as np

def intro_level():

    char = '~'

    tab = np.array(([char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,        #Basic Map / Maybe fixed
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char,
                    char,char,char,char,char,char,char,char,char,char]))
    tab = np.reshape(tab, (10,10))


    walls = 'X'
    for i in range(10):
        tab[0,i] = walls
        tab[i,0] = walls
        tab[9,i] = walls
        tab[i,9] = walls

    items = 'I'
    tab[randint(1, 8), randint(1, 8)] = items
    tab[randint(1, 8), randint(1, 8)] = items

    posItems = (np.where(tab == "I"))

    spawn_point = 'P'
    tab[randint(1,8), randint(1,8)] = spawn_point  #Maybe fixed for intro ?

    posPlayer = (np.where(tab == 'P'))

    boss = 'B'
    tab[randint(1, 8), randint(1, 8)] = boss

    posBoss = (np.where(tab == 'B'))

    print(tab)




intro_level()   #Remove after completion ----------------------------------------------------------------------------------------
                #Description github add CLI--------------------------------------------------------------------------------------
                #Add dialogue in the intro --------------------------------------------------------------------------------------