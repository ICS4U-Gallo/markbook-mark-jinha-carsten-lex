from typing import Dict, List
import json
"""
Markbook Application
Group members: Lex, Jinha, Carsten, Mark
"""

classroom_list = []

'''The main interface that the user will see'''


def gui():
    while True:
        print('       Markbook       ')
        print('----------------------')
        print('(1) Create A Classroom')
        print('(2) View All Classes')
        print('(0) Exit')
        print('')
        print('Type and press enter  ')
        print('to select your choice ')
        print('----------------------')

        choice = integer_input("Choice: ")

        if choice == 1:
            classroom_creation_interface()

        elif choice == 2:
            view_classrooms()

        elif choice == 0:
            print()
            print("Thank You For Using Markbook")
            print(" _ ")
            print("| |      ")
            print("| |__  _   _  ___ ")
            print("| '_ \| | | |/ _ \ ")
            print("| |_) | |_| |  __/")
            print("|_.__/ \__, |\___|")
            print("        __/ |     ")
            print("       |___/      ")
            return None

        else:
            print('invalid choice')


'''Used to ensure integer inputs'''


def integer_input(value) -> int:
    while True:
        try:
            num = int(input(value))

        except ValueError:
            print("Incorrect input. Enter a number.")

        else:
            return num


'''Shows all the classrooms and allows you to select one to view/edit'''


def view_classrooms():
    print()
    print('        Classes       ')
    print('----------------------')
    if classroom_list == []:
        print("No Classes added.")
        print()
        return
    index = 1
    for i in classroom_list:
        print("(" + str(index) + ")", i["course_code"], i["teacher"])
        index += 1
    print("(0) Exit")
    print()
    print('Type and press enter  ')
    print('to select your choice ')
    print('----------------------')
    option = integer_input("Choice: ")
    if option > len(classroom_list):
        print("Incorrect Value")
        return None
    if option == 0:
        return None
    classroom_students_assignments(option)
    return None


'''Here you can create your classroom'''


def classroom_creation_interface():
    print()
    print('Fill in the classroom information')
    print('---------------------------------')
    ccode = input('Course Code: ')
    cname = input('Course Name: ')
    period = integer_input("Period Number: ")
    teacher = input('Name of Teacher: ')
    temp_class = create_classroom(ccode, cname, period, teacher)
    classroom_list.append(temp_class)
    print()
    return None


'''Here you can view/edit assignments and students for a specific class
You can also create an assignment report, store class information on a file
You can also view the classroom's information'''


def classroom_students_assignments(option):
    room = classroom_list[option-1]

    while True:
        print()
        print(room["course_name"], room["teacher"])
        print('---------------------------------')
        print('(1) Create Students')
        print('(2) View/Edit Students')
        print('(3) Create Assignments')
        print('(4) View/Edit Assignments')
        print('(5) Assignment Report')
        print('(6) Store class on a file')
        print('(7) View Class information')
        print('(0) Exit')
        print('')
        print('Type and press enter  ')
        print('to select your choice ')
        print('---------------------------------')
        selection = integer_input("Choice: ")
        if selection == 0:
            return None

        elif selection == 1:
            student = student_creation_interface()
            room["student_list"].append(student)

        elif selection == 2:
            room["student_list"] = student_view(room)

        elif selection == 3:
            room["assignment_list"].append(create_assignment_interface())

        elif selection == 4:
            room["assignment_list"] = assignment_viewer(room)

        elif selection == 5:
            assignment_report(room)

        elif selection == 6:
            store_class_information(room)

        elif selection == 7:
            index = 0
            titles = ["Course Code: ", "Course Name: ", "Period: ",
                      "Teacher: ", "Student List: ", "Assignment List: "]
            for values in room.values():
                if titles[index] == "Student List: ":
                    print(titles[index], end=" ")
                    for i in values:
                        print(i["first_name"] + " " + i["last_name"], end=" ")

                    print()

                elif titles[index] == "Assignment List: ":
                    print(titles[index], end=" ")
                    for i in values:
                        print(i["name"], end=" ")

                    print()

                else:
                    print(titles[index]+str(values))
                index += 1

        else:
            print("Incorrect Value")


'''This is the interface that the user sees when creating a student'''


def student_creation_interface():
    first_name = str(input("First Name: "))
    last_name = str(input("Last Name: "))
    gender = str(input("Gender: "))
    image = input("Image: ")
    student_number = integer_input("Student Number: ")
    grade = integer_input("Grade: ")
    email = str(input("Email: "))
    print('Hit "enter" after entering all the marks or enter no marks')
    print('Make sure to have spaces between each mark')
    marks = [int(item) for item in input("Enter the marks: ").split()]
    print('Hit "enter" when done')
    comments = str(input("Comments: "))
    return create_student(first_name, last_name, gender, image, student_number,
                          grade, email, marks, comments)


'''This allows you to view and select all the students in a specific class'''


