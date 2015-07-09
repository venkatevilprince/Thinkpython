class Time(object):
    """Represents the time of day.
        attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        # Use join to quickly print out string colon separated
        return ':'.join([str(self.hour).zfill(2), str(self.minute).zfill(2), str(self.second).zfill(2)])

    def time_to_int(self):
        # We create fractional portions of the "hour" attribute
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        # Turn the time object into seconds
        """
        :rtype : object
        """
        self_seconds = self.time_to_int()
        ret_time_seconds = self_seconds + seconds
        return self.int_to_time(ret_time_seconds)

    def is_after(self, other):
        # Return result from comparing via compute_scalar_time
        return self.time_to_int() < other.time_to_int()

    def __add__(self, other):
        if isinstance(other, Time):
            return self.increment(other.time_to_int())
        else:
            return self.increment(other)

    def __cmp__(self, other):
        tup1 = (self.hour, self.minute, self.second)
        tup2 = (other.hour, other.minute, other.second)
        print tup1, tup2
        if tup1 > tup2:
            return 1
        if tup1 < tup2:
            return -1
        else:
            return 0       
t1 = Time(11, 59, 30)
t2 = Time(11, 59, 30)
print t1 == t2


