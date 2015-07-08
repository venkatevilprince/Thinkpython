from sixteen_one import *
t1 = time()
t1.hour = 5
t1.minute = 25
t1.second = 29
t2 = time()
t2.hour = 0
t2.minute = 120
t2.second = 31


def time_to_int(t):
    """convers the time into seconds and returns integer"""
    sec = t.second + (t.minute*60) + (t.hour*3600)
    return sec


def int_to_time(sec):
    """convers seconds(integer) to class type time and returns time variable""" 
    t = time()
    t.minute,t.second = divmod(sec, 60)
    t.hour,t.minute = divmod(t.minute, 60)
    return t


def increment(t1, t2):
    """Returns the time variable with sum of the two times"""
    sec1 = time_to_int(t1)
    sec2 = time_to_int(t2)
    new_sec = sec1 + sec2
    return int_to_time(new_sec)
if __name__ == "__main__":
    sec = time_to_int(t1)
    print sec
    test_t = int_to_time(sec)
    print_time(test_t)
    print_time(increment(t1,t2))


