from typing import Dict, List
import json
"""
Markbook Application
Group members: 
"""

classroom_list = []


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

        choice = int(input("Choice: "))

        if choice == 1:
            classroom_creation_interface()

        elif choice == 2:
            view_classrooms()

        elif choice == 0:
            return None

        else:
            print('invalid choice')


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
        print("("+ str(index)+ ")", i["course_code"], i["teacher"])
        index += 1

    print()
    print('Type and press enter  ')
    print('to select your choice ')
    print('----------------------')
    option = int(input("Choice: "))
    if option > len(classroom_list):
        print("Incorrect Value")
        return None
    classroom_students_assignments(option)
    return None



def classroom_creation_interface():
    print()
    print('Fill in the classroom information')
    print('---------------------------------')
    ccode = input('Course Code: ')
    cname = input('Course Name: ')
    period = int(input('Period Number: '))
    teacher = input('Name of Teacher: ')
    temp_class = create_classroom(ccode, cname, period, teacher)
    classroom_list.append(temp_class)
    print()
    return None

def classroom_students_assignments(option):
    room = classroom_list[option-1]
    while True:
        print()
        print(room["course_name"], room["teacher"])
        print('---------------------------------')
        print('(1) Create Students')
        print('(2) View Students')
        print('(3) Create Assignments')
        print('(4) View Assignments')
        print('(5) Store class on a file')
        print('(6) View Class information')
        print('(0) Exit')
        print('')
        print('Type and press enter  ')
        print('to select your choice ')
        print('---------------------------------')
        selection = int(input("Choice: "))
        if selection == 0:
            return None

        if selection == 1:
            student = student_creation_interface()
            room["student_list"].append(student)

        if selection == 2:
            room["student_list"] = student_view(room)

        else:
            print("Incorrect Value")


def student_creation_interface():
    first_name = str(input("First Name: "))
    last_name = str(input("Last Name: "))
    gender = str(input("Gender: "))
    image = input("Image: ")
    student_number = int(input("Student Number: "))
    grade = int(input("Grade: "))
    email = str(input("Email: "))
    print('Hit "enter" after entering all the marks')
    marks = [int(item) for item in input("Enter the marks: ").split()]
    print('Hit "enter" when done')
    comments = str(input("Comments: "))
    return create_student(first_name, last_name, gender,
                   image, student_number, grade,
                   email, marks, comments)

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

    print()
    print('Type and press enter  ')
    print('to select your choice ')
    print('----------------------')
    print()
    option = int(input("Choice: "))
    student_list = student_editor(option, student_list, room)
    return student_list

def student_editor(option, student_list, room):
    while True:
        student = student_list[option - 1]
        print('----------------------')
        print('(1) View Information')
        print('(2) Edit Student')
        print('(3) Remove Student')
        print('(4) Make Report Card')
        print('(0) Exit')
        print()
        print('Type and press enter  ')
        print('to select your choice ')
        print('----------------------')
        selection = int(input("Choice: "))
        if selection == 0:
            return student_list

        elif selection == 1:
            for items in student.items():
                print(str(items[0])+" "+str(items[1]))

        elif selection == 2:
            print('Press "enter" to keep it the same')
            first_name = str(input("First Name: "))
            last_name = str(input("Last Name: "))
            gender = str(input("Gender: "))
            image = input("Image: ")
            student_number = input("Student Number: ")
            grade = input("Grade: ")
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

def create_assignment_interface(room: Dict)-> List:
    print()
    print('Fill in the assignment information')
    print('---------------------------------')
    aname = input('Name of assignment: ')
    due_date = input("Due date of assignment:")
    pointers = int(input('Total points: '))
    assignment_list = room["assignment_list"]
    assignment = create_assignment(aname, due_date, pointers)
    assignment_list.append(assignment)
    print()
    return assignment_list




def store_class_information(classroom: dict):
    with open("class_data.txt", "w") as write_file:
        json.dump(classroom, write_file)
    return None

