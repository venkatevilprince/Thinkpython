import math
import random


def is_prime(n):
    """Returns True id the arguemen is a prime number"""
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def rand_prime(i, func):
    """Returns a random prime number in the range [i,func]"""
    a = random.randint(i, func)
    while(not is_prime(a)):
        #print" aahan"
        a = random.randint(i, func)
        if is_prime(a):
            return a
    return a
message = 100
""" creates a cipher and keys and then decodes the message back"""
print "message: ", message
p = rand_prime(50, 60)
q = rand_prime(60, 70)
n = p * q
#print p,q
func = (p - 1) * (q - 1)
#print func
e = rand_prime(1, func)

cipher = (message ** e) % n
print "cipher: ", cipher
for d in range(func):
    if e * d % func == 1:
        #print " d=",d
        break
#print d
decoded = (cipher ** d) % n
print "decodec message: ", decoded
