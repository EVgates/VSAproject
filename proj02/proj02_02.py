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
while amount> 0:
    z = x + y
    print z
    x= y
    y= z
    amount= amount-1


for number in range (1,amount)
    z = x+ y
    print z
    x= y
    y= z
    amount= amount + 1