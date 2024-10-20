import random

wordList = ["titan", "adieu", "king", "cruel", "fire"]
gameWord = wordList[random.randint(0, (len(wordList)-1))]
gameLetters = []
gameLetters.extend(gameWord) #splits the gameword into letters

userGuess = ""
guesses = 6 #how many chances the user gets


