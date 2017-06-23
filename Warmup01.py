# REVIEW: Conditionals, for loops, lists, and functions

#INSTRUCTIONS:

#PartI:

#Make the string "sentence_string" into a list called "sentence_list"
#Use a for loop and an append function like this: list.append(something)

sentence_string = raw_input("Enter a string to figure out which vowels are in it.")
first_letter=sentence_string[0].upper()
mid_slice=sentence_string[1:1000]
alist = []
for letter in sentence_string:
    alist.append(letter)
#print alist

#PartII:
# Print every item of the list using a for loop
for letter in alist:
    print letter



#PartIII:
# write a for loop to find the index of 'b' in the list "vowels"
c = -1
vowels = ['a', 'b', 'i', 'o', 'u', 'y', 'A','E','I','O','U','Y']
for letter in vowels:
    c=c+1
    if vowels[c]=="b":
        #print "The index of b is",c
        break




#PartIV:
# use the index found above to change 'b' to 'e'
vowels[c]="e"
#print vowels


#PartV:
# Using a for statement and an if statement, print all the vowels from the sentence
blist=[]
for letters in vowels:
    if letters in alist:
        blist.append(letters)
#print blist


#PartVI:
#Make a new function called "vowelFinder" that will return a list that holds all the vowels found in a list (no duplicates).
#The function's parameters should be "list" and "vowels."
"""
Example:

vowelList = vowelFinder(sentence_string, vowels)
print vowelList

would print:
['a', 'e', 'i', 'o', 'y']
"""

def VowelFinder(string, vowels):
    vowelList=[]
    for letters in string:
        if letters in vowels and letters not in vowelList:
            vowelList.append(letters)

    return vowelList

a=sentence_string

VowelFinder(a,vowels)

vowelList = vowelFinder(sentence_string, vowels)
print vowelList