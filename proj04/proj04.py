0# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
lollipop_list = []
lollipop= raw_input("Type anything....just make sure it's a string:")
for letter in lollipop:
    lollipop_list.append(letter)
print lollipop_list
length=len(lollipop_list)
print length


while lollipop_list:
    if lollipop_list[0]==lollipop_list[-1]:
        lollipop_list=lollipop_list[1:-1]
    else:
        print "This word is not a palindrome."
        break
#if lollipop_list[0]==lollipop_list[int(length)] and lollipop_list[1]==lollipop_list[int(length-1)] and lollipop_list[2]==lollipop_list[int(length-2)] and lollipop_list[3]==lollipop_list[int(length-3)] and lollipop_list[4]==lollipop_list[int(length-4)] and lollipop_list[5]==lollipop_list[int(length-5)] and lollipop_list[6]==lollipop_list[int(length-6)]and lollipop_list[7]==lollipop_list[int(length-7)] and lollipop_list[8]==lollipop_list[int(length-8)] and lollipop_list[9]==lollipop_list[int(length-9)]and lollipop_list[10]==lollipop_list[int(length-10)] and lollipop_list[11]==lollipop_list[int(length-11)] and lollipop_list[12]==lollipop_list[int(length-12)]:
    print lollipop_list
if lollipop_list==[]:
    print "This word is a palindrome."


