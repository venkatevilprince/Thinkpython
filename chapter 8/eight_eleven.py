"""This program wants me to determine what each function does"""


def any_lowercase1(s):
    """Checks whether the first letter is lower"""
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """ This will always be true"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """ Checks whether the first letter is lower """
    for c in s:
        flag = c.islower()
        return flag


def any_lowercase4(s):
    """ Checks whether the first letter is lower """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """returns None if everything is lower
       false if even a singe character is not lower"""
    for c in s:
        if not c.islower():
            return False
