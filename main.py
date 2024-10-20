import random

wordList = ["titan", "adieu", "king", "cruel", "fire"]
gameWord = wordList[random.randint(0, (len(wordList)-1))]
gameLetters = []
gameLetters.extend(gameWord) #splits the gameword into letters

userGuess = ""
userLetters = []
userGuessedLetters = []
guesses = 6 #how many chances the user gets

while userGuess != gameWord and guesses > 0:
    print(f"the word is {len(gameWord)} letters long")
    print(f"you've currently guessed {userGuessedLetters} and have {guesses} guesses left")
    userChoice = int(input("1.would you like to guess the word? \n2.would you like to guess a letter?"))
    if userChoice == 1:
        userGuess = input("Put in the word you're guessing!")
