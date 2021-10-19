# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:22:33 2020

@author: user
"""

Guesses=8
    n=len(secretWord)
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is", n, " letters long.")
    print(" _ _ _ _ _ _ " )
    print("You have 8 guesses left.")
    totalguess=" "
    print("Available Letters: ", getAvailableLetters(totalguess) )
    n=str(input("Please guess a letter:"))
    while Guesses<=8:
        k=n.lower()
        if k in totalguess:
           print("Oops! you have entered this letter already!", getGuessedWord(secretWord, totalguess))
           print(" _ _ _ _ _ _ " )
           print("You have", Guesses, "guesses left.")
           print("Available Letters: ", getAvailableLetters(totalguess))
           n=str(input("Please guess a letter:"))
        elif k in secretWord:
           totalguess+=k
           Guesses=Guesses-1
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
            print("You have", Guesses, "guesses left.")
            print("Available Letters: ", getAvailableLetters(totalguess))
            n=str(input("Please guess a letter:"))
        