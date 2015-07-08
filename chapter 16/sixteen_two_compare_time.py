class time(object):
    """represents a time variable

       attributes: hour, minute,second """
t1 = time()
t1.hour = 5
t1.minute = 25
t1.second = 29
t2 = time()
t2.hour = 5
t2.minute = 25
t2.second = 30
#def is_after(t1,t2):
def time_tuple(time):
    """returns a tuple of (hour,minute,second)"""
    res = (time.hour, )
    res += (time.minute, )
    res += (time.second, )
    return res


def is_after(t1, t2):
    """ returns True if t2 occurs after t1"""
    #print time_tuple(t1), time_tuple(t2)
    return time_tuple(t1) < time_tuple(t2)
print is_after(t1, t2)   
    
