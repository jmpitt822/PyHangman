import Gameboard


def makeAGuess(triesRemaining):
    guess = input()
    if guess in wordGuessArray:
        for x in range(len(wordGuessArray)):
            if guess == wordGuessArray[x]:
                wordArray[x] = guess
        print(wordArray)
        print("Correct!")
        return triesRemaining
    else:
        triesRemaining -= 1
        if triesRemaining >= 1:
            print("Wrong. Try again. You have", triesRemaining, "tries remaining.")
            return triesRemaining


wordToGuess = "bicycle"
wordGuessArray = list(wordToGuess)
wordArray = ["_", "_", "_", "_", "_", "_", "_", ]
x = 10
print("Welcome to hangman!\nPlease enter a letter to guess the word.")
print(wordArray)
while "_" in wordArray and x is not None:
    x = makeAGuess(x)
    # Gameboard.printGameBoard(x)
if "_" not in wordArray:
    print("You got it!")
elif x is None:
    print("Game Over")
