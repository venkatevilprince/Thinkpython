def is_palindrome(value,start_index,end_index):

    """ Returns True if the entered value is a palindrome
        from start index to the end index"""
    
    value=str(value)
    s = value[start_index:end_index+1]
    return s==s[::-1]

def is_car_puzzle(i):

    """ Returns true if the number satisfies the puzzle in exercise 9.9"""
    
    decision = (is_palindrome(i,2,5) and is_palindrome(i+1,1,5)
                and is_palindrome(i+2,1,4) and is_palindrome(i+3,0,5))
    return decision 

#print is_palindrome(121221,2,5)    

for i in range(100000,999999):
    if(is_car_puzzle(i)):
        print i
    

