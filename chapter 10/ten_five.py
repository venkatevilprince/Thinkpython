def chop(item):
    """deletes the first and last element of the passed item"""
    del item[0]
    del item[len(item) - 1]
test=[1, 2, 3, 4, 5, 6]
chop(test)
print test
