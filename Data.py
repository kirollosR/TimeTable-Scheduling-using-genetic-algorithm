from Course import Course
from Day import Day
from Department import Department
from Hall import Hall
from Lecturer import Lecturer
from Time import Time
from TimeAvailable import TimeAvailable


class Data:
    # TODO: chanege capacity
    HALLS = [["H1", 500], ["H2", 500], ["H3", 500], ["H4", 500],
             ["R1", 100], ["R2", 100], ["R3", 100], ["R4", 100]]
    LECTURERS = [["100", "DR Amr Ghoneim"],
                 ["101", "DR Mohamed Elsaid"],
                 ["102", "DR Marwa Abd ElFattah"],
                 ["103", "DR Hossam Shamardan"],
                 ["104", "DR Helal"],
                 ["105", "DR Ahmed Hesham"],
                 ["106", "DR Wessam ELBehedy"],
                 ["107", "DR Salwa Ossama"]]

    DAYS = [Day(1, "sunday"), Day(2, "monday"), Day(3, "tuesday"), Day(4, "wednesday"), Day(5, "thursday")]
    TIMES = [Time(1, "8-10"), Time(2, "10-12"), Time(3, "12-2"), Time(4, "2-4"), Time(5, "4-6")]
    def __init__(self):
        self.halls = [] #array of class Room
        self.lecturers = [] #array of class Lecturer
        self.timeAvailable = [] #array of class TimeAvailable
        for i in range(0, len(self.HALLS)):
            self.halls.append(Hall(self.HALLS[i][0], self.HALLS[i][1]))

        for i in range(0, len(self.LECTURERS)):
            self.lecturers.append(Lecturer(self.LECTURERS[i][0],self.LECTURERS[i][1]))

        for i in range(0, len(self.DAYS)):
            for j in range(0, len(self.TIMES)):
                self.timeAvailable.append(TimeAvailable(str(self.DAYS[i].getId())+str(self.TIMES[j].getId()),self.DAYS[i].getDay(), self.TIMES[j].getTime()))
        # for i in range(0, len(self.TIME_AVAILABLE)):
        #     self.timeAvailable.append(TimeAvailable(self.TIME_AVAILABLE[i][0], self.TIME_AVAILABLE[i][1]))

        # TODO: change number of students
        course1 = Course("C1", "Image Processing", [self.lecturers[3]], 100)
        course2 = Course("C2", "Data Communication", [self.lecturers[3]], 500)
        course3 = Course("C3", "E-Commerce", [self.lecturers[4]], 100)
        course4 = Course("C4", "Project Management", [self.lecturers[4]], 100)
        course5 = Course("C5", "Human Rights", [self.lecturers[4]], 100)
        course6 = Course("C6", "Computer Organization", [self.lecturers[2]], 500)
        course7 = Course("C7", "PL2", [self.lecturers[2], self.lecturers[1]], 500)
        course8 = Course("C8", "Artificial Intelligence", [self.lecturers[0]], 500)
        course9 = Course("C9", "Intro to CS", [self.lecturers[0]], 100)
        course10 = Course("C10", "OS-2", [self.lecturers[5]], 500)
        course11 = Course("C11", "PL3", [self.lecturers[5]], 500)
        course12 = Course("C12", "Selected-1", [self.lecturers[6]], 500)
        course13 = Course("C13", "Logic Design", [self.lecturers[6], self.lecturers[7]], 500)
        course14 = Course("C14", "Concepts of Programing", [self.lecturers[7]], 100)
        self.courses = [course1, course2, course3, course4, course5, course6, course7, course8,
                        course9, course10, course11, course12, course13, course14]

        dept1 = Department("IT", [course1, course2])
        dept2 = Department("IS", [])
        dept3 = Department("CS", [course6, course8, course10, course11, course12, course14])
        dept4 = Department("General", [course3, course4, course5, course9, course13])

        self.depts = [dept1, dept2, dept3, dept4]
        self.numberOfClasses = 0
        for i in range(0, len(self.depts)):
            #condition if the course in other department and already added don't add it again
            self.numberOfClasses += len(self.depts[i].getCourses())

    def getRooms(self):
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
