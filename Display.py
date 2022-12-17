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
    def print_available_data(self, data):
        print("> ALL Available Data")
        self.print_dept(data)
        self.print_course(data)
        self.print_halls(data)
        self.print_instructor(data)
        self.print_Time_Avilable(data)

    def print_dept(self, data):
        depts = data.getDepts()
        print(len(depts))
        availableDeptsTable = prettytable.PrettyTable(['dept', 'course'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).getCourses()
            if len(courses) == 0:
                tempStr = "[ ]"
            else:
                tempStr = "["
                for j in range(0, len(courses) - 1):
                    tempStr += courses[j].__str__() + ", "
                tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).getName(), tempStr])

        print(availableDeptsTable)

    def print_course(self, data):
        availableCoursesTable = prettytable.PrettyTable(['id', 'course #', 'max # of students', 'instructors'])
        courses = data.getCourses()
        for i in range(0, len(courses)):
            instructors = courses[i].getLecturer()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ","
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [courses[i].getId(), courses[i].getName(), str(courses[i].getMaxNumberOfStudents()), tempStr])
        print(availableCoursesTable)

    def print_instructor(self, data):
        # data = Data()
        availableInstructorsTable = prettytable.PrettyTable(['id', 'Lecturer'])
        instructors = data.getLecturers()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].getId(), instructors[i].getName()])

        print(availableInstructorsTable)

    def print_halls(self, data):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.getHalls()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].getId()), str(rooms[i].getCapacity())])
        print(availableRoomsTable)

    def print_Time_Avilable(self, data):
        availableTimeAvilableTable = prettytable.PrettyTable(['id', 'Time Avilable'])
        timeAvilable = data.getTimeAvailable()
        for i in range(0, len(timeAvilable)):
            availableTimeAvilableTable.add_row([timeAvilable[i].getId(), timeAvilable[i].getTimeAvailable()])
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
            ['\nSunday', dictClasses.get("11").getCourse().getName() + "\n" + dictClasses.get("11").getLecturer().getName() + "\n" + dictClasses.get("11").getHall().getId(),
                        dictClasses.get("12").getCourse().getName() + "\n" + dictClasses.get("12").getLecturer().getName() + "\n" + dictClasses.get("12").getHall().getId(),
                        dictClasses.get("13").getCourse().getName() + "\n" + dictClasses.get("13").getLecturer().getName() + "\n" + dictClasses.get("13").getHall().getId(),
                        dictClasses.get("14").getCourse().getName() + "\n" + dictClasses.get("14").getLecturer().getName() + "\n" + dictClasses.get("14").getHall().getId(),
                        dictClasses.get("15").getCourse().getName() + "\n" + dictClasses.get("15").getLecturer().getName() + "\n" + dictClasses.get("15").getHall().getId()])
        table.add_row([9 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-'])

        table.add_row(
            ['\nMonday', dictClasses.get("21").getCourse().getName() + "\n" + dictClasses.get("21").getLecturer().getName() + "\n" + dictClasses.get("21").getHall().getId(),
             dictClasses.get("22").getCourse().getName() + "\n" + dictClasses.get("22").getLecturer().getName() + "\n" + dictClasses.get("22").getHall().getId(),
             dictClasses.get("23").getCourse().getName() + "\n" + dictClasses.get("23").getLecturer().getName() + "\n" + dictClasses.get("23").getHall().getId(),
             dictClasses.get("24").getCourse().getName() + "\n" + dictClasses.get("24").getLecturer().getName() + "\n" + dictClasses.get("24").getHall().getId(),
             dictClasses.get("25").getCourse().getName() + "\n" + dictClasses.get("25").getLecturer().getName() + "\n" + dictClasses.get("25").getHall().getId()])
        table.add_row([9 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-'])

        table.add_row(
            ['\nTuesday', dictClasses.get("31").getCourse().getName() + "\n" + dictClasses.get("31").getLecturer().getName() + "\n" + dictClasses.get("31").getHall().getId(),
             dictClasses.get("32").getCourse().getName() + "\n" + dictClasses.get("32").getLecturer().getName() + "\n" + dictClasses.get("32").getHall().getId(),
             dictClasses.get("33").getCourse().getName() + "\n" + dictClasses.get("33").getLecturer().getName() + "\n" + dictClasses.get("33").getHall().getId(),
             dictClasses.get("34").getCourse().getName() + "\n" + dictClasses.get("34").getLecturer().getName() + "\n" + dictClasses.get("34").getHall().getId(),
             dictClasses.get("35").getCourse().getName() + "\n" + dictClasses.get("35").getLecturer().getName() + "\n" + dictClasses.get("35").getHall().getId()])
        table.add_row([9 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-'])

        table.add_row(
            ['\nWednesday', dictClasses.get("41").getCourse().getName() + "\n" + dictClasses.get("41").getLecturer().getName() + "\n" + dictClasses.get("41").getHall().getId(),
             dictClasses.get("42").getCourse().getName() + "\n" + dictClasses.get("42").getLecturer().getName() + "\n" + dictClasses.get("42").getHall().getId(),
             dictClasses.get("43").getCourse().getName() + "\n" + dictClasses.get("43").getLecturer().getName() + "\n" + dictClasses.get("43").getHall().getId(),
             dictClasses.get("44").getCourse().getName() + "\n" + dictClasses.get("44").getLecturer().getName() + "\n" + dictClasses.get("44").getHall().getId(),
             dictClasses.get("45").getCourse().getName() + "\n" + dictClasses.get("45").getLecturer().getName() + "\n" + dictClasses.get("45").getHall().getId()])
        table.add_row([9 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-', 19 * '-'])

        table.add_row(
            ['\nThursday', dictClasses.get("51").getCourse().getName() + "\n" + dictClasses.get("51").getLecturer().getName() + "\n" + dictClasses.get("51").getHall().getId(),
             dictClasses.get("52").getCourse().getName() + "\n" + dictClasses.get("52").getLecturer().getName() + "\n" + dictClasses.get("52").getHall().getId(),
             dictClasses.get("53").getCourse().getName() + "\n" + dictClasses.get("53").getLecturer().getName() + "\n" + dictClasses.get("53").getHall().getId(),
             dictClasses.get("54").getCourse().getName() + "\n" + dictClasses.get("54").getLecturer().getName() + "\n" + dictClasses.get("54").getHall().getId(),
             dictClasses.get("55").getCourse().getName() + "\n" + dictClasses.get("55").getLecturer().getName() + "\n" + dictClasses.get("55").getHall().getId()])














        # table.add_row(
        #     ['Monday', dictClasses.get("21").getCourse().getName(), dictClasses.get("22").getCourse().getName(),
        #     dictClasses.get("23").getCourse().getName(), dictClasses.get("24").getCourse().getName(),
        #     dictClasses.get("25").getCourse().getName()])
        # table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        # table.add_row(
        #     ['Tuesday', dictClasses.get("31").getCourse().getName(), dictClasses.get("32").getCourse().getName(),
        #      dictClasses.get("33").getCourse().getName(), dictClasses.get("34").getCourse().getName(),
        #      dictClasses.get("35").getCourse().getName()])
        # table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        # table.add_row(
        #     ['Wednesday', dictClasses.get("41").getCourse().getName(), dictClasses.get("42").getCourse().getName(),
        #      dictClasses.get("43").getCourse().getName(), dictClasses.get("44").getCourse().getName(),
        #      dictClasses.get("45").getCourse().getName()])
        # table.add_row(['---------', '----------', '----------', '----------', '----------', '----------'])
        # table.add_row(
        #     ['Thursday', dictClasses.get("51").getCourse().getName(), dictClasses.get("52").getCourse().getName(),
        #      dictClasses.get("53").getCourse().getName(), dictClasses.get("54").getCourse().getName(),
        #      dictClasses.get("55").getCourse().getName()])

        print(table)
