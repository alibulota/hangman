print ("Welcome to Animal Hangman!")

words = ['dog', 'cat', 'bird', 'hamster', 'gerbil']

i = int(raw_input("Choose a number 0-4 to select a word from the list: "))
print "Length of chosen word is", len(words[i]), "characters long."

incorrectGuesses = 0


while incorrectGuesses < 7:
    guess = str(raw_input("Guess a letter: "))
    if ((guess) in words[i]):
        print ('Good job! The letter "' + guess + '" appears in the word ' + str(words[i].count(str(guess))) + ' times.')
        incorrectGuesses = incorrectGuesses + 1
    else:
        print('Sorry, try again.')
        incorrectGuesses = incorrectGuesses + 1

print ("Game over. The word is:" , words[i])