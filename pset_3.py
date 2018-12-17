# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(secretWord) & set(lettersGuessed) == set(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guesses = []
    for i in secretWord:
        if i in lettersGuessed:
            guesses.append(i)
        else:
            guesses.append("_ ")
    str_guesses = "".join(guesses)
    return str_guesses




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = string.ascii_lowercase
    return "".join(i for i in alphabet if i not in lettersGuessed)


def hangman(secretWord):

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print("-----------")

    mistakeMade = 8
    lettersGuessed = []

    while mistakeMade != 0:

        print("You have {} guesses left.".format(mistakeMade))

        print("Available letters:", getAvailableLetters(lettersGuessed))

        letter = input("Please guess a letter: ").lower()

        if letter in secretWord and letter not in lettersGuessed:
            lettersGuessed.append(letter)
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        elif letter not in secretWord and letter not in lettersGuessed:
            mistakeMade -= 1
            lettersGuessed.append(letter)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        else:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print("-----------")

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break

    if mistakeMade == 0:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
