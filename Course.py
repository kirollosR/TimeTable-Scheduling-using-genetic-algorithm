class Course:
    def __init__(self, id, name, lecturer, maxNumberOfStudents ):
        self.id = id
        self.name = name
        self.lecturer = lecturer #variable of class Lecturer
        self.maxNumberOfStudents = maxNumberOfStudents
        #know the meaning ofCourse Requirements matrix with integer elements
        #representing the number of hours a lecturer teaches a course during each week

    def getId(self):
        return self.id

    def GetCourseName(self):
        return self.name

    def getLecturer(self):
        return self.lecturer

    def getMaxNumberOfStudents(self):
        return self.maxNumberOfStudents

    def __str__(self): return self.name