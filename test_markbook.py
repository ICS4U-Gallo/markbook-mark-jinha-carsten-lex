import pytest

import markbook


def test_create_assigment():
    assignment1 = markbook.create_assignment(name="Assignment One",
                                            due="2019-09-21",
                                            points=100)
    expected = {
        "name": "Assignment One",
        "due": "2019-09-21",
        "points": 100
    }
    assert assignment1 == expected

    assignment2 = markbook.create_assignment(name="Assignment Two",
                                             due=None,
                                             points=1)
    assert assignment2["name"] == "Assignment Two"
    assert assignment2["due"] is None
    assert assignment2["points"] == 1


def test_create_classroom():
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")

    assert classroom["course_code"] == "ICS4U"
    assert classroom["course_name"] == "Computer Science"
    assert classroom["period"] == 2
    assert classroom["teacher"] == "Mr. Gallo"
    # The classroom needs to be created with
    # empty lists for students and assignments
    assert classroom["student_list"] == []
    assert classroom["assignment_list"] == []


@pytest.mark.skip
def test_calculate_average_mark():
    student = {
        "marks": [50, 100]
    }
    assert markbook.calculate_average_mark(student) == 75.0


@pytest.mark.skip
def test_add_student_to_classroom():
    """
    Dependencies:
        - create_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    student = {"first_name": "John", "last_name": "Smith"}

    assert len(classroom["student_list"]) == 0
    markbook.add_student_to_classroom(student, classroom)
    assert type(classroom["student_list"]) is list
    assert len(classroom["student_list"]) == 1


@pytest.mark.skip
def test_remove_student_from_classroom():
    """
    Dependencies:
        - create_classroom()
        - add_student_to_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    student = {"first_name": "John", "last_name": "Smith"}

    markbook.add_student_to_classroom(student, classroom)
    assert len(classroom["student_list"]) == 1
    markbook.remove_student_from_classroom(student, classroom)
    assert type(classroom["student_list"]) is list
    assert len(classroom["student_list"]) == 0


@pytest.mark.skip
def test_edit_student():
    student = {"first_name": "John", "last_name": "Smith", "grade": 10}
    markbook.edit_student(student, first_name="Frank", last_name="Bell")
    assert student["first_name"] == "Frank"
    assert student["last_name"] == "Bell"
    assert student["grade"] == 10

    
def test_create_student():
    student = markbook.create_student("Alexander", "Jorge", "Male", None, 123456, 12, "Alexander.Jorge21@ycdsbk12.ca", [], "Exceptional student")
    assert student["first_name"] == "Alexander"
    assert student["last_name"] == "Jorge"
    assert student["gender"] == "Male"
    assert student["image"] is None 
    assert student["student_number"] == 123456
    assert student["grade"] == 12
    assert student["email"] == "Alexander.Jorge21@ycdsbk12.ca"
    assert student["marks"] == []
    assert student["comments"] == "Exceptional student"   
    
    
def test_add_assignment():
    assignment = markbook.create_assignment("Math CPT", "October 21, 1999", 100)
    classroom = markbook.create_classroom("MHF4U", "Advanced Functions", 3, "Mr.Smith", ["Emma", "Ethan", "Nicholas"], [])
    markbook.add_assignment(assignment, classroom)
    assert len(classroom["assignment_list"]) == 1
    assert type(classroom["assignment_list"]) is list
    
def test_remove_assignment():
    assignment = markbook.create_assignment ("Math CPT", "October 21, 1999", 100)
    classroom = markbook.create_classroom("MHF4U", "Advanced Functions", 3, "Mr.Smith", ["Emma", "Ethan", "Nicholas"], [])
    markbook.add_assignment(assignment, classroom)
    assert len(classroom["assignment_list"]) == 1
    markbook.remove_assignment(assignment, classroom)
    assert len(classroom["assignment_list"]) == 0
    assert type(classroom["assignment_list"]) is list
  
    
def test_sort_students_alphabetically():
    classroom = markbook.create_classroom("MHF4U", "Advanced Functions", 3, "Mr.Smith", ["Jayden","Samuel, ""Emma", "Ethan", "Nicholas"], [])
    markbook.sort_students_alphabetically(classroom)
    assert classroom["student_list"] == ["Emma", "Ethan", "Jayden", "Nicholas", "Samuel"]
    assert type(classroom["student_list"]) is list  
    
    
def test_order_marks():
    student = markbook.create_student("Alexander", "Jorge", "Male", None, 123456, 12, "Alexander.Jorge21@ycdsbk12.ca", [101,99, 97, 102, 65, 87, 40, 300], "Exceptional student")
    markbook.order_marks(student)
    assert student["marks"] == [40, 65, 87, 97, 99, 102, 300]
    assert len(student["marks"]) == 7
    assert type(student["marks"]) is list    
    
    
def test_class_average():
    jayden = markbook.create_student("Jayden", "Smith", "Male", None, 5678910, 10, "Jayden.Smith34@ycdsbk12.ca", [50, 60, 70, 80], None)
    samuel = markbook.create_student("Samuel", "Jiang", "Male", None, 8765432, 10, "Samuel.Jiang34@ycdsbk12.ca", [90, 30, 70, 50], None)
    emma = markbook.create_student("Emma", "Winnasdale". "female", None, 9567823, 10, "Emma.Winnasdale34@ycdsbk12.ca", [60, 100, 70, 80], None)
    classroom = markbook.create_classroom("MHF4U", "Advanced Functions", 3, "Mr.Smith", [], [])
    markbook.add_student_to_classroom(jayden ,classroom)
    markbook.add_student_to_classroom(samuel ,classroom)
    markbook.add_student_to_classroom(emma ,classroom)
    assert classroom["student_list"] == 3
    avg_of_class = markbook.class_average(classroom)
    assert avg_of_class == 67.5
