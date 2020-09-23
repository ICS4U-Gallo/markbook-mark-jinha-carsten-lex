from typing import Dict, List
import json
"""
Markbook Application
Group members: 
"""
def gui():
    print('==================')
    print('=====markbook=====')
    print('Type 1 to create a classroom')
    print('Type 2 to see all classes')
    print('Type 0 to exit')
    choice = int(input())
    while True and choice != 0:
        if choice == 1:
            print('Fill in the classroom information')
            course_code = input('Select course code')
            course_name = input('Select course name')
            period = int(input('Select period'))
            teacher = input('Select teacher')
            create_classroom(course_code, course_name, period, teacher)
        elif choice == 2:
            #list_classrooms()
            pass
        else:
            print('invalid choice')
            choice = int(input())

def store_class_information(classroom: dict):
    with open("class_data.json", "w") as write_file:
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
