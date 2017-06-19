# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == "Y":
    year= 2017

else:
    year= 2016
answer=year
for number in range (int(age), 101):
    answer = answer + 1
    print name, " will turn", int(age+1), "in the year ", int(answer), "."

print "done"
