# Name:
# Date:

# proj05: functions and lists

# Part I

def divisors(num):
    """
    Takes a number and returns all divisors of the number, ordered least to greatest
    :param num: int
    :return: list (int)
    """
    return 0

def prime(num):
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """
    return False

# Part III

def find_ab(side1, side2, side3):
    """
    Takes three side lengths an returns two smallest in a list
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: list of 2 ints or floats
    """
    if side1 > side2 and side1 > side3:
        return [side2, side3]
    elif side2 > side1 and side2 > side3:
        return [side1, side3]
    elif side3 > side2 and side3 > side1:
        return [side1, side2]
def find_c(side1, side2, side3):
    """
    Takes three side lengths an returns the largest
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: int or float
    """

    if side1 > side2 and side1 > side3:
        return side1
    elif side2 > side1 and side2 > side3:
        return side2
    elif side3 > side2 and side3 > side1:
        return side3

def square(side):
    return side*side



 # """
 #    Takes a side length and returns the side length squared
 #    :param side: int or float
 #    :return: int or float
 #    """


def pythagorean(a,b,c):
    """
    Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: bool
    """
    if square(a)+square(b)==square(c):
        return True
    else:
        return False




def is_right(side1, side2, side3):
    """
    Takes three side lengths and returns true if triangle is right
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: bool
    """
    Small= find_ab(side1, side2, side3)
    a=Small[0]
    b=Small[1]
    c= find_c(side1, side2, side3)
    p=pythagorean(a,b,c)
    return p



def divisors(num):
    myList = []
    b=int(num)
    for b in range(1, num+1):
        a=int(num)%b
        if a==0:
             myList.append(b)
    return myList
print divisors(8)

def prime(num):
    length = len(divisors(num))
    if length==2:
        return True
    else:
        return False
print prime(8)




# def divisors(num):
#     myList = []
#     b=int(num)
#     while b>0:
#        a=int(num)%b
#        if a==0:
#             myList.append(b)
#        b=b-1
#     return myList
# print divisors(8)


import random
lst1= [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]
lst2= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list =[1, 2, 1, 1, 1, 3, 2, 1, 2, 1, 2, 1]
list2=[1, 2, 1, 1, 1, 3, 2, 1, 2, 1, 2, 1]


a=0
for number in list:
    list[a]=random.randint(1,99)
    a= a+1
print list



b=0
for number in list2:
    list2[b]=random.randint(1,99)
    b=b+1
print list2



def intersection(list, list2):
    myList=[]
    for numbers in list:
        if numbers in list2:
            myList.append(numbers)
    return myList
print intersection(list, list2)




























































# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
