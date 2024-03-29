# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
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
    result=False
    for l in secretWord:  
        if l in lettersGuessed:      
            result=True
        else:
            return False
    return result



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=('')
    for l in secretWord:  
        if l in lettersGuessed:      
            result+=l
        else:
               result+=' _ '
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    Alphabets= string.ascii_lowercase
    R= ""
    for l in Alphabets:
        if l not in lettersGuessed:
          R=R+l   
    return R
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    Guesses=8
    n=len(secretWord)
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is", n, " letters long.")
    print(" _ _ _ _ _ _ " )
    print("You have 8 guesses left.")
    totalguess=" "
    print("Available Letters: ", getAvailableLetters(totalguess) )
    n=str(input("Please guess a letter:"))
    while Guesses>0:
        k=n.lower()
        if k in totalguess:
           print("Oops! you have entered this letter already!", getGuessedWord(secretWord, totalguess))
           print(" _ _ _ _ _ _ " )
           print("You have", Guesses, "guesses left.")
           print("Available Letters: ", getAvailableLetters(totalguess))
           n=str(input("Please guess a letter:"))
        elif k in secretWord:
           totalguess+=k
           print("Good guess: ", getGuessedWord(secretWord, totalguess))
           print(" _ _ _ _ _ _ " )
           if isWordGuessed(secretWord, totalguess)==True:
                   print("Congratulations, you won!")
                   break
           else:
                  print("You have", Guesses, "guesses left.")
                  print("Available Letters: ", getAvailableLetters(totalguess))
                  n=str(input("Please guess a letter:"))
        elif k not in secretWord:
            totalguess+=k
            Guesses=Guesses-1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, totalguess))
            print(" _ _ _ _ _ _ " )
            if Guesses==0:
                print("Sorry, you ran out of guesses. The word was ", secretWord)
                break
            else:
                print("You have", Guesses, "guesses left.")
                print("Available Letters: ", getAvailableLetters(totalguess))
                n=str(input("Please guess a letter:"))
            
                
    
      


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
