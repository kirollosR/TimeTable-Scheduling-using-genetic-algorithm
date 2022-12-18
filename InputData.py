import prettytable as prettytable

from Course import Course
from Data import Data
from DataWithIds import DataWithIds
from DataWithInput import DataWithInput
from Department import Department
from Hall import Hall
from Lecturer import Lecturer


class InputData:
    def __init__(self):
        global data
        mainMenu = {}
        mainMenu['1'] = "Hard code data"
        mainMenu['2'] = "Enter number of data"
        mainMenu['3'] = "Enter specific data"
        mainMenu['4'] = "Exit"

        options = list(mainMenu.keys())
        options.sort()
        for entry in options:
            print(entry + ": " + mainMenu[entry])

        selectionMainMenu = input("\nPlease Select: ")
        if selectionMainMenu == '1':
            data = Data()
        elif selectionMainMenu == '2':
            # print("Enter number of data")
            # numberOfCourses = input("Enter number of courses: ")
            numberOfCoursesOfIT = input("Enter number of courses of IT MAX (25): ")
            numberOfCoursesOfIS = input("Enter number of courses of IS MAX (25): ")
            numberOfCoursesOfCS = input("Enter number of courses of CS MAX (25): ")
            numberOfCoursesOfGeneral = input("Enter number of courses of General MAX (25): ")
            numberOfCoursesOfAI = input("Enter number of courses of AI MAX (25): ")

            if int(numberOfCoursesOfIT) > 25 or int(numberOfCoursesOfIS) > 25 or int(numberOfCoursesOfCS) > 25 or int(
                    numberOfCoursesOfGeneral) > 25 or int(numberOfCoursesOfAI) > 25:
                print("Error: Number of courses of a department is more than 25")
                exit(0)

            else:
                numberOfCourses = int(numberOfCoursesOfIS) + int(numberOfCoursesOfCS) + int(numberOfCoursesOfIT) + int(numberOfCoursesOfAI) + int(numberOfCoursesOfGeneral)
                numberOfCoursesList = [int(numberOfCoursesOfIT), int(numberOfCoursesOfIS), int(numberOfCoursesOfCS), int(numberOfCoursesOfGeneral), int(numberOfCoursesOfAI)]

                numberOfLecturers = input("Enter number of lecturers: ")
                numberOfHalls = input("Enter number of halls: ")
                data = DataWithIds(int(numberOfCourses), int(numberOfLecturers), int(numberOfHalls), numberOfCoursesList)
        elif selectionMainMenu == '3':
            dataMenu = {}
            dataMenu['1'] = "Enter halls"
            dataMenu['2'] = "Enter lecturers"
            dataMenu['3'] = "Enter courses"
            dataMenu['4'] = "Enter Departments"
            dataMenu['5'] = "Exit"

            data = DataWithInput()
            while True:
                options = list(dataMenu.keys())
                options.sort()
                for entry in options:
                    print(entry + ": " + dataMenu[entry])
                selectionOfData = input("\nPlease Select: ")
                if selectionOfData == '1':
                    if len(data.getHalls()) > 0:
                        halls = data.getHalls()
                        hallIds = []
                        for i in range(0, len(halls)):
                            hallIds.append(halls[i].getId())
                        hallId = input("Enter hall id: ")
                        if hallId in hallIds:
                            print("Hall id already exists")
                        else:
                            hallCapacity = input("Enter hall capacity: ")
                            hall = Hall(hallId, int(hallCapacity))
                            data.addHall(hall)
                    else:
                        hallId = input("Enter hall id: ")
                        hallCapacity = input("Enter hall capacity: ")
                        hall = Hall(hallId, int(hallCapacity))
                        data.addHall(hall)
                elif selectionOfData == '2':
                    if len(data.getLecturers()) > 0:
                        lecturers = data.getLecturers()
                        lecturerIds = []
                        for i in range(0, len(lecturers)):
                            lecturerIds.append(lecturers[i].getId())
                        lecturerId = input("Enter lecturer id: ")
                        if lecturerId in lecturerIds:
                            print("Lecturer id already exists")
                        else:
                            lecturerName = input("Enter lecturer name: ")
                            lecturer = Lecturer(lecturerId, lecturerName)
                            data.addLecturer(lecturer)
                    else:
                        lecturerId = input("Enter lecturer id: ")
                        lecturerName = input("Enter lecturer name: ")
                        lecturer = Lecturer(lecturerId, lecturerName)
                        data.addLecturer(lecturer)
                elif selectionOfData == '3':
                    lecturers = data.getLecturers()
                    if not lecturers:
                        print("Please enter lecturers first")
                    else:
                        if len(data.getCourses()) > 0:
                            courses = data.getCourses()
                            courseIds = []
                            for i in range(0, len(courses)):
                                courseIds.append(courses[i].getId())
                            courseId = input("Enter course id: ")
                            if courseId in courseIds:
                                print("Course id already exists")
                            else:
                                courseName = input("Enter course name: ")

                                availableInstructorsTable = prettytable.PrettyTable(['number', 'Lecturer'])
                                for i in range(0, len(lecturers)):
                                    availableInstructorsTable.add_row([i, lecturers[i].getName()])
                                print(availableInstructorsTable)

                                numberOfLecturer = input("Choose number of lecturer: ")
                                lecturer = lecturers[int(numberOfLecturer)]
                                numberOfStudents = input("Enter number of students of this course: ")
                                course = Course(courseId, courseName, [lecturer], int(numberOfStudents))
                                data.addCourse(course)
                        else:
                            courseId = input("Enter course id: ")
                            courseName = input("Enter course name: ")

                            availableInstructorsTable = prettytable.PrettyTable(['number', 'Lecturer'])
                            for i in range(0, len(lecturers)):
                                availableInstructorsTable.add_row([i, lecturers[i].getName()])
                                print(availableInstructorsTable)

                            numberOfLecturer = input("Choose number of lecturer: ")
                            lecturer = lecturers[int(numberOfLecturer)]
                            numberOfStudents = input("Enter number of students of this course: ")
                            course = Course(courseId, courseName, [lecturer], int(numberOfStudents))
                            data.addCourse(course)
                elif selectionOfData == '4':
                    courses = data.getCourses()
                    if not courses:
                        print("Please enter courses first")
                    else:
                        if len(data.getDepts()) > 0:
                            depts = data.getDepts()
                            departmentNames = []
                            for i in range(0, len(depts)):
                                departmentNames.append(depts[i].getName())
                            departmentName = input("Enter department name: ")
                            if departmentName in departmentNames:
                                print("Department is already exists")
                            else:
                                departmentCoursesTable = prettytable.PrettyTable(['number', 'Course'])
                                for i in range(0, len(courses)):
                                    departmentCoursesTable.add_row([i+1, courses[i].getName()])
                                print(departmentCoursesTable)
                                departmentCourses = []
                                x = input("Choose number of course: ")
                                while x:
                                    if x != '0':
                                        departmentCourses.append(courses[int(x)])
                                        x = input("Choose number of course: ")
                                    else:
                                        break
                                department = Department(departmentName, departmentCourses)
                                data.addDepartment(department)
                        else:
                            departmentName = input("Enter department name: ")
                            departmentCoursesTable = prettytable.PrettyTable(['number', 'Course'])
                            for i in range(0, len(courses)):
                                departmentCoursesTable.add_row([i+1, courses[i].getName()])
                            print(departmentCoursesTable)
                            departmentCourses = []
                            x = input("Choose number of course: ")
                            while x:
                                if x != '0':
                                    departmentCourses.append(courses[int(x)-1])
                                    x = input("Choose number of course: ")
                                else:
                                    break
                            department = Department(departmentName, departmentCourses)
                            data.addDepartment(department)
                elif selectionOfData == '5':
                    break
                else:
                    print("Unknown Option Selected!")

        elif selectionMainMenu == '4':
            exit()
        else:
            print("Invalid selection")
            exit()

    def getData(self):
        return data