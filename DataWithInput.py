from Course import Course
from Day import Day
from Department import Department
from Hall import Hall
from Lecturer import Lecturer
from Time import Time
from TimeAvailable import TimeAvailable


class DataWithInput:
    # TODO: chanege capacity

    DAYS = [Day(1, "sunday"), Day(2, "monday"), Day(3, "tuesday"), Day(4, "wednesday"), Day(5, "thursday")]
    TIMES = [Time(1, "8-10"), Time(2, "10-12"), Time(3, "12-2"), Time(4, "2-4"), Time(5, "4-6")]
    def __init__(self):
        self.halls = [] #array of class Room
        self.lecturers = [] #array of class Lecturer
        self.timeAvailable = [] #array of class TimeAvailable
        self.courses = [] #array of class Course
        self.depts = [] #array of class Department

        for i in range(0, len(self.DAYS)):
            for j in range(0, len(self.TIMES)):
                self.timeAvailable.append(TimeAvailable(str(self.DAYS[i].getId())+str(self.TIMES[j].getId()),self.DAYS[i].getDay(), self.TIMES[j].getTime()))
        # for i in range(0, len(self.TIME_AVAILABLE)):
        #     self.timeAvailable.append(TimeAvailable(self.TIME_AVAILABLE[i][0], self.TIME_AVAILABLE[i][1]))

        # TODO: change number of students

        self.numberOfClasses = 0
        for i in range(0, len(self.depts)):
            #condition if the course in other department and already added don't add it again
            self.numberOfClasses += len(self.depts[i].getCourses())

    def addHall(self, hall):
        self.halls.append(hall)

    def addLecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def addCourse(self, course):
        self.courses.append(course)

    def addDepartment(self, dept):
        self.depts.append(dept)
    def getHalls(self):
        return self.halls

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
