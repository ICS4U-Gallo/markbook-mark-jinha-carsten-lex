from typing import Dict, List
import json
"""
Markbook Application
Group members: 
"""


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


def print_report(classroom: Dict):
    print("======================")
    print("        Report        ")
    print("Class: " + str(classroom["course_code"]))
    print("Class Average: " + str(class_average(classroom)))
    return None

def store_student_information(classroom: dict):
    with open("class_data.json", "w") as write_file:
        json.dump(classroom, write_file)
    return None

def student_mark_for_assignment(student: Dict, Mark_of_assignment: int):
    student["marks"].append(Mark_of_assignment)
    return None
