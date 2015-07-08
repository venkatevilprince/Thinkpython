class time(object):
    """represents time

    attributes hour,miinute,second"""


    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def __str__(self):

        # Use join to quickly print out string colon separated
        return "{0:02d}:{1:02d}:{2:02d}".format(int(self.hour), int(self.minute), int(self.second))


    def time_to_int(self):
        """convers the time into seconds and returns integer"""
        sec = self.second + (self.minute*60) + (self.hour*3600)
        return sec


    @staticmethod
    def int_to_time(sec):
        """convers seconds(integer) to class type time and returns time variable""" 
        t = time()
        t.minute,t.second = divmod(sec, 60)
        t.hour,t.minute = divmod(t.minute, 60)
        return t

    
    def increment(self, other):
        """Returns the time variable with sum of the two times"""
        sec1 = self.time_to_int()
        sec2 = other.time_to_int()
        new_sec = sec1 + sec2
        return self.int_to_time(new_sec)
        

t1 = time(1,25,30)
t2 = time(0,120,30)
print t1.__str__()
sec = t1.time_to_int()
test = time.int_to_time(sec)
print test
print t1.increment(t2)








    
