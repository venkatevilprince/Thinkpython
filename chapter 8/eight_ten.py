def is_palindrome_modified(word):
    """Returns true if the string is palindrome in a sinle check statement
       without involving loop"""
        return word==word[::-1]
print is_palindrome_modified("madam")
