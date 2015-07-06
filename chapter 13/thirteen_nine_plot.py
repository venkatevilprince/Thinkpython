x = [1, 2, 3]
y = [4, 5, 6]

t = zip(x,y)
print t
x, y = zip(*t)
print x, y
