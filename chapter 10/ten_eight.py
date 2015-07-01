from random import *

""" Prints the success percentage of 500 samples of 23 random students
    with birthday paradox """

def has_duplicates(item):

    """ Returns true if the list has duplicate values """

    for i in range(len(item)):
        
        for j in range(len(item)):
            if item[i]==item[j] and i!=j:
                #print j
                return True
    return False               

def gen_rand_23():

    """ Returns a list with 23 random numbers between 1 and 365 indicating
        uniquue birthdays """
    
    a=[]
    for i in range(23):
        a.append(randint(1,365))

    return a

def prob_estimation(n):

    """ Returns the number of time paradox occurs out of n samples"""
    truecount=0
    for i in range(n):
        test=gen_rand_23()
        if has_duplicates(test):
            truecount+=1
    return truecount        

test=[1,2,3,4,5,6]

#print has_duplicates(test)
    
#test2=gen_rand_23()
#print test2                 
#print has_duplicates(test2)

yes=prob_estimation(500)
yes=float(yes)
print "Succes percentage = {0:.4f}".format(yes/500)                 
