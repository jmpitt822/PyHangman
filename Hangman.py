import Gameboard
import WordPicker


def makeAGuess(decrementTries):
    guess = input()
    if guess in wordGuessArray:
        for x in range(len(wordGuessArray)):
            if guess == wordGuessArray[x]:
                wordArray[x] = guess
        print("Guessed Letters:", wrongGuesses)
        print(wordArray)
        print("Correct!")
        return decrementTries
    else:
        wrongGuesses.append(guess)
        decrementTries -= 1
        if decrementTries >= 1:
            print("Wrong. Try again. You have", decrementTries, "tries remaining.")
            print("Guessed Letters:", wrongGuesses)
            print(wordArray)
            return decrementTries


wordToGuess = WordPicker.selectRandomWord()
wordGuessArray = list(wordToGuess)
wordArray = WordPicker.randomWordArray(wordToGuess)
triesRemaining = 10
wrongGuesses = []
print("Welcome to hangman!\nPlease enter a letter to guess the word.")
print(wordArray)
Gameboard.printGameBoard(triesRemaining)
while "_" in wordArray and triesRemaining is not None:
    triesRemaining = makeAGuess(triesRemaining)
    Gameboard.printGameBoard(triesRemaining)
if "_" not in wordArray:
    print("You got it!")
elif triesRemaining is None:
    print("Game Over! The word was ", wordToGuess, ".", end="")
