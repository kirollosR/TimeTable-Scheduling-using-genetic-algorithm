import prettytable as prettytable
from Data import Data


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
    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            ['Class #', 'Dept', 'Course(number , max # of students)', 'Room (Capacity)', 'Instructor','TimeAvilable'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " + str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_seatingCapacity())+")",
                           classes[i].get_instructor().get_name() + " (" + str(classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_TimeAvilable().get_time() + " (" + str(classes[i].get_TimeAvilable().get_id()) + ")"])
        print(table)