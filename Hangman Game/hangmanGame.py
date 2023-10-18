import random
from words import words
import string

def getvalidword(words):
    # Randomly chooses something from the list (words.py)
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=getvalidword(words)
    #Letters in word
    wordletter=set(word)
    alphabet= set(string.ascii_uppercase)
    #User's guess
    usedletter= set()

    lives=6

    #User input
    while len(wordletter) >0 and lives>0:
        #Letters used
        print('You have', lives, 'lives left and you have used these letter: ',' '.join(usedletter))

        #Current Word
        wordlist= [letter if letter in usedletter else  '-' for letter in word]
        print('Current word: ', ' '.join(wordlist))

        userletter= input("Guess Letter: ").upper()
        if userletter in alphabet - usedletter:
            usedletter.add(userletter)
            if userletter in wordletter:
                wordletter.remove(userletter)

            else:
                #Take away one life
                lives=lives-1
                print('Letter is not the word. ')
        elif userletter in usedletter:
            print('You have Already used it. Please try again')
        else:
            print('Inavlid charecter. Please try again')
    if lives==0:
        print('You have not mores lives left. The word was', word)
    else:
        print('You guessed right', word,'!!' )
hangman()