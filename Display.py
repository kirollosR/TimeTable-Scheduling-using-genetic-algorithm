import prettytable as prettytable

from Class import Class
from Course import Course
from Data import Data
from Day import Day
from Department import Department
from Hall import Hall
from Lecturer import Lecturer
from Time import Time
from TimeAvailable import TimeAvailable


class Display:
    def print_available_data(self):
        print("> ALL Available Data")
        self.print_dept()
        self.print_course()
        self.print_halls()
        self.print_instructor()
        self.print_Time_Avilable()

    def print_dept(self):
        depts = Data.getDepts()
        print(len(depts))
        availableDeptsTable = prettytable.PrettyTable(['dept', 'course'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_Courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])

        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(['id', 'course #', 'max # of students', 'instructors'])
        courses = Data.getCourses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ","
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr])
        print(availableCoursesTable)

    def print_instructor(self):
        data = Data()
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructors'])
        instructors = data.getLecturers()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])

        print(availableInstructorsTable)

    def print_halls(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = Data.getHalls()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)

    def print_Time_Avilable(self):
        availableTimeAvilableTable = prettytable.PrettyTable(['id', 'Time Avilable'])
        timeAvilable = Data.getTimeAvailable()
        for i in range(0, len(timeAvilable)):
            availableTimeAvilableTable.add_row([timeAvilable[i].get_id(), timeAvilable[i].get_time()])
        print(availableTimeAvilableTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            ['schedule #', 'fitness', '# of conflicts', 'classes[dept,class,room,instructor]'])
        schedules = population.getSchedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [str(i), round(schedules[i].getFitness(), 3), schedules[i].getNumberOfConflicts(), schedules[i]])
        print(table1)

    # TODO : change the display of time available
    def get_sort_key_time(list):
        return list.getTimeAvilable().getId()

    def print_schedule_as_table(self, schedule):
        classes = schedule.getClasses()
        table = prettytable.PrettyTable(
            ['Class #', 'Dept', 'Course(number , max # of students)', 'Room (Capacity)', 'Instructor', 'TimeAvilable'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].getDept().getName(), classes[i].getCourse().getName() + " (" +
                           classes[i].getCourse().getId() + ", " + str(
                classes[i].getCourse().getMaxNumberOfStudents()) + ")",
                           classes[i].getHall().getId() + " (" + str(classes[i].getHall().getCapacity()) + ")",
                           classes[i].getLecturer().getName() + " (" + str(classes[i].getLecturer().getId()) + ")",
                           classes[i].getTimeAvilable().getTimeAvailable() + " (" + str(
                               classes[i].getTimeAvilable().getId()) + ")"])
        print(table)

    def printOurUsualSchedule(self, schedule, dept):
        allClasses = schedule.getClasses()
        deptClasses = []
        for i in range(0, len(allClasses)):
            if allClasses[i].getDept().getName() == dept:
                deptClasses.append(allClasses[i])
        deptClasses.sort(key=Display.get_sort_key_time, reverse=False)

        # Default class
        defaultClass1 = Class(" ",Department(" ", [Course(" ", " ", [Lecturer(" ", " ")], 0)]), Course(" ", " ", [Lecturer(" ", " ")], 0))
        defaultClass1.setHall(Hall(" ", 0))
        defaultTime = TimeAvailable(" ", Day(0, " "), Time(0, " "))
        defaultClass1.setTimeAvilable(defaultTime)
        defaultClass1.setLecturer(Lecturer(" ", " "))

        dictClasses = {"11": defaultClass1, "12": defaultClass1, "13": defaultClass1, "14": defaultClass1, "15": defaultClass1,
                       "21": defaultClass1, "22": defaultClass1, "23": defaultClass1, "24": defaultClass1, "25": defaultClass1,
                       "31": defaultClass1, "32": defaultClass1, "33": defaultClass1, "34": defaultClass1, "35": defaultClass1,
                       "41": defaultClass1, "42": defaultClass1, "43": defaultClass1, "44": defaultClass1, "45": defaultClass1,
                       "51": defaultClass1, "52": defaultClass1, "53": defaultClass1, "54": defaultClass1, "55": defaultClass1}
        for i in range(0, len(deptClasses)):
            deptClasses[i].getTimeAvilable().getId()
            if deptClasses[i].getTimeAvilable().getId() in dictClasses:
                # dictClasses[str(deptClasses[i].getTimeAvilable().getId())] = deptClasses[i]
                dictClasses.update({str(deptClasses[i].getTimeAvilable().getId()): deptClasses[i]})
        #     for key, value in dictClasses.items():
        table = prettytable.PrettyTable(
            ['', '8:00-10:00', '10:00-12:00', '12:00-2:00', '2:00-4:00', '4:00-6:00'])
        table.add_row(
            ['Sunday', dictClasses.get("11").getCourse().getName(), dictClasses.get("12").getCourse().getName(),
            dictClasses.get("13").getCourse().getName(), dictClasses.get("14").getCourse().getName(),
            dictClasses.get("15").getCourse().getName()])
        table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        table.add_row(
            ['Monday', dictClasses.get("21").getCourse().getName(), dictClasses.get("22").getCourse().getName(),
            dictClasses.get("23").getCourse().getName(), dictClasses.get("24").getCourse().getName(),
            dictClasses.get("25").getCourse().getName()])
        table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        table.add_row(
            ['Tuesday', dictClasses.get("31").getCourse().getName(), dictClasses.get("32").getCourse().getName(),
             dictClasses.get("33").getCourse().getName(), dictClasses.get("34").getCourse().getName(),
             dictClasses.get("35").getCourse().getName()])
        table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        table.add_row(
            ['Wednesday', dictClasses.get("41").getCourse().getName(), dictClasses.get("42").getCourse().getName(),
             dictClasses.get("43").getCourse().getName(), dictClasses.get("44").getCourse().getName(),
             dictClasses.get("45").getCourse().getName()])
        table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        table.add_row(
            ['Thursday', dictClasses.get("51").getCourse().getName(), dictClasses.get("52").getCourse().getName(),
             dictClasses.get("53").getCourse().getName(), dictClasses.get("54").getCourse().getName(),
             dictClasses.get("55").getCourse().getName()])
        # for i in range(0, len(dictClasses)):
        #
        #     table.add_row(
        #         ['Sunday', dictClasses.get("11").getCourse().getName(), dictClasses.get("12").getCourse().getName(),
        #          dictClasses.get("13").getCourse().getName(), dictClasses.get("14").getCourse().getName(),
        #          dictClasses.get("15").getCourse().getName()])

        # table = prettytable.PrettyTable(
        #     ['Class #', 'Dept', 'Course(number , max # of students)', 'Room (Capacity)', 'Instructor', 'TimeAvilable'])
        # for i in range(0, len(deptClasses)):
        #     table.add_row([str(i), deptClasses[i].getDept().getName(), deptClasses[i].getCourse().getName() + " (" +
        #                    deptClasses[i].getCourse().getId() + ", " + str(
        #         deptClasses[i].getCourse().getMaxNumberOfStudents()) + ")",
        #                    deptClasses[i].getHall().getId() + " (" + str(deptClasses[i].getHall().getCapacity()) + ")",
        #                    deptClasses[i].getLecturer().getName() + " (" + str(deptClasses[i].getLecturer().getId()) + ")",
        #                    deptClasses[i].getTimeAvilable().getTimeAvailable() + " (" + str(
        #                        deptClasses[i].getTimeAvilable().getId()) + ")"])
        print(table)
