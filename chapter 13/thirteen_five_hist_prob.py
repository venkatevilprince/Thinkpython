import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 11'))
sys.path.append(path)
from eleven_two import *
hist = histogram("appple")


def probablities(box):
    prob = {}
    total = 0.0
    for x in box:
        total = total + box[x]
    for x in box:
        prob[x]=box[x]/total
    return prob      
print probablities(hist)    



