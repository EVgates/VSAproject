# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
sprinkles= raw_input ("Do you want to play a guessing game?")
guesses = 5
number = random.randint(1, 99)
while (sprinkles=="yes" or sprinkles=="Yes" or sprinkles=="YES" or sprinkles=="yeah" or sprinkles=="Yeah" or sprinkles=="YEAH" or sprinkles=="Yep" or sprinkles=="yep" or sprinkles=="YEP" or sprinkles=="totally" or sprinkles=="sure" or sprinkles=="Totally" or sprinkles=="sure" or sprinkles=="Sure" or sprinkles=="maybe" or sprinkles=="Maybe" or sprinkles==" yes" or sprinkles==" yeah" or sprinkles==" Yes" or sprinkles==" y" or sprinkles=="y" or sprinkles=="Y" or sprinkles==" yeah" or sprinkles==" Y") and guesses>0:
    #number = random.randint(1, 99)
    frosting= int(raw_input ("Guess a number between 1 and 99"))

    if frosting==number:
        print "Good Job! You guessed it correctly."
        guesses= guesses+3
        sprinkles = raw_input("Do you want to play again?")
        number = random.randint(1, 99)
    elif frosting>number:
        print "Too high! Try again."
    elif frosting<number:
        print "Too low! Try again."
    #else:
        #print "Nice Try! Maybe you'll get it next time! The correct answer was",number,"."
        #sprinkles= raw_input ("Do you want to play again?")
    guesses = guesses -1
if frosting==number:
    print "Congrats, you guessed a random number correctly."
    glitter= raw_input("Would you like to keep playing?")


else:
    print "Sorry, you have run out of guesses, and you failed to guess correctly. Nice try, but the correct answer was", number,"."

