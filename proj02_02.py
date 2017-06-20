# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
amount = int(raw_input("How many numbers do you wish to generate?"))
x=0
y=1
print y
while amount-1> 0:
    z = x + y
    print z
    x= y
    y= z
    amount= amount-1
print "Generation complete."

c = raw_input("Do you want to generate any more numbers?")
if c=="yes" or c=="Yes" or c=="Yeah" or c== "Yep" or c=="YES" or c=="yep" or c=="yeah" or c=="y" or c=="Y":
    dog = int(raw_input("How many numbers do you wish to generate this time?"))
    x=0
    y=1
    print y
    for number in range (1,dog):
        z = x+ y
        print z
        x= y
        y= z
        dog= dog + 1
    "Program complete."
elif c=="no" or c=="No" or c=="NO" or c=="Nope" or c=="nope":
    print "Program complete."
else:
    print "That is an unacceptable answer. Program incomplete."
