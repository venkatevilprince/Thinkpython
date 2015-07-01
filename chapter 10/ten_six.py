def is_sorted(item):

    for i in range(len(item)-1):
        if not item[i]<item[i+1]:
            return False

    return True



test=[1,2,3,4,5,6,11]
test2=['b','a']
print is_sorted(test)
print is_sorted(test2)
