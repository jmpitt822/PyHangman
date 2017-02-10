def printGameBoard(triesRemaining):
    if triesRemaining == 10:
        gameboard = "---------\n      |\n      |\n      |\n      |\n      |\n_________"
    elif triesRemaining == 9:
        gameboard = "---------\n   |  |\n      |\n      |\n      |\n      |\n_________"
    elif triesRemaining == 8:
        gameboard = "---------\n   |  |\n   () |\n      |\n      |\n      |\n_________"
    elif triesRemaining == 7:
        gameboard = "---------\n   |  |\n   () |\n  \   |\n      |\n      |\n_________"
    elif triesRemaining == 6:
        gameboard = "---------\n   |  |\n   () |\n  \|  |\n      |\n      |\n_________"
    elif triesRemaining == 5:
        gameboard = "---------\n   |  |\n   () |\n  \|| |\n      |\n      |\n_________"
    elif triesRemaining == 4:
        gameboard = "---------\n   |  |\n   () |\n  \||/|\n      |\n      |\n_________"
    elif triesRemaining == 3:
        gameboard = "---------\n   |  |\n   () |\n  \||/|\n   /  |\n      |\n_________"
    elif triesRemaining == 2:
        gameboard = "---------\n   |  |\n   () |\n  \||/|\n   /\ |\n      |\n_________"
    elif triesRemaining == 1:
        gameboard = "---------\n   |  |\n   () |\n  \||/|\n   /\ |\n  /   |\n_________"
    else:
        gameboard = "---------\n   |  |\n   () |\n  \||/|\n   /\ |\n  /  \|\n_________"

    print(gameboard)
