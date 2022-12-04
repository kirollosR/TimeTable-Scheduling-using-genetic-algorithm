from Class import Class
from  random import randint

class Schedule:
    def __init__(self, data):
        self.data = data
        self.classes = []
        self.numOfConflicts = 0
        self.fitness = -1
        self.classNumb = 0
        self.isFitnesschanged = True  # ********

    def individual(self):
        depts = self.data.getDepts()

        for i in range(0, len(depts)):
            courses = depts[i].get_courses()

            for j in range(0, len(courses)):
                newClass = Class(self.classNumb, depts[i], courses[j])
                self.classNumb += 1
                newClass.setTimeAvilable(self.data.getTimeAvailable()[randint(0, len(self.data.getTimeAvailable()) - 1)])
                newClass.setHall(self.data.getHall()[randint(0, len(self.data.getHall()) - 1)])
                newClass.setLecturer(
                    courses[j].getLecturer()[randint(0, len(courses[j].getLecturer()) - 1)])
                self.classes.append(newClass)

    def encoding(self):
        pass

    def decoding(self):
        pass

    def calculateFitness(self):
        self.numOfConflicts = 0

    def averageFitness(self):
        pass


