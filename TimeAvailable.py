class TimeAvailable:
    def __init__(self,id, day, time):
        self.id = id
        self.time = time
        self.day = day


    def getId(self):
        return self.id

    def getTime(self):
        return self.time

    def getDay(self):
        return self.day

    def getTimeAvailable(self):
        return self.day + " " + self.time
