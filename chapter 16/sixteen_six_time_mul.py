from sixteen_five import *
t1 = time()
t1.hour = 5
t1.minute = 25
t1.second = 29
t2 = time()
t2.hour = 0
t2.minute = 120
t2.second = 31


def mul_time(time,n):
    sec1 = time_to_int(time)
    new_sec = sec1 * n
    return int_to_time(new_sec)

#print_time(mul_time(t1,2))


def average_pace(f_time, dist):
    f_sec = time_to_int(f_time)
    dist = float(dist)
    new_sec = f_sec / dist
    return int_to_time(new_sec)

print_time(t1)
print_time(average_pace(t1, 100))
print_time(mul_time(average_pace(t1, 100),100))
