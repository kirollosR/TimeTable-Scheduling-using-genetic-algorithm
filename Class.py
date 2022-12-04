class Class:
    def __init__(self, id, dept, course):
        self.id = id
        self.dept = dept
        self.course = course
        self.lecturer = None
        self.timeAvailable = None
        self.hall = None

    def getId(self): return self.id

    def getDept(self): return self.dept

    def getCourse(self): return self.course

    def getLecturer(self): return self.lecturer

    def getTimeAvilable(self): return self.timeAvailable

    def getHall(self): return self.hall

    def setLecturer(self, instructor): self.lecturer = instructor

    def setTimeAvilable(self, TimeAvilable): self.timeAvailable = TimeAvilable

    def setHall(self, hall): self.hall = hall

    def __str__(self):
        return "{" + str(self.dept.getName()) + "," + str(self.course.getId()) + "," + \
               str(self.hall.getId()) + "," + str(self.lecturer.getId()) + "," + str(
            self.timeAvailable.getId()) + "}"