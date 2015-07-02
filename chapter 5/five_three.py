import sys
import time


def check_fermet(num):
    """ This could have been done easier with 4 parameters
        but i wanted to do it with lists"""
    a_n = num[0] ** num[3]
    b_n = num[1] ** num[3]
    c_n = num[2] ** num[3]
    if(c_n == (a_n + b_n)):
        print "Holy Smokes, Fermet was wrong!"
    else:
        print "No, that doesn't work"
letters = ['a', 'b', 'c', 'd']   # this is for displaying for user
numbers = []
#statement below get values of a,b,c,d from user
#And i have checked whether the user enters only numbers
#try typing a character and it will exit
for i in range(4):
    temp = raw_input("enter value for {}" .format(letters[i]))
    numbers.append(temp)
    numbers[i] = unicode(numbers[i], 'utf-8')
    if(not numbers[i].isnumeric()):
        print "Enter only numbers"
        time.sleep(3)
        sys.exit()
    numbers[i] = int(numbers[i])
check_fermet(numbers)
