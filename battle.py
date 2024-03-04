import random

def intro_battle():
    #Tutorial for the battle
    def playerTurn():
        pass

    def bossTurn():
        pass
    class Boss:
        name = 'Boss'
        atk = 5
        type = 'Poison'
        rarity = 'Basic'
        hp = 25

    bossintro = Boss

    print(f"Player vs {bossintro.name}")

    choiceOfTurn = random.randint(1,2)
    if choiceOfTurn == 1:
        firstPick = 'player'
    else:
        firstPick = 'boss'

    if firstPick == 'player':
        while True:
            playerTurn()
            bossTurn()
    else:
        while True:
            bossTurn()
            playerTurn()




