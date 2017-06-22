# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
#def word1():


def hangman():
    print "Let's play hangman!"
    guesses=6
    print "You will have 6 passes for screwing up."
    word = choose_word(wordlist)
    length = len(word)
    print word
    print "The word you are trying to guess happens to be", length, "letters long."
    theList = []
    blanklist = []
    for letter in word:
        theList.append(letter)
    for letter in word:
        blanklist.append('_')
    while guesses>0:
        print " ".join(blanklist)
        g = raw_input ("Guess a letter ")
        guesslist=[]
        a = 0
        b = 0
        for letters in theList:

                for letter in g:
                    if theList[a]== g:
                        print "You got a letter right."
                        a=a+1
                        blanklist[b]=g
                        b=b+1
                    else:
                        if b>length:
                            print "You got the letter wrong. You failed."
                            guesslist.append(g)
                            print " ".join(guesslist)
                            guesses=guesses-1
                            print "You have",guesses,"guesses left."
                        else:
                            b= b+1
                            a= a+1







hangman()