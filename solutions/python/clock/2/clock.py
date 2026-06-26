"""
implements a clock
"""
class Clock:
    """
    implements a clock
    """
    def __init__(self, hour, minute):
        adj = 0
        tmp = minute
        if minute < 0:
            while tmp < 0:
                adj -= 1
                tmp += 60
        else:
            adj = int(minute / 60)
        if hour < 0:
            self.hour = (hour + adj) % 24
        else:
            self.hour = (hour + adj) % 24
        self.minute = tmp % 60

    def __repr__(self):
        return "Clock({}, {})".format(str(self.hour), str(self.minute))

    def __str__(self):
        return "{}:{}".format(str(self.hour).rjust(2, "0"), str(self.minute).rjust(2, "0"))

    def __eq__(self, other):
        if not isinstance(self, Clock) or not isinstance(other, Clock):
            return False
        return self.__str__() == other.__str__()

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
