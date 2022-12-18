from Class import Class
from random import randint



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
            courses = depts[i].getCourses()


            for j in range(0, len(courses)):
                newClass = Class(self.classNumb, depts[i], courses[j])
                self.classNumb += 1
                newClass.setTimeAvilable(
                    self.data.getTimeAvailable()[randint(0, len(self.data.getTimeAvailable()) - 1)])
                newClass.setHall(self.data.getHalls()[randint(0, len(self.data.getHalls()) - 1)])
                newClass.setLecturer(
                    courses[j].getLecturer()[randint(0, len(courses[j].getLecturer()) - 1)])
                self.classes.append(newClass)
        return self

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
        self.numberOfConflicts = 0
        timeIds = {}
        departments = self.data.getDepts()
        days = []
        courseIds = {}
        # Create dictionary of departments without times
        for i in range(0, len(departments)):
            timeIds[departments[i].getName()] = []

        classes = self.getClasses()
        for i in range(0, len(classes)):
            # add timeID to dictionary in the list of the course department to calculate the number of gaps of department
            timeIds[classes[i].getDept().getName()] += [int(classes[i].getTimeAvilable().getId())]
            timeIds.setdefault(classes[i].getDept().getName(), []).append(int(classes[i].getTimeAvilable().getId()))
            courseIds.setdefault(classes[i].getCourse().getName(), []).append(classes[i].getCourse().getName())

            if classes[i].getTimeAvilable().getDay() not in days:
                days.append(classes[i].getTimeAvilable().getDay())

            # capacity of hall < number of students
            if classes[i].getHall().getCapacity() < classes[i].getCourse().getMaxNumberOfStudents():
                self.numberOfConflicts += 15  # 5 points for the students over the capacity of the hall

            # TODO: number of days the dr will teach per week

            for j in range(i, len(classes)):
                # 2 classes in the same department
                if classes[i].getDept().getName() == classes[j].getDept().getName():
                    # 2 classes at the same time of same department
                    if classes[i].getTimeAvilable().getId() == classes[j].getTimeAvilable().getId() and i != j:
                        self.numberOfConflicts += 5
                        # 2 classes at the same time in the same hall
                        if classes[i].getHall().getId() == classes[j].getHall().getId():
                            self.numberOfConflicts += 5
                        # 2 classes at the same time have the same lecturer
                        if classes[i].getLecturer() == classes[j].getLecturer():
                            self.numberOfConflicts += 5
                # 2 classes in different departments
                else:
                    if classes[i].getTimeAvilable().getId() == classes[j].getTimeAvilable().getId() and i != j:
                        # 2 classes at the same time in the same hall
                        if classes[i].getHall().getId() == classes[j].getHall().getId() and i != j:
                            self.numberOfConflicts += 5
                        # 2 classes at the same time have the same lecturer
                        if classes[i].getLecturer() == classes[j].getLecturer() and i != j:
                            self.numberOfConflicts += 5

        # number of gaps of the day
        for i in timeIds.keys():
            sortedTimeIds = sorted(timeIds[i])
            for j in range(0, len(sortedTimeIds)):
                for k in range(j, len(sortedTimeIds)):
                    gaps = int(sortedTimeIds[k]) - int(sortedTimeIds[j])
                    if 2 <= gaps <= 4:
                        self.numberOfConflicts += (gaps - 1)
                        break

        # for i in courseIds.keys():
        #     if len(courseIds[i]) <= 15:
        #         if len(days) == 5:
        #             self.numberOfConflicts += 2
        #         elif len(days) == 4:
        #             self.numberOfConflicts += 1
        #     elif 15 < len(courseIds[i]) <= 20:
        #         if len(days) == 5:
        #             self.numberOfConflicts += 1
        #     elif len(courseIds[i]) > 20:
        #         pass

        return (1 / ((1.0 * self.numberOfConflicts) + 1))

    def getFitness(self):
        if self.isFitnesschanged:
            self.fitness = self.calculateFitness()
            self.isFitnesschanged = False
        return self.fitness

    def __str__(self):
        phrase = ""
        for i in range(0, len(self.classes)):
            phrase += str(self.classes[i]) + ","

        return phrase
