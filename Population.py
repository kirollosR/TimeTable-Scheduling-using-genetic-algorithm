from Schedule import Schedule


class Population:
    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.schedules = []
        for i in range(0, size):
            self.schedules.append(Schedule(self.data).individual())

    def getSchedules(self):
        return self.schedules