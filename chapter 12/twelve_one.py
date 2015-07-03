def sumall( * a):
    """ Returns the sum of any number of arguments passed"""
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]
    return sum
print sumall(1, 1, 1, 1, 1, 1)
