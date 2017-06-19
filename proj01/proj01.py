# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


print "Hello User!"
x = raw_input("What is your name?:")
first_letter=x[0].upper()
mid_slice=x[1:1000].lower()
t= first_letter + mid_slice
y = raw_input("How old are you?:")
h = raw_input("Please enter the year:")
d = raw_input("Have you had your birthday this year yet?")
z = 100-int(y)+int(h)
if d=="no" or d=="No" or d=="NO" or d=="nope" or d=="Nope" or d=="NOPE":
    print (t), ", you will turn 100 in the year" ,(z - 1), "."
elif d=="yes" or d=="Yes" or d=="YES":
    print (t), ", you will turn 100 in the year" ,(z), "."
else:
    print "The above question is a yes or no question only."
    d= raw_input ("Have you had your birthday this year yet?")
    if d == "no" or d == "No" or d == "NO" or d == "nope" or d == "Nope" or d == "NOPE":
        print (t), ", you will turn 100 in the year", (z - 1), "."
    elif d == "yes" or d == "Yes" or d == "YES":
        print (t), ", you will turn 100 in the year", (z), "."
    else:
        print "The above question is a yes or no question only, and I already gave you the chance to retry. You only get one second chance. You have Failed a survey. That is just sad."



if int(y)<10:
    s= raw_input("Can you watch PG movies?")
    if s=="yes" or s=="Yes" or s=="YES" or s=="yeah" or s=="Yeah" or s=="YEAH":
        r = raw_input("Can you watch PG-13 movies?")
    else:
        print "You are now finished with this survey. Thank you very much!"
elif int(y)>9 and int(y)<17:
    r= raw_input("Can you watch PG-13 movies?")
    if r=="yes" or r=="Yes" or r=="YES" or r=="yeah" or r=="Yeah" or r=="YEAH":
        n= raw_input ("Can you watch R movies?")
        if n=="yes" or n=="Yes" or n=="YES" or n=="yeah" or n=="Yeah" or n=="YEAH" or n == "no" or n == "No" or n == "NO" or n == "nope" or n == "Nope" or n == "NOPE":
            print "Congrats! You are finished!"


