def makeAGuess():
    guess = input()
    if guess in wordGuessArray:
        for x in range(len(wordGuessArray)):
            if guess == wordGuessArray[x]:
                wordArray[x] = guess
    else:
        print("Wrong. Try again.")

wordToGuess = "bicycle"
wordGuessArray = list(wordToGuess)
wordArray = ["_", "_", "_", "_", "_", "_", "_", ]
print("Welcome to hangman!\n Please enter a letter to guess the word.")
print(wordArray)
while "_" in wordArray:
    makeAGuess()
    print(wordArray)
print("You got it!")