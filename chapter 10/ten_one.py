def nested_sum(list1):
    """Returns the sum of nested lists"""
    nsum = 0
    for i in range(len(list1)):        
        if isinstance(list1[i], list):
            nsum = nsum+nested_sum(list1[i])
        else:
            nsum = nsum + list1[i]
    return nsum
test_list=[1, 1, [1, [1, 1, 1], 1], 1, 1]
#print nested_sum(test_list);
print nested_sum(test_list)
