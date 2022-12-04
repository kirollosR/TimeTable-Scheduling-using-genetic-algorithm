from Lecturer import Lecturer

class Time:
    def __init__(self,id, day, time):
        self.id = id
        self.time = time #array of times at that day
        self.day = day

    def getId(self):
        return self.id

    def getTime(self):
        return self.time

    def getDay(self):
        return self.day

t = [["t1","monday",["10-12","12-2"]],
     ["t2","tuesday",["10-12","12-2"]]]
# time = Time("t1","monday",["10-12","12-2"])
time = []
for i in range(0, len(t)):
    time.append(Time(t[0][0], t[0][1], t[0][2]))
print(time[0].getTime())