class time(object):
    """represents a time variable

       attributes: hour, minute,second """
t = time()
t.hour = 5
t.minute = 25
t.second = 30


def print_time(time):
    time.hour = int(time.hour)
    time.minute = int(time.minute)
    time.second = int(time.second)
    """prints the time variables in a formatted manner"""
    print "{0:02d}:{1:02d}:{2:02d}".format(time.hour, time.minute, time.second)
if __name__ == "__main__":
    print_time(t)
