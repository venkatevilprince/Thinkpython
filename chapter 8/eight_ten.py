def is_palindrome_modified(word):
    
    """Returns true if the string is palindrome in a sinle check statement
       without involving loop"""
    
    if(word==word[::-1]):
        return True
    else :
        return False


print is_palindrome_modified("madam")
    
