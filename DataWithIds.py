import random

from Course import Course
from Day import Day
from Department import Department
from Hall import Hall
from Lecturer import Lecturer
from Time import Time
from TimeAvailable import TimeAvailable


class DataWithIds:

    DAYS = [Day(1, "sunday"), Day(2, "monday"), Day(3, "tuesday"), Day(4, "wednesday"), Day(5, "thursday")]
    TIMES = [Time(1, "8-10"), Time(2, "10-12"), Time(3, "12-2"), Time(4, "2-4"), Time(5, "4-6")]

    DEPARTMENTS = ["IT", "IS", "CS", "General", "AI"]
    def __init__(self, numberOfCourses=0, numberOfLecturers=0, numberOfHalls=0, numberOfCoursesList=[]):
        self.halls = [] #array of class Room
        self.lecturers = [] #array of class Lecturer
        self.timeAvailable = [] #array of class TimeAvailable
        self.courses = [] #array of class Course
        self.depts = [] #array of class Department

        hallsIds = "HR"
        for i in range(0, numberOfHalls):
            self.halls.append(Hall(random.choice(hallsIds) + str(i + 1), random.randint(1000, 2500)))

        for i in range(0, numberOfLecturers):
            self.lecturers.append(Lecturer(str(100 + i),"DR " + chr(65 + i)))

        for i in range(0, len(self.DAYS)):
            for j in range(0, len(self.TIMES)):
                self.timeAvailable.append(TimeAvailable(str(self.DAYS[i].getId())+str(self.TIMES[j].getId()),self.DAYS[i].getDay(), self.TIMES[j].getTime()))
        # for i in range(0, len(self.TIME_AVAILABLE)):
        #     self.timeAvailable.append(TimeAvailable(self.TIME_AVAILABLE[i][0], self.TIME_AVAILABLE[i][1]))

        # TODO: change number of students
        # course1 = Course("C1", "Image Processing", [self.lecturers[3]], 100)
        for i in range(0, numberOfCourses):
            randomLecturer = random.choice(self.lecturers)
            self.courses.append(Course("C" + str(i + 1), "Course " + str(i + 1), [randomLecturer], random.randint(1000, 2500)))

        # COURSES = self.courses.copy()
        # for i in range(0, len(self.DEPARTMENTS)):
        #     if len(COURSES) > 0:
        #         randomNumberOfCourses = random.randint(1, int(len(COURSES)))
        #     else:
        #         randomNumberOfCourses = 0
        #     deptsCourses = []
        #     for j in range(0, randomNumberOfCourses):
        #         deptsCourses.append(COURSES[0])
        #         COURSES.pop(0)
        #
        #     self.depts.append(Department(self.DEPARTMENTS[i], deptsCourses))

        k = 0
        for i in range(0, len(self.DEPARTMENTS)):
            deptsCourses = []
            for j in range(0, numberOfCoursesList[i]):
                deptsCourses.append(self.courses[k])
                k += 1
            self.depts.append(Department(self.DEPARTMENTS[i], deptsCourses))

        self.numberOfClasses = 0
        for i in range(0, len(self.depts)):
            #condition if the course in other department and already added don't add it again
            self.numberOfClasses += len(self.depts[i].getCourses())

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
