import random

def selectRandomWord():
    array = []
    with open("words.txt", "r") as f:
        for line in f:
            array.append(line.strip())

    x = random.randrange(1, 354939)
    randomWord = array[x]
    return randomWord

def randomWordArray(randomWord):
    randWordArray = []
    for x in range(len(randomWord)):
        randWordArray.append("_")
    return randWordArray