def student_view(room):
    student_list = room["student_list"]
    print()
    print('Students:', room["course_name"])
    print('----------------------')
    if student_list == []:
        print("No students added.")
        print()
        return student_list
    index = 1
    for i in student_list:
        print("(" + str(index) + ")", i["first_name"], i["last_name"])
        index += 1
    print("(0) Exit")

    print()
    print('Type and press enter  ')
    print('to select your choice ')
    print('----------------------')
    print()
    option = integer_input("Choice: ")
    if option == 0:
        return student_list
    if option > len(student_list):
        print("Invalid Input")
        return student_list
    student_list = student_editor(option, student_list, room)
    return student_list


'''This allows you to view/edit/remove students.
You can make and print their report card here
and edit/remove/add marks'''


def student_editor(option, student_list, room):
    while True:
        student = student_list[option - 1]
        print('----------------------')
        print('(1) View Information')
        print('(2) Edit Student')
        print('(3) Remove Student')
        print('(4) Make Report Card')
        print('(5) Add Marks')
        print('(6) Edit Marks')
        print('(0) Exit')
        print()
        print('Type and press enter  ')
        print('to select your choice ')
        print('----------------------')
        selection = integer_input("Choice: ")
        if selection == 0:
            return student_list

        elif selection == 1:
            print()
            title = ["First Name: ", "Last Name: ",
                     "Gender: ", "Image: ", "Student Number: ",
                     "Grade: ", "Email: ", "Marks: ", "Comments: "]
            index = 0
            for values in student.values():
                if values == list:
                    temp = ' '.join(values)
                    print(title[index]+temp)

                else:
                    print(str(title[index]) + str(values))

                index += 1

        elif selection == 2:
            print('Press "enter" to keep it the same')
            first_name = str(input("First Name: "))
            last_name = str(input("Last Name: "))
            gender = str(input("Gender: "))
            image = input("Image: ")
            student_number = integer_input("Student Number: ")
            grade = integer_input("Grade: ")
            email = str(input("Email: "))
            comments = str(input("Comments: "))
            info = {"first_name": first_name,
                    "last_name": last_name,
                    "gender": gender,
                    "image": image,
                    "student_number": student_number,
                    "grade": grade,
                    "email": email,
                    "comments": comments}
            edit_student(student, **info)

        elif selection == 3:
            if len(student_list) == 1:
                return []

            else:
                student_list.pop(option-1)

            return student_list

        elif selection == 4:
            student_report(room, student)

        elif selection == 5:
            print('Hit "enter" after entering all the marks')
            marks = student["marks"]
            for item in input("Enter the marks: ").split():
                marks.append(int(item))

            student["marks"] = marks

        if selection == 6:
            print('Rewrite each mark and hit "enter" afterwards')
            temp = []
            for i in student["marks"]:
                newmark = int(input(str(i) + ": "))
                temp.append(newmark)
                student["marks"] = temp

        if selection > 6:
            print("Invalid Input")


'''This is the interface that allows the user to create an assignment
for a specific class'''


def create_assignment_interface() -> Dict:
    print()
    print('Fill in the assignment information')
    print('---------------------------------')
    aname = input('Name of assignment: ')
    due_date = input('Due date of assignment: ')
    pointers = integer_input("Total Points: ")
    assignment = create_assignment(aname, due_date, pointers)
    print()
    return assignment


'''This function allows you to view/select all the assignments in a specific
class'''


def assignment_viewer(room: Dict):
    alist = room["assignment_list"]
    print()
    print('Assignments:', room["course_name"])
    print('-------------------------')
    if alist == []:
        print("No assignments added")
        return []

    index = 1
    for i in alist:
        print("(" + str(index) + ")", i["name"])
        index += 1

    print("(0) Exit")
    print()
    print('Type and press enter  ')
    print('to select your choice ')
    print('----------------------')
    print()
    option = integer_input("Choice: ")
    if option == 0:
        return alist
    if option > len(alist):
        print("Invalid Input")
        return alist
    alist = assignment_editor(option, alist, room)
    return alist


'''This allows you to view/edit/remove a specific assignment'''


def assignment_editor(option, alist, room):
    assignment = alist[option - 1]
    while True:
        print('----------------------')
        print('(1) View Assignment')
        print('(2) Edit Assignment')
        print('(3) Remove Assignment')
        print('(0) Exit')
        print()
        print('Type and press enter  ')
        print('to select your choice ')
        print('----------------------')
        selection = integer_input("Choice: ")
        if selection == 0:
            return alist

        elif selection == 1:
            titles = ["Name: ", "Due: ", "Points: "]
            i = 0
            for items in assignment.items():
                print(titles[i]+str(items[1]))
                i += 1

        elif selection == 2:
            print('Press "enter" to keep it the same')
            name = str(input("Enter the name: "))
            due = str(input("Enter the due date: "))
            points = input("Enter the points: ")
            info = {"name": name,
                    "due": due,
                    "points": points}
            edit_assignment(assignment, **info)

        elif selection == 3:
            if len(alist) == 1:
                return []

            else:
                remove_assignment(assignment, room)
                alist.pop(option-1)

            return student_list

        else:
            print("Invalid Input")


