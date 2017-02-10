import Gameboard

def makeAGuess(triesRemaining):
    guess = input()
    if guess in wordGuessArray:
        for x in range(len(wordGuessArray)):
            if guess == wordGuessArray[x]:
                wordArray[x] = guess
                print(wordArray)
                print("Correct!")
    else:
        triesRemaining -= 1
        print("Wrong. Try again. You have", triesRemaining, "tries remaining.")

wordToGuess = "bicycle"
wordGuessArray = list(wordToGuess)
wordArray = ["_", "_", "_", "_", "_", "_", "_", ]
triesRemaining = 10
print("Welcome to hangman!\n Please enter a letter to guess the word.")
print(wordArray)
while "_" in wordArray and triesRemaining > 0:
    makeAGuess(triesRemaining)
    # Gameboard.printGameBoard(triesRemaining)
if "_" not in wordArray:
    print("You got it!")
elif triesRemaining == 0:
    print("Game Over")
