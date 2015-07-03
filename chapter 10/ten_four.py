def middle(item):
    a = []
    for i in range(1, len(item) - 1):
        a.append(item[i])
    return a    
test=[1, 2, 3, 4, 5, 6]
print middle(test)
