def printGameBoard(triesRemaining):
    if triesRemaining == 10:
        gameboard = "<No Danger>"
    elif triesRemaining == 9:
        gameboard = "<Rope>"
    elif triesRemaining == 8:
        gameboard = "<Head>"
    elif triesRemaining == 7:
        gameboard = "<Left Arm>"
    elif triesRemaining == 6:
        gameboard = "<Left Body>"
    elif triesRemaining == 5:
        gameboard = "<Right Body>"
    elif triesRemaining == 4:
        gameboard = "<Right Arm>"
    elif triesRemaining == 3:
        gameboard = "<Left Leg>"
    elif triesRemaining == 2:
        gameboard = "<Left Foot>"
    elif triesRemaining == 1:
        gameboard = "<Right Leg>"
    else:
        gameboard = "<Right Foot>"

    print(gameboard)
