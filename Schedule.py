from Class import Class
from  random import randint

class Schedule:
    def __init__(self, data):
        self.data = data
        self.classes = []
        self.numberOfConflicts = 0
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

    def getClasses(self):
        self.isFitnesschanged = True
        return self.classes

    def getNumberOfConflicts(self):
        return self.numberOfConflicts

    def calculateFitness(self):
        self.numOfConflicts = 0
        classes = self.getClasses()
        for i in range(0, len(classes)):
            if(classes[i].getHall().getCapacity() < classes[i].getCourse().getNumberOfStudents()):
                self.numberOfConflicts += 5 # 5 points for the students over the capacity of the hall

            for j in range(0, len(classes)):
                if(classes[i].getHall().getId() == classes[j].getHall().getId() and i != j):
                    if(classes[i].getTimeAvilable().getId() == classes[j].getTimeAvilable().getId()):
                        self.numberOfConflicts += 1

    def averageFitness(self):
        pass