def create_assignment(name: str, due: str, points: int) -> Dict:
    return {"name": name, "due": due, "points": points}

def create_student(first_name: str, last_name: str, gender: str, image, student_number: int, grade: int, email: str,
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

def add_assignment(assignment: Dict, classroom: Dict):
    classroom["assignment_list"].append(assignment)
    return None


def remove_assignment(assignment: Dict, classroom: Dict):
    classroom["assignment_list"].remove(assignment)
    return None


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:

    return {
        "course_code": course_code,
        "course_name": course_name,
        "period": period,
        "teacher": teacher,
        "student_list": [],
        "assignment_list": []
    }


def student_mark_for_assignment(student: Dict, Mark_of_assignment: int):
    student["marks"].append(Mark_of_assignment)
    return None

def sort_students_alphabetically(classroom: Dict):
    alphabetically = sorted(classroom["student_list"])
    return alphabetically

def calculate_average_mark(student: Dict) -> float:
    marks = student["marks"]
    average = 0
    for i in marks:
        average += i

    average = average / len(marks)

    return average


def add_student_to_classroom(student: Dict, classroom: Dict):
    classroom["student_list"].append(student)
    return None


def remove_student_from_classroom(student: Dict, classroom: Dict):
    classroom["student_list"].remove(student)
    return None

def order_marks(student: Dict):
    marks = student["marks"]
    return sorted(marks)


def edit_student(student: Dict, **kwargs: Dict):
    for i in kwargs.items():
        if i[1] != None and i[1] != "":
            student[i[0]] = i[1]

    return None


def student_list(classroom: Dict) -> List:
    return classroom["student_list"]


def assignment_list(classroom: Dict) -> List:
    return classroom["assignment_list"]

def class_average(classroom: Dict) -> float:
    students = classroom["student_list"]
    class_avg = 0
    for i in students:
        class_avg += calculate_average_mark(i)

    class_avg = class_avg/len(students)
    return class_avg


def student_report(classroom: Dict, student: Dict):
    first = student["first_name"]
    last = student["last_name"]

    with open(first+"_"+last+".txt", "w") as f:
        f.write("======================\n")
        f.write("        Report        \n")
        f.write("Class: " + classroom["course_code"]+"\n")
        f.write("Student: " + first + " " + last + "\n")
        f.write("Class Average: " + str(class_average(classroom))+"\n")
        f.write("Mark Breakdown: \n")
        string = ""
        index = 0
        for i in order_marks(student):
            if index == 7:
                index = 0
                f.write("\n")
            f.write(str(i)+" ")
            index += 1

        f.write(string + "\n")

        f.write("Comments:\n")
        f.write(student["comments"]+"\n")
        f.write("======================\n")
    with open(first+"_"+last+".txt", "r") as f:
        contents = f.read()
    print(contents)
    return None

def assignment_report(classroom: Dict):
    ccode = classroom["course_code"]
    with open(ccode + "_" + "assignments" + ".txt", "w") as f:
        f.write("======================\n")
        f.write("   Assignment Report  \n")
        f.write("\n")
        f.write("Class: "+ ccode+ "\n")
        f.write("\n")
        for i in classroom["assignment_list"]:
            if len(i["name"]) > 16:
                f.write("Name: " + i["name"][:15]+ "\n")
                f.write(i["name"][15:]+ "\n")
                f.write("Due Date: " + i["due"] + "\n")
                f.write("Points: /" + i["points"] + "\n")
                f.write("\n")

            else:
                f.write("Name: " + i["name"]+ "\n")
                f.write("Due Date: "+ i["due"]+"\n")
                f.write("Points: /"+ i["points"]+"\n")
                f.write("\n")

        f.write("======================\n")

    with open(ccode + "_" + "assignments"+".txt", "r") as f:
        contents = f.read()
    print(contents)
    return None

gui()
