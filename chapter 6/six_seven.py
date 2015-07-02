def is_power(a, b):
    """simple function for understanding recursion
       and base case"""
    if(a == b):
        return True
    elif(a % b == 0):
        return is_power(a / b, b)
    else:
        return False
print is_power(81, 9)
