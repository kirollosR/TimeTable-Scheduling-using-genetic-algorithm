from Course import Course
from Department import Department
from Hall import Hall
from Lecturer import Lecturer
from TimeAvailable import TimeAvailable


class Data:
    HALLS = []
    LECTURERS = []
    TIME_AVAILABLE = []
    def __init__(self):
        self.rooms = [] #array of class Room
        self.lecturers = [] #array of class Lecturer
        self.timeAvailable = [] #array of class TimeAvailable
        for i in range(0, len(self.HALLS)):
            self.rooms.append(Hall(self.HALLS[i][0],self.HALLS[i][1]))

        for i in range(0, len(self.LECTURERS)):
            self.lecturers.append(Lecturer(self.LECTURERS[i][0],self.LECTURERS[i][1]))

        for i in range(0, len(self.TIME_AVAILABLE)):
            self.timeAvailable.append(TimeAvailable(self.TIME_AVAILABLE[i][0], self.TIME_AVAILABLE[i][1]))

        course1 = Course("C1", "Intro to CS", [self.lecturers[0]], 150)
        self.courses = [course1]
        # self.courses = [course1, course2, course3, ...]

        dept1 = Department("Information Systems", [course1])
        self.depts = [dept1]
        self.numberOfClasses = 0
        # dept1 = Department("Information Systems", [course1, course3]) #take array of courses
        # self.depts = [dept1, dept2, dept3, ...]

        for i in range(0, len(self.depts)):
            #condition if the course in other department and already added don't add it again
            self.numberOfClasses += len(self.depts[i].getCourses())

    def getRooms(self):
        return self.rooms

    def getLecturers(self):
        return self.lecturers

    def getCourses(self):
        return self.courses

    def getDepts(self):
        return self.depts

    def getTimeAvailable(self):
        return self.timeAvailable

    def getNumberOfClasses(self):
        return self.numberOfClasses
