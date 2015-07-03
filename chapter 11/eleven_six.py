import time
known = {0: 0, 1: 1}


def fibonacci(n):
    """memorised version of  fibonacci"""
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res
start = time.time()
print fibonacci(10)
end = time.time()
print end - start
print known


def fibonacci_rec(n):
    """ Recursive version of fibonacci"""
    if(n == 0):
        return 0
    return n + fibonacci_rec(n - 1)
start = time.time()
print fibonacci_rec(10)
end = time.time()
print end - start