'''This function stores a classrooms infromation on a .txt file'''


def store_class_information(classroom: Dict):
    with open(classroom["course_code"]+".txt", "w") as write_file:
        json.dump(classroom, write_file)
    return None


'''This function creates the assignment dictionary'''


def create_assignment(name: str, due: str, points: int) -> Dict:
    return {"name": name, "due": due, "points": points}


'''This function creates the student dictionary'''


def create_student(first_name: str, last_name: str, gender: str, image,
                   student_number: int, grade: int, email: str,
                   marks: List[float], comments: str):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "image": image,
        "student_number": student_number,
        "grade": grade,
        "email": email,
        "marks": marks,
        "comments": comments

    }


'''This function adds an assignment to the "assignment_list"
of a specific classroom'''


def add_assignment(assignment: Dict, classroom: Dict):
    classroom["assignment_list"].append(assignment)
    return None


'''This function removes an assignment from the "assignment_list" of
a specific function'''


def remove_assignment(assignment: Dict, classroom: Dict):
    classroom["assignment_list"].remove(assignment)
    return None


'''This function creates a classroom'''


def create_classroom(course_code: str, course_name: str, period: int,
                     teacher: str) -> Dict:

    return {
        "course_code": course_code,
        "course_name": course_name,
        "period": period,
        "teacher": teacher,
        "student_list": [],
        "assignment_list": []
    }


'''This function sorts students by alphabetical order'''


def sort_students_alphabetically(classroom: Dict):
    alphabetically = sorted(classroom["student_list"])
    return alphabetically


'''This function  calculates the average mark of a student'''


def calculate_average_mark(student: Dict) -> float:
    marks = student["marks"]
    average = 0
    for i in marks:
        average += i

    average = average / len(marks)

    return average


'''This function adds a student to the classroom'''


def add_student_to_classroom(student: Dict, classroom: Dict):
    classroom["student_list"].append(student)
    return None


'''This function removes a student from a specific classroom'''


def remove_student_from_classroom(student: Dict, classroom: Dict):
    classroom["student_list"].remove(student)
    return None


'''This function allows you to edit a student'''


def edit_student(student: Dict, **kwargs: Dict):
    for i in kwargs.items():
        if i[1] is not None and i[1] != "":
            student[i[0]] = i[1]

    return None


'''This function returns a list of all the students'''


def student_list(classroom: Dict) -> List:
    return classroom["student_list"]


'''This function returns a list of all the assignments'''


def assignment_list(classroom: Dict) -> List:
    return classroom["assignment_list"]


'''This function calculates the class average'''


def class_average(classroom: Dict) -> float:
    students = classroom["student_list"]
    class_avg = 0
    for i in students:
        class_avg += calculate_average_mark(i)

    class_avg = class_avg/len(students)
    return class_avg


'''This function edits the assignment'''


def edit_assignment(assignment: Dict, **kwargs: Dict):
    for i in kwargs.items():
        if i[1] is not None and i[1] != "":
            assignment[i[0]] = i[1]

    return None


'''This function creates a student report'''


def student_report(classroom: Dict, student: Dict):
    first = student["first_name"]
    last = student["last_name"]
    marks = student["marks"].copy()
    print()
    with open(first + "_" + last + ".txt", "w") as f:
        f.write("======================\n")
        f.write("        Report        \n")
        f.write("Class: " + classroom["course_code"] + "\n")
        f.write("Student: " + first + " " + last + "\n")
        f.write("Class Average: " + str(class_average(classroom)) + "\n")
        f.write("Mark Breakdown: \n")
        string = ""
        index = 0
        for i in sorted(marks):
            if index == 7:
                index = 0
                f.write("\n")
            f.write(str(i) + " ")
            index += 1

        f.write(string + "\n")

        f.write("Comments:\n")
        f.write(student["comments"] + "\n")
        f.write("======================\n")
    with open(first + "_" + last + ".txt", "r") as f:
        contents = f.read()
    print(contents)
    return None


'''This function creates the assignment report'''


def assignment_report(classroom: Dict):
    ccode = classroom["course_code"]
    with open(ccode + "_" + "assignments" + ".txt", "w") as f:
        f.write("======================\n")
        f.write("   Assignment Report  \n")
        f.write("\n")
        f.write("Class: " + ccode + "\n")
        f.write("\n")
        for i in classroom["assignment_list"]:
            if len(i["name"]) > 16:
                f.write("Name: " + i["name"][:15] + "\n")
                f.write(i["name"][15:] + "\n")
                f.write("Due Date: " + i["due"] + "\n")
                f.write("Points: /" + str(i["points"]) + "\n")
                f.write("\n")

            else:
                f.write("Name: " + i["name"] + "\n")
                f.write("Due Date: " + i["due"] + "\n")
                f.write("Points: /" + str(i["points"]) + "\n")
                f.write("\n")

        f.write("======================\n")

    with open(ccode + "_" + "assignments" + ".txt", "r") as f:
        contents = f.read()
    print(contents)
    return None


gui()
