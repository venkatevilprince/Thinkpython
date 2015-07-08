import sixteen_one
class time(object):
    """represents a time variable

       attributes: hour, minute,second """
t1 = time()
t1.hour = 5
t1.minute = 25
t1.second = 29
t2 = time()
t2.hour = 0
t2.minute = 120
t2.second = 31


def add_time(t1,t2):
    """Returns the sum of the two times and handles time variable limits"""
    time_sum = time()
    time_sum.hour = t1.hour + t2.hour
    time_sum.minute = t1.minute + t2.minute
    time_sum.second = t1.second + t2.second
    time_sum.hour += time_sum.minute/60
    time_sum.minute = time_sum.minute%60
    time_sum.minute += time_sum.second/60
    time_sum.second = time_sum.second%60
    return time_sum
new = add_time(t1,t2)
sixteen_one.print_time(new)
