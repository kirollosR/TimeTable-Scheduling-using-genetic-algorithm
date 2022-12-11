class Department:
    def __init__(self, name, Courses):
        self._name = name
        self._Courses = Courses

    def getName(self): return self._name

    def getCourses(self): return self._Courses
